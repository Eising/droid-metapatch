"""Circuit generation."""

from pathlib import Path

from .parsing import load_circuits
from .writer import write_circuits


def generate(filename: str, output_directory: str) -> None:
    """Generate circuits."""
    collection = load_circuits(Path(filename))
    write_circuits(collection, Path(output_directory))


__all__ = ["generate"]
