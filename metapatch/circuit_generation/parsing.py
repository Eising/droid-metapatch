"""DROID circuits JSON parsing."""

from pathlib import Path

from .models import DroidCircuitSpecRoot


def load_circuits(filename: Path) -> DroidCircuitSpecRoot:
    """Load circuits from file."""
    assert filename.exists(), "Error: Filename does not exist!"
    with open(filename, "r", encoding="utf-8") as f:
        circuit_spec = DroidCircuitSpecRoot.model_validate_json(f.read())

    return circuit_spec
