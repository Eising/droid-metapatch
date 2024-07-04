"""Circuit base class."""

from copy import copy
from dataclasses import dataclass, is_dataclass, fields, asdict
from typing import (
    ClassVar,
    Dict,
    Literal,
    List,
    Optional,
    Tuple,
    TypeVar,
)
from metapatch.base import Circuit


@dataclass
class DroidCircuit:
    """@private Droid Circuit parent class."""

    """@private"""
    comment: Optional[str] = None
    __ramsize__: ClassVar[int] = 0

    def to_circuit(self) -> Circuit:
        """Convert to circuit.

        @private
        """
        return dataclass_to_circuit(self)


T = TypeVar("T", bound=DroidCircuit)


def dataclass_to_circuit(
    circuit: DroidCircuit, section: Optional[str] = None, comment: Optional[str] = None
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


def transform(
    circuits: List[T],
    *,
    select: Optional[str] = None,
    select_at: Optional[str] = None,
    prepend: Optional[str] = None,
    append: Optional[str] = None,
    new_input: Optional[str] = None,
    new_output: Optional[str] = None,
    gate: Optional[str] = None,
    replace: Optional[List[Tuple[str, str]]] = None,
    ignore: Optional[List[str]] = None,
) -> List[T]:
    """Transform a list of circuits.

    Args:
        select: Add a select parameter to all circuits that support it and have
            no current select.
        select_at: Add a selectat parameter to all circuits that support it.
        prepend: Add a word to the start of all virtual cable names.
        append: Add a word to the end of all virtual cable names.
        new_input: If an input is found, change it to the value of input
        output: If an output is found, change it to value of output (e.g., O2)
        gate: If a gate is found, change it to the value of the gate.
        replace: List of (from, to). Does a search and replace for an arbitrary value.
           Can be used to e.g., replace one pot with another.
        ignore: Ignore any of the supplied names when doing a rewriting operation.

    """
    if not ignore:
        ignore = []
    if select:
        circuits = [add_select(circuit, select, select_at) for circuit in circuits]

    circuits = [rename_cables(circuit, append, prepend, ignore) for circuit in circuits]
    if new_input:
        circuits = change_jack(circuits, new_input, "input", ignore)
    if new_output:
        circuits = change_jack(circuits, new_output, "output", ignore)
    if gate:
        circuits = change_jack(circuits, gate, "gate", ignore)

    if replace:
        circuits = translate(circuits, replace)

    return circuits


def rename_cables(
    circuit: T, append: Optional[str], prepend: Optional[str], ignore: List[str]
) -> T:
    """Rename cables."""
    if not append and not prepend:
        return circuit

    cables = find_cables(circuit)
    if not cables:
        return circuit

    for fieldname, cablename in cables.items():
        if cablename in ignore:
            continue
        if not prepend:
            prependname = ""
        elif prepend.startswith("_"):
            prependname = prepend
        else:
            prependname = "_" + prepend

        newname = f"{prependname}{cablename}{append or ''}"
        setattr(circuit, fieldname, newname)

    return circuit


def find_cables(circuit: DroidCircuit) -> Dict[str, str]:
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
    circuits: List[T],
    new_jack: str,
    jacktype: Literal["input", "output", "gate"],
    ignore: List[str],
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
        new_circuit = copy(circuit)
        for key, value in circuit_fields.items():
            if not value or value in ignore:
                continue
            if value.startswith(start):
                jacks.add(value)
                if len(jacks) > 1:
                    raise ValueError(
                        f"Cannot run {jacktype} transformation, "
                        f"more than one unique {jacktype} found."
                    )
                setattr(new_circuit, key, new_jack)
        new_circuits.append(new_circuit)

    return new_circuits


def translate(circuits: List[T], translations: List[Tuple[str, str]]) -> List[T]:
    """Translate parameters in multiple circuits.

    This allows renaming a controller to another controller.
    """
    new_circuits = []
    d_translation = dict(translations)
    for circuit in circuits:
        circuit_fields = asdict(circuit)
        c_copy = copy(circuit)
        for key, value in circuit_fields.items():
            if value and value in d_translation:
                setattr(c_copy, key, d_translation[value])
        new_circuits.append(c_copy)
    return new_circuits
