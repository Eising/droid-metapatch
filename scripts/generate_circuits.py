"""Generate circuits.

This generates objects that matches the available circuits with all their
parameters. These can be used instead of adding circuits by hand.
"""

import argparse
import json
import re
import sys
import textwrap
import keyword
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, TypedDict

from pylatexenc.latex2text import LatexNodes2Text


CIRCUIT_TEMPLATE = """
@dataclass
class {circuitname}(DroidCircuit):
    \"\"\"Circuit {internalname}.

    {title}

    Args:
{inputs}
{outputs}
    \"\"\"
"""

INIT_HEADER = """\"\"\"DROID circuits module. These circuits are auto-generated from circuits.json.

.. include:: README.md
\"\"\"

__docformat__ = "google"
"""

MODULE_HEADER = """\"\"\"DROID circuits. These circuits are auto-generated from circuits.json.\"\"\"

from dataclasses import dataclass
from typing import Optional

from metapatch.circuits.base import DroidCircuit"""

PARAM_TEMPLATE = "    {param}: Optional[str] = None"

INIT_TEMPLATE = "from .{filename} import ("


def _strip_latex(text: str) -> str:
    """Strip latex formatting from string."""
    #  Some patterns I've found.
    # macros = {
    #     "\\meighteen": "MASTER18",
    # }
    patterns = [(r"\\msixteen", "MASTER"), (r"\\meighteen", "MASTER18")]
    for pat, replacement in patterns:
        text = re.sub(pat, replacement, text)
    text = LatexNodes2Text().latex_to_text(text).strip("\t")
    # Modify those frameboxes that remain
    text = text.replace("[5mm][c]", "")
    return text


def _reformat_inline_list(text: str, indent: int) -> str:
    """Find inline lists."""
    if "*" not in text:
        return text
    # dedent the text
    list_indent = indent * " "
    continuation = list_indent + "  "
    text = textwrap.dedent(text)
    lines = ""
    sections = []
    for line in re.split(r"\s{2,}", text):
        line = line.replace("\n", " ")
        if line.startswith("*"):
            sections.append((True, line))
        else:
            sections.append((False, line))
    for is_list, line in sections:
        if not is_list:
            lines += "\n".join(
                textwrap.wrap(
                    line,
                    width=88,
                    initial_indent=list_indent,
                    subsequent_indent=list_indent,
                )
            )
        else:
            lines += "\n".join(
                textwrap.wrap(
                    line,
                    width=88,
                    initial_indent=list_indent,
                    subsequent_indent=continuation,
                )
            )
        lines += "\n"
    return lines


@dataclass
class Parameter:
    """Parameter."""

    name: str
    type: str
    description: str
    ramsize: int
    direction: str

    def __post_init__(self) -> None:
        """Reformat name if it collides with python."""
        if keyword.iskeyword(self.name):
            self.name += "_"

    @property
    def clean_description(self) -> str:
        """Return description without LaTeX."""
        # Join lines together
        description = " ".join(self.description.splitlines())
        return _strip_latex(description)

    @property
    def synopsis(self) -> str:
        """Return a synopsis for the docstring."""
        indent = " " * 8
        descr_indent = " " * 10
        heading_str = f"{self.name} ({self.type}):"
        heading = textwrap.indent(heading_str, indent)
        body = "\n".join(
            textwrap.wrap(
                self.clean_description,
                width=88,
                initial_indent=descr_indent,
                subsequent_indent=descr_indent,
            )
        )
        if "*" in body:
            body = _reformat_inline_list(body, 10)
        return "\n".join([heading, body, ""])

    def __str__(self) -> str:
        """Generate string."""
        return PARAM_TEMPLATE.format(param=self.name)


@dataclass
class Circuit:
    """Circuit container."""

    name: str
    title: str
    category: str
    parameters: List[Parameter] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Remove latex from title for good meassure."""
        self.title = _strip_latex(self.title)

    def __str__(self) -> str:
        """Generate string."""
        props = "\n".join([str(parameter) for parameter in self.parameters])
        input_params = "\n".join(
            [
                parameter.synopsis
                for parameter in self.parameters
                if parameter.direction == "input"
            ]
        )
        output_params = "\n".join(
            [
                parameter.synopsis
                for parameter in self.parameters
                if parameter.direction == "output"
            ]
        )

        circuit = CIRCUIT_TEMPLATE.format(
            circuitname=self.name.capitalize(),
            internalname=self.name,
            title=self.title,
            inputs=input_params,
            outputs=output_params,
        )

        return "\n\n".join([circuit, props])


class DroidControllerJSON(TypedDict):
    """Typing of the controllers JSON."""

    ramsize: int


class DroidParamJSON(TypedDict):
    """Typing of the DROID circuit JSON."""

    type: str
    ramsize: int
    count: int
    default: str
    prefix: str
    name: str
    start_at: int
    description: str


class DroidCircuitJSON(TypedDict):
    """Typing of the DROID circuit JSON."""

    category: str
    ramsize: int
    title: str
    description: str
    inputs: list[DroidParamJSON]
    outputs: list[DroidParamJSON]


class DroidOuterJSON(TypedDict):
    """Outer JSON."""

    circuits: dict[str, DroidCircuitJSON]
    controllers: dict[str, DroidControllerJSON]
    available_memory: int


def _parse_parameters(param: DroidParamJSON, direction: str) -> List[Parameter]:
    """Parse parameters."""
    params = []
    if "prefix" in param:
        prefix = param["prefix"]
        start = param["start_at"]
        count = param["count"]
        for step in range(start, count + start):
            p_name = prefix + str(step)
            params.append(
                Parameter(
                    p_name,
                    param["type"],
                    param.get("description", ""),
                    param.get("ramsize"),
                    direction,
                )
            )
    else:
        p_name = param["name"]
        if keyword.iskeyword(p_name):
            p_name = f"{p_name}_"
        params.append(
            Parameter(
                p_name,
                param["type"],
                param.get("description", ""),
                param.get("ramsize"),
                direction,
            )
        )

    return params


def _parse_circuits(json_circuits: DroidOuterJSON) -> List[Circuit]:
    """Perform the actual parsing."""
    circuits: List[Circuit] = []

    for circuit_name, params in json_circuits["circuits"].items():
        inputs = params.get("inputs", [])
        outputs = params.get("outputs", [])
        title = params.get("title", "").strip()
        category = params.get("category", "other")
        circuit = Circuit(circuit_name, title, category)
        for in_param in inputs:
            circuit.parameters.extend(_parse_parameters(in_param, "input"))

        for out_param in outputs:
            circuit.parameters.extend(_parse_parameters(out_param, "output"))

        circuits.append(circuit)

    return circuits


def split_circuits(circuits: List[Circuit]) -> Dict[str, str]:
    """Split circuits into one file per category.

    Returns a dictionary keyed by filename, with the contents of the file as
    value.
    """
    files = {}
    for circuit in circuits:
        filename = f"{circuit.category}.py"
        if filename not in files:
            files[filename] = ""
        files[filename] += f"{circuit}\n"

    return files


def write_circuits(files: Dict[str, str], directory: Path) -> None:
    """Write circuits to files in a directory."""
    assert (
        directory.exists() and directory.is_dir()
    ), "Directory must exist and be a directory."
    for filename, content in files.items():
        filepath = directory / filename
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(MODULE_HEADER)
            f.write("\n")
            f.write(content)
            f.flush()


def write_init(circuits: List[Circuit], directory: Path) -> None:
    """Write circuit imports to the module init file."""
    assert (
        directory.exists() and directory.is_dir()
    ), "Directory must exist and be a directory."
    filepath = directory / "__init__.py"
    content = [INIT_HEADER]
    categorymap = defaultdict(list)
    for circuit in circuits:
        categorymap[circuit.category].append(circuit.name.capitalize())

    for category, c_circuits in categorymap.items():
        content.append(INIT_TEMPLATE.format(filename=category))
        for circuit in c_circuits:
            content.append(f"    {circuit},")
        content.append(")")

    content.append("\n__all__ = (")

    for circuit in sorted(circuits, key=lambda x: x.name):
        content.append(f'    "{circuit.name.capitalize()}",')
    content.append(")")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(content))
        f.flush()


def parse_to_directory(json_circuits: DroidOuterJSON, directory: Path) -> None:
    """Parse circuits and write in smaller files to a directory."""
    circuits = _parse_circuits(json_circuits)
    files = split_circuits(circuits)
    write_circuits(files, directory)
    write_init(circuits, directory)


def parse_circuits(json_circuits: DroidOuterJSON) -> str:
    """Parse circuits."""
    circuits = _parse_circuits(json_circuits)
    circuitstr = "\n\n".join([str(circuit) for circuit in circuits])
    text = [MODULE_HEADER, circuitstr]

    return "\n\n".join(text)


def cli() -> None:
    """Handle CLI."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "circuitsfile",
        type=argparse.FileType("r", encoding="utf-8"),
        help="circuits.json file.",
    )

    parser.add_argument(
        "outfile",
        nargs="?",
        type=argparse.FileType("w", encoding="utf-8"),
        default=sys.stdout,
    )

    parser.add_argument("--directory", "-d", help="Output directory")

    args = parser.parse_args()
    circuits: DroidOuterJSON = json.load(args.circuitsfile)
    if args.directory:
        directory = Path(args.directory)
        assert (
            directory.exists() and directory.is_dir()
        ), "Directory must exist and be a directory."

        print(f"Writing files to directory {directory.absolute()}")
        parse_to_directory(circuits, directory)

    else:
        circuitstr = parse_circuits(circuits)
        args.outfile.write(circuitstr)


if __name__ == "__main__":
    cli()
