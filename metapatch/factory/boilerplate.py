"""Boilerplate functions."""

from typing import List
from .patch_parser import parse_patch
from . import patch_factory


def generate_snippet(patch: str) -> str:
    """Generate a code snippet from a patch."""
    parsed = parse_patch(patch)
    snippet = []
    snippet.append(patch_factory.generate_add_controllers(parsed.controllers))
    for circuit in parsed.circuits:
        for circuitname, params in circuit.items():
            snippet.append(patch_factory.generate_add_circuit(circuitname, params))

    return "\n".join(snippet)


def transform_section_name(section_name: str):
    """Transform a section name into a python function name."""
    section_name = section_name.strip().lower().replace(" ", "_")
    lastchar = -1
    for index, letter in enumerate(section_name):
        if not letter.isalnum() and letter != "_":
            break

        lastchar = index
    lastchar += 1
    section_name = section_name[:lastchar]
    if section_name.endswith("_"):
        section_name = section_name[:-1]
    return section_name


def find_unique_section_name(section_name: str, used_names: List[str]):
    """Find a unique section name."""
    if section_name[-1].isdigit():
        digit = int(section_name[-1])
        while True:
            candidate = section_name[-1] + str(digit)
            if candidate not in used_names:
                return candidate
            digit += 1
    else:
        digit = 2
        while True:
            candidate = section_name + f"_{digit}"
            if candidate not in used_names:
                return candidate
            digit += 1


def generate_boilerplate(patch: str) -> str:
    """Generate boilerplate."""
    parsed = parse_patch(patch)
    pg_fun = [
        patch_factory.generate_pg_function(parsed.controllers),
    ]
    boilerplate = []

    if parsed.sections:
        # We have sections.

        boilerplate.append(patch_factory.header(with_list=True))
        boilerplate.append(patch_factory.pg_class())
        secfunmap = {}
        used_sections = []
        circuits_main = []
        for section_name, circuits in parsed.section_grouped.items():
            if section_name == "__none":
                circuits_main = circuits
                continue

            new_section_name = transform_section_name(section_name)
            if new_section_name in used_sections:
                new_section_name = find_unique_section_name(
                    new_section_name, used_sections
                )

            used_sections.append(new_section_name)
            secfunmap[new_section_name] = section_name
            boilerplate.append(
                patch_factory.generate_section_function(
                    circuits, new_section_name, section_name
                )
            )
        boilerplate.append("\n")
        for circuit in circuits_main:
            for circuit_name, circuit_params in circuit.items():
                pg_fun.append(
                    patch_factory.generate_add_circuit(
                        circuit_name, circuit_params, level=2
                    )
                )

        for secfun, section_name in secfunmap.items():
            # TODO: Pass in transformations
            pg_fun.append(
                patch_factory.generate_transformation(secfun, section_name, {}, [])
            )

        boilerplate.extend(pg_fun)
        boilerplate.append(patch_factory.footer())
        boilerplate.append("\n")
        return "".join(boilerplate)

    boilerplate.append(patch_factory.header())
    for circuit in parsed.circuits:
        for circuit_name, circuit_params in circuit.items():
            pg_fun.append(
                patch_factory.generate_add_circuit(
                    circuit_name, circuit_params, level=2
                )
            )

    boilerplate.append(patch_factory.pg_class())
    boilerplate.extend(pg_fun)
    boilerplate.append("\n")
    boilerplate.append(patch_factory.footer())
    return "".join(boilerplate)
