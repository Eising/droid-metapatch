"""Circuit base class."""

from typing import (
    Literal,
    cast,
)
from pydantic import BaseModel
from metapatch.base import Circuit


class DroidCircuit(BaseModel):
    """@private Droid Circuit parent class."""

    """@private"""
    comment: str | None = None

    def to_circuit(self, section: str | None = None) -> Circuit:
        """Convert to circuit.

        @private
        """
        parameters: dict[str, str] = {
            key: str(value)
            for key, value in self.model_dump(
                exclude_defaults=True,
                exclude_unset=True,
                exclude_none=True,
                exclude={"comment"},
                by_alias=True,
            ).items()
        }
        circuit_name = type(self).__name__.lower()
        return Circuit(name=circuit_name, parameters=parameters, comment=self.comment, section=section)


def transform(
    circuits: list[DroidCircuit],
    *,
    select: str | None = None,
    select_at: str | None = None,
    prepend: str | None = None,
    append: str | None = None,
    new_input: str | None = None,
    new_output: str | None = None,
    gate: str | None = None,
    replace: list[tuple[str, str]] | None = None,
    ignore: list[str] | None = None,
) -> list[DroidCircuit]:
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
    circuit: DroidCircuit, append: str | None, prepend: str | None, ignore: list[str]
) -> DroidCircuit:
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


def find_cables(circuit: DroidCircuit) -> dict[str, str]:
    """Return a dictionary of the input/outputs that contain virtual cables."""
    cables: dict[str, str] = {}
    circuit_dict = circuit.model_dump(by_alias=False)
    for field, value in circuit_dict.items():
        if str(value).startswith("_"):
            cables[field] = value

    return cables


def add_select(
    circuit: DroidCircuit, select: str, select_at: str | None = None
) -> DroidCircuit:
    """Add select."""
    if not "select" in type(circuit).model_fields:
        return circuit
    circuit_dict = circuit.model_dump(exclude_none=True, by_alias=False)
    select_val = circuit_dict.get("select")
    to_update: dict[str, str] = {}
    if not select_val:
        to_update["select"] = select

    if select_val and select_val != select:
        # Circuit has a different existing select value.
        return circuit

    if select_at:
        to_update["selectat"] = select_at

    return circuit.model_copy(update=to_update)


def change_jack(
    circuits: list[DroidCircuit],
    new_jack: str,
    jacktype: Literal["input", "output", "gate"],
    ignore: list[str],
) -> list[DroidCircuit]:
    """Change jack on a list of circuits.

    There can only be a single distinct value in all of the circuits.
    """
    jackmap = {"input": "I", "output": "O", "gate": "G"}
    start = jackmap[jacktype]
    jacks: set[str] = set()
    new_circuits: list[DroidCircuit] = []
    for circuit in circuits:
        circuit_fields = circuit.model_dump()
        to_update: dict[str, str] = {}
        for key, value in circuit_fields.items():
            value = cast(str, value)
            if not value or value in ignore:
                continue
            if value.startswith(start):
                jacks.add(value)
                if len(jacks) > 1:
                    raise ValueError(
                        f"Cannot run {jacktype} transformation, more than one unique {jacktype} found."
                    )
                to_update[key] = new_jack
        new_circuits.append(circuit.model_copy(update=to_update))

    return new_circuits


def translate(
    circuits: list[DroidCircuit], translations: list[tuple[str, str]]
) -> list[DroidCircuit]:
    """Translate parameters in multiple circuits.

    This allows renaming a controller to another controller.
    """
    new_circuits: list[DroidCircuit] = []
    d_translation = dict(translations)
    for circuit in circuits:
        c_dict = circuit.model_dump(exclude_unset=True, by_alias=False, exclude_none=True)
        update = {key: d_translation[value]for key, value in c_dict.items() if value in d_translation}

        new_circuits.append(circuit.model_copy(update=update))
    return new_circuits
