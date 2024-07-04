"""DROID circuits JSON parsing."""

import json
import keyword
from pathlib import Path

from typing import Dict, List, TypedDict

from .types import Circuit, CircuitCollection, Parameter


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
    inputs: List[DroidParamJSON]
    outputs: List[DroidParamJSON]


class DroidOuterJSON(TypedDict):
    """Outer JSON."""

    firmware_version: str
    circuits: Dict[str, DroidCircuitJSON]
    controllers: Dict[str, DroidControllerJSON]
    available_memory: Dict[str, int]


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
                    param.get("ramsize", 0),
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
                int(param.get("ramsize", 0)),
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
        ramsize = params.get("ramsize", 0)
        if not ramsize:
            ramsize = 0
        circuit = Circuit(circuit_name, title, category, ramsize=ramsize)
        for in_param in inputs:
            circuit.parameters.extend(_parse_parameters(in_param, "input"))

        for out_param in outputs:
            circuit.parameters.extend(_parse_parameters(out_param, "output"))

        circuits.append(circuit)

    return circuits


def load_circuits(filename: Path) -> CircuitCollection:
    """Load circuits from file."""
    assert filename.exists(), "Error: Filename does not exist!"
    with open(filename, "r", encoding="utf-8") as f:
        raw_circuits: DroidOuterJSON = json.load(f)

    circuits = _parse_circuits(raw_circuits)
    droid_version = raw_circuits["firmware_version"]

    return CircuitCollection(droid_version, circuits)
