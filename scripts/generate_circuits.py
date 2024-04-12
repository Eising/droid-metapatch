"""Generate circuits.

This generates objects that matches the available circuits with all their
parameters. These can be used instead of adding circuits by hand.
"""

import argparse
import json
import re
import sys
import textwrap
from dataclasses import dataclass, field
from typing import List, TypedDict

from pylatexenc.latex2text import LatexNodes2Text


CIRCUIT_TEMPLATE = """
@dataclass
class {circuitname}:
    \"\"\"Circuit {internalname}.
     {title}

    Inputs:
{inputs}

    Outputs:
{outputs}
    \"\"\"
"""

MODULE_HEADER = """\"\"\"DROID circuits. These circuits are auto-generated from circuits.json.\"\"\"

from dataclasses import dataclass
from typing import Optional
"""

PARAM_TEMPLATE = "    {param}: Optional[str] = None"
COMMENT_TEMPLATE = "    comment: Optional[str] = None"


PYTHON_PROTECTED_WORDS = [
    "and",
    "as",
    "assert",
    "async",
    "await",
    "break",
    "class",
    "continue",
    "def",
    "del",
    "elif",
    "else",
    "except",
    "finally",
    "for",
    "from",
    "global",
    "if",
    "import",
    "in",
    "is",
    "lambda",
    "nonlocal",
    "not",
    "or",
    "pass",
    "raise",
    "return",
    "try",
    "while",
    "with",
    "yield",
]


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
    return text


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
        if self.name in PYTHON_PROTECTED_WORDS:
            self.name += "_"

    @property
    def clean_description(self) -> str:
        """Return description without LaTeX."""
        return _strip_latex(self.description)

    @property
    def synopsis(self) -> str:
        """Return a synopsis for the docstring."""
        indent = " " * 8
        descr_indent = " " * 12
        heading_str = f"{self.name}: {self.type}"
        heading = textwrap.indent(heading_str, indent)
        body = textwrap.indent(self.clean_description, descr_indent)
        return "\n".join([heading, body])

    def __str__(self) -> str:
        """Generate string."""
        return PARAM_TEMPLATE.format(param=self.name)


@dataclass
class Circuit:
    """Circuit container."""

    name: str
    title: str
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

        return "\n\n".join([circuit, props, COMMENT_TEMPLATE])


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
        if p_name in PYTHON_PROTECTED_WORDS:
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


def parse_circuits(json_circuits: DroidOuterJSON) -> str:
    """Parse circuits."""
    circuits: List[Circuit] = []

    for circuit_name, params in json_circuits["circuits"].items():
        inputs = params.get("inputs", [])
        outputs = params.get("outputs", [])
        title = params.get("title", "")
        circuit = Circuit(circuit_name, title)
        for in_param in inputs:
            circuit.parameters.extend(_parse_parameters(in_param, "input"))

        for out_param in outputs:
            circuit.parameters.extend(_parse_parameters(out_param, "output"))

        circuits.append(circuit)
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

    args = parser.parse_args()
    circuits: DroidOuterJSON = json.load(args.circuitsfile)
    circuitstr = parse_circuits(circuits)
    args.outfile.write(circuitstr)


if __name__ == "__main__":
    cli()
