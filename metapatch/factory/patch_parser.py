"""Rudimentary droid patch parser."""

import re

from dataclasses import dataclass, field
from typing import Iterator, Dict, List, Optional


TCircuitParams = Dict[str, str]
TCircuit = Dict[str, TCircuitParams]
TSectionGroupedCircuits = Dict[str, List[TCircuit]]

TModDefinition = List[str]


@dataclass
class Token:
    """Token container class."""

    type: str
    value: str
    line: int
    column: int


@dataclass
class ParsedPatch:
    """Parsed patch container class."""

    sections: Dict[str, str] = field(default_factory=dict)
    circuits: List[Dict[str, Dict[str, str]]] = field(default_factory=list)
    controllers: List[str] = field(default_factory=list)

    @property
    def section_grouped(self) -> TSectionGroupedCircuits:
        """Group circuits by section."""
        current_section = "__none"
        grouped = {}
        for circuit in self.circuits:
            circuit_name = list(circuit.keys())[0]
            section = circuit[circuit_name].get("__section", current_section)
            if section not in grouped:
                grouped[section] = []
            grouped[section].append(circuit)
            current_section = section
        return grouped


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
    section_re = re.compile(r"----*$")  # This is the regex that Forge uses too.
    in_section = False
    section_title_derived = False
    for mo in re.finditer(tok_regex, patch):
        # This currently throws away the patch title.
        # TODO: Handle top of patch comments
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        if kind == "NEWLINE":
            line_start = mo.end()
            line_num += 1
            continue
        if kind == "COMMENT" and section_re.match(value) is not None:
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


def parse_patch(patch: str) -> ParsedPatch:
    """Parse the patch."""
    sections = {}
    circuits = []
    controllers = []
    curr_params = {}
    curr_param: Optional[str] = None
    curr_section: Optional[str] = None
    curr_circuit: Optional[str] = None
    curr_circuit_comments: List[str] = []
    in_header = True
    for token in tokenize(patch):
        if token.type == "SECTION":
            curr_section = token.value
            sections[curr_section] = []
            in_header = False
            continue
        elif token.type == "CONTROLLER":
            # Discard all previous comments
            controllers.append(token.value)
            curr_circuit_comments = []

        elif token.type == "CIRCUIT":
            in_header = False
            if curr_circuit:
                circuits.append({curr_circuit: curr_params})
            curr_circuit = token.value
            curr_params = {}
            if curr_circuit_comments:
                curr_params["comment"] = "\\n".join(curr_circuit_comments)
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
            if not in_header:
                curr_circuit_comments.append(token.value)

    if curr_circuit:
        final_circuit = {curr_circuit: curr_params}
        if not circuits or final_circuit != circuits[-1]:
            circuits.append(final_circuit)

    return ParsedPatch(sections, circuits, controllers)
