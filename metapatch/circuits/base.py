"""Circuit base class."""

from dataclasses import is_dataclass, fields
from typing import Any, Dict, List, Optional
from metapatch.base import Circuit


def dataclass_to_circuit(
    circuit: Any, section: Optional[str] = None, comment: Optional[str] = None
) -> Circuit:
    """Convert a dataclass to a circuit."""
    if not is_dataclass(circuit):
        raise ValueError("Error: Circuit must be a dataclass.")
    parameters: Dict[str, str] = {}
    for field in fields(circuit):
        value = getattr(circuit, field.name)
        field_name = field.name
        if field.name.endswith("_"):
            field_name = field.name[:-1]
        if value:
            parameters[field_name] = value

    circuit_name = type(circuit).__name__.lower()
    return Circuit(circuit_name, parameters, comment, section)
