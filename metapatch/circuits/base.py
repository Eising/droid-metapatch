"""Circuit base class."""

from dataclasses import dataclass, is_dataclass, fields, asdict
from typing import Dict, Literal, List, Optional, TypeVar, Protocol, runtime_checkable
from metapatch.base import Circuit


@runtime_checkable
@dataclass
class TDataclass(Protocol):
    pass


T = TypeVar("T", bound=TDataclass)


def dataclass_to_circuit(
    circuit: TDataclass, section: Optional[str] = None, comment: Optional[str] = None
) -> Circuit:
    """Convert a dataclass to a circuit."""
    if not is_dataclass(circuit):
        raise ValueError("Error: Circuit must be a dataclass.")
    parameters: Dict[str, str] = {}
    for field in fields(circuit):
        value = getattr(circuit, field.name)
        field_name = field.name
        if not value:
            continue
        if field.name == "comment" and comment is None:
            comment = value
            continue
        if field.name.endswith("_"):
            field_name = field.name[:-1]
        parameters[field_name] = value

    circuit_name = type(circuit).__name__.lower()
    return Circuit(circuit_name, parameters, comment, section)


def transform(circuits: List[T], **actions: str) -> List[T]:
    """Transform a list of circuits.

    Args:
        select: Add a select parameter to all circuits that support it and have no current select.
        select_at: Add a selectat parameter to all circuits that support it.
        prepend: Add a word to the start of all virtual cable names.
        append: Add a word to the end of all virtual cable names.
        output: If an output is found, change it to value of input (e.g., O2)
        input: If an input is found, change it to the value of input
        gate: If a gate is found, change it to the value of the gate.
    """
    select = actions.get("select")
    select_at = actions.get("select_at")
    if select:
        circuits = [add_select(circuit, select, select_at) for circuit in circuits]

    append: Optional[str] = actions.get("append", None)
    prepend: Optional[str] = actions.get("prepend", None)
    circuits = [rename_cables(circuit, append, prepend) for circuit in circuits]
    if new_input := actions.get("input", None):
        circuits = change_jack(circuits, new_input, "input")
    if new_output := actions.get("output", None):
        circuits = change_jack(circuits, new_output, "output")
    if new_gate := actions.get("gate", None):
        circuits = change_jack(circuits, new_gate, "gate")

    return circuits


def rename_cables(circuit: T, append: Optional[str], prepend: Optional[str]) -> T:
    """Rename cables."""
    if not append and not prepend:
        return circuit

    cables = find_cables(circuit)
    if not cables:
        return circuit

    for fieldname, cablename in cables.items():
        if not prepend:
            prependname = ""
        elif prepend.startswith("_"):
            prependname = prepend
        else:
            prependname = "_" + prepend

        newname = f"{prependname}{cablename}{append or ''}"
        setattr(circuit, fieldname, newname)

    return circuit


def find_cables(circuit: TDataclass) -> Dict[str, str]:
    """Return a dictionary of the input/outputs that contain virtual cables."""
    cables = {}
    for field in fields(circuit):
        value: str = getattr(circuit, field.name)
        if not value:
            continue
        if value.startswith("_"):
            cables[field.name] = value

    return cables


def add_select(circuit: T, select: str, select_at: Optional[str] = None) -> T:
    """Add select."""
    selectfield = [field for field in fields(circuit) if field.name == "select"]
    if not selectfield:
        return circuit
    select_val = getattr(circuit, "select")
    if not select_val:
        setattr(circuit, "select", select)

    if select_val != select:
        # Circuit has a different existing select value.
        return circuit

    if select_at:
        setattr(circuit, "selectat", select_at)

    return circuit


def change_jack(
    circuits: List[T], new_jack: str, jacktype: Literal["input", "output", "gate"]
) -> List[T]:
    """Change jack on a list of circuits.

    There can only be a single distinct value in all of the circuits.
    """
    jackmap = {"input": "I", "output": "O", "gate": "G"}
    start = jackmap[jacktype]
    jacks = set()
    new_circuits = []
    for circuit in circuits:
        circuit_fields = asdict(circuit)
        for key, value in circuit_fields.items():
            if not value:
                continue
            if value.startswith(start):
                jacks.add(value)
                if len(jacks) > 1:
                    raise ValueError(
                        f"Cannot run {jacktype} transformation, more than one unique {jacktype} found."
                    )
                setattr(circuit, key, new_jack)
            new_circuits.append(circuit)

    return new_circuits
