"""Circuit types."""

from typing import TypedDict


class DroidCircuitMeta(TypedDict):
    """Typed dictionary for circuit metadata."""

    parameter_type: str
    ramsize: int


# Maps to string
def type_any(ramsize: int = 0) -> DroidCircuitMeta:
    """Return circuit type 'any'."""
    return {"parameter_type": "any", "ramsize": ramsize}


# Maps to float
def type_bipolar(ramsize: int = 0) -> DroidCircuitMeta:
    """Return circuit type 'bipolar'."""
    return {"parameter_type": "bipolar", "ramsize": ramsize}


# Maps to float
def type_cv(ramsize: int = 0) -> DroidCircuitMeta:
    """Return circuit type 'cv'."""
    return {"parameter_type": "cv", "ramsize": ramsize}


# Maps to float
def type_fraction(ramsize: int = 0) -> DroidCircuitMeta:
    """Return circuit type 'fraction'."""
    return {"parameter_type": "fraction", "ramsize": ramsize}


# Maps to float
def type_gate(ramsize: int = 0) -> DroidCircuitMeta:
    """Return circuit type 'gate'."""
    return {"parameter_type": "gate", "ramsize": ramsize}


# Maps to integer
def type_integer(ramsize: int = 0) -> DroidCircuitMeta:
    """Return circuit type 'integer'."""
    return {"parameter_type": "integer", "ramsize": ramsize}


# Maps to float
def type_stepped(ramsize: int = 0) -> DroidCircuitMeta:
    """Return circuit type 'stepped'."""
    return {"parameter_type": "stepped", "ramsize": ramsize}


# Maps to float
def type_trigger(ramsize: int = 0) -> DroidCircuitMeta:
    """Return circuit type 'trigger'."""
    return {"parameter_type": "trigger", "ramsize": ramsize}


# Maps to float
def type_voltperoctave(ramsize: int = 0) -> DroidCircuitMeta:
    """Return circuit type 'voltperoctave'."""
    return {"parameter_type": "voltperoctave", "ramsize": ramsize}
