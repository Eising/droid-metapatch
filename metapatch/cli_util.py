#!/usr/bin/env python3
"""This is a small helper script that can be used to speed up some of the patch building."""
import argparse
import sys
import os
import re

from dataclasses import dataclass
from typing import Iterator, Dict, List, Optional


@dataclass
class Token:
    """Token container class."""

    type: str
    value: str
    line: int
    column: int


def tokenize(patch: str) -> Iterator[Token]:
    """Tokenize a patch."""
    spec = [
        ("CONTROLLER", r"(?<=\[)([a-z][0-9]+[a-z0-9]*)(?=\])"),
        ("CIRCUIT", r"(?<=\[)([a-z]+)(?=\])"),
        ("PARAM", r"([a-z0-9]+)\s*(?= =)"),
        ("VALUE", r"(?<= =\s)([^\s].*)(?=\n)"),
        ("NEWLINE", r"\n"),
        ("COMMENT", r"(?<=#\s)(.*)(?=\n)"),
    ]

    tok_regex = "|".join("(?P<%s>%s)" % pair for pair in spec)
    line_num = 1
    line_start = 0
    section_header = "-" * 49
    in_section = False
    section_title_derived = False
    for mo in re.finditer(tok_regex, patch):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        if kind == "NEWLINE":
            line_start = mo.end()
            line_num += 1
            continue
        if kind == "COMMENT" and value == section_header:
            in_section = not in_section
            if in_section:
                section_title_derived = False
            continue
        if in_section:
            if kind == "COMMENT":
                if section_title_derived:
                    kind = "SECTION_COMMENT"
                else:
                    kind = "SECTION"
                    section_title_derived = True

        if kind is None:
            continue
        yield Token(kind, value, line_num, column)


def get_patch_stdin() -> str:
    """Read a patch from stdin."""
    buffer = []
    empty_lines = 0
    while True:
        line = sys.stdin.readline()
        if line == "\n":
            empty_lines += 1
            if empty_lines == 2:
                break
            else:
                buffer.append(line.rstrip("\n"))
        elif line == "":
            break
        else:
            buffer.append(line.rstrip("\n"))

    return "\n".join(buffer)


def _generate_section(name, comment: Optional[str], indent: bool = False) -> str:
    """Generate section."""
    indstr = ""
    c_indstr = " "
    level_start = 8
    level_cont = 12
    if indent:
        indstr = f"\n{' ' * level_start}"
        c_indstr = f"\n{' ' * level_cont}"
    if comment:
        comment = _format_comment(comment)
        return f'{indstr}self.add_section({c_indstr}"{name}",{c_indstr}"{comment}"{indstr})'

    return f'{indstr}self.add_section("{name}")'


def _params_to_str(params: Dict[str, str], start_indent: int = 4) -> str:
    """Convert params to string."""
    level_1 = start_indent
    level_2 = level_1 + 4
    indstr = " " * level_1
    c_indstr = " " * level_2

    text = "\n"
    text += indstr + "{"
    if not params:
        text += "}"
        return text
    text += "\n"
    for key, value in params.items():
        text += f'{c_indstr}"{key}": "{value}",\n'

    text += indstr + "}"
    return text


def _format_comment(comment: str) -> str:
    """Format comment.

    This escapes the newline characters.
    """
    return comment.replace("\n", "\\n")


def _generate_controller(name: str, index: int, indent: bool = False) -> str:
    """Generate a controller."""
    level_1 = 0
    if indent:
        level_1 = 8

    indstr = " " * level_1
    return f"{indstr}self.add_controller(\"{name}\", {index})"


def _generate_circuit(
    name: str, params: Dict[str, str], comment: Optional[str], indent: bool = False
) -> str:
    """Generate circuit."""
    level_1 = 0
    if indent:
        level_1 = 8

    level_2 = level_1 + 4

    indstr = f"\n{' ' * level_1}"
    c_indstr = f"\n{' ' * level_2}"
    param_str = _params_to_str(params, level_2)

    if comment:
        comment = _format_comment(comment)
        return f'{indstr}self.add_circuit({c_indstr}"{name}",{param_str},{c_indstr}"{comment}"{indstr})'
    return f'{indstr}self.add_circuit({c_indstr}"{name}",{param_str}{indstr})'


def generate_boilerplate(patch: str) -> str:
    """Generate full boilerplate."""
    boilerplate = """
import metapatch

class PatchGenerator(metapatch.PatchGenerator):
    \"\"\"Patch Generator boilerplate.

    Change this to something more meaningful.
    Also remember to add parameters and presets.
    \"\"\"
    title = "Title of your patch generator"  # CHANGEME
    description = "Description of your patch generator"  # CHANGEME

    def generate(self) -> None:
        \"\"\"Patch generator function.

        Modify this function to create your patch generator.
        \"\"\"
"""
    boilerplate += patch_to_metapatch(patch, indent=True)

    boilerplate += """
if __name__ == "__main__":
    PatchGenerator.run()
    """
    return boilerplate


def patch_to_metapatch(patch: str, indent: bool = False) -> str:
    """Convert a patch to a partial metapatch."""
    metapatch = []
    sections = {}
    circuits = []
    controllers = []
    curr_params = {}
    curr_param: Optional[str] = None
    curr_section: Optional[str] = None
    curr_circuit: Optional[str] = None
    curr_circuit_comments: List[str] = []
    for token in tokenize(patch):
        if token.type == "SECTION":
            curr_section = token.value
            sections[curr_section] = []
            continue
        elif token.type == "CONTROLLER":
            # Discard all previous comments
            controllers.append(token.value)
            curr_circuit_comments = []

        elif token.type == "CIRCUIT":
            if curr_circuit:
                circuits.append({curr_circuit: curr_params})
            curr_circuit = token.value
            curr_params = {}
            if curr_circuit_comments:
                curr_params["__comment"] = "\n".join(curr_circuit_comments)
                curr_circuit_comments = []
            if curr_section:
                curr_params["__section"] = curr_section

        elif token.type == "PARAM":
            curr_params[token.value] = ""
            curr_param = token.value
        elif token.type == "VALUE":
            curr_params[curr_param] = token.value

            curr_param = None
        elif token.type == "SECTION_COMMENT":
            sections[curr_section].append(token.value)
        elif token.type == "COMMENT":
            curr_circuit_comments.append(token.value)

    if curr_circuit:
        final_circuit = {curr_circuit: curr_params}
        if not circuits or final_circuit != circuits[-1]:
            circuits.append(final_circuit)

    for index, controller in enumerate(controllers, start=1):
        metapatch.append(_generate_controller(controller, index, indent))
    all_sections = [
        param.get("__section", "__NONE")
        for circuit in circuits
        for _, param in circuit.items()
    ]
    unique_sections = set(all_sections)
    for section in unique_sections:
        if section == "__NONE":
            # No section.
            section_circuits = [
                circ
                for circ in circuits
                for params in circ.values()
                if "__section" not in params
            ]
        else:
            section_comment = sections.get(section)
            if section_comment:
                section_comment = "\n".join(section_comment)
            metapatch.append(_generate_section(section, section_comment, indent))
            section_circuits = [
                circ
                for circ in circuits
                for params in circ.values()
                if params.get("__section") == section
            ]

        for circuit in section_circuits:
            for circuit_name, circuit_params in circuit.items():
                circuit_comment: Optional[str] = None
                if "__comment" in circuit_params:
                    circuit_comment = circuit_params["__comment"]
                    del circuit_params["__comment"]
                if "__section" in circuit_params:
                    del circuit_params["__section"]

                metapatch.append(
                    _generate_circuit(
                        circuit_name, circuit_params, circuit_comment, indent
                    )
                )

    return "\n".join(metapatch)


def cli() -> argparse.Namespace:
    """Parse cli."""
    parser = argparse.ArgumentParser(description="Metapatch helper script.")
    parser.add_argument(
        "infile",
        nargs="?",
        type=argparse.FileType("r", encoding="utf-8"),
        default=sys.stdin,
        help="Input file. Defaults to stdin.",
    )
    parser.add_argument(
        "outfile",
        nargs="?",
        type=argparse.FileType("w", encoding="utf-8"),
        default=sys.stdout,
        help="Output file. Defaults to stdout.",
    )
    parser.add_argument(
        "--boilerplate",
        action="store_true",
        help="Generate a full example patch generator.",
    )
    parser.epilog = (
        "If called without any arguments, you may input one or more droid circuits, "
        "and get the corresponding python code back."
    )
    args = parser.parse_args()
    return args


def main() -> None:
    """Main function."""
    args = cli()
    if args.infile.isatty():
        print("Paste a circuit configuration and finish with ctrl-d.\n")
    buffer = args.infile.read()
    if args.boilerplate:
        output = generate_boilerplate(buffer)
    else:
        output = patch_to_metapatch(buffer)

    args.outfile.write(output + os.linesep)


if __name__ == "__main__":
    main()
