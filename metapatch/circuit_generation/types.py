"""Circuit generation types."""

import keyword

from collections import defaultdict
from dataclasses import dataclass, field
from typing import Dict, List

from .formatting import strip_latex, format_synopsis


@dataclass
class Parameter:
    """Parameter."""

    name: str
    type: str
    description: str
    ramsize: int
    direction: str

    def __post_init__(self) -> None:
        """Reformat name if it collides with python."""
        if keyword.iskeyword(self.name):
            self.name += "_"
        description = " ".join(self.description.splitlines())
        self.description = strip_latex(description)

    @property
    def synopsis(self) -> str:
        """Return a synopsis for the docstring."""
        return format_synopsis(self.description)


@dataclass
class Circuit:
    """Circuit container."""

    name: str
    title: str
    category: str
    parameters: List[Parameter] = field(default_factory=list)
    ramsize: int = 0

    def __post_init__(self) -> None:
        """Remove latex from title for good meassure."""
        self.title = strip_latex(self.title)


@dataclass
class CircuitCollection:
    """Enclosing dataclass for a collection of circuits."""

    droid_version: str
    circuits: List[Circuit] = field(default_factory=list)

    def split_categories(self) -> Dict[str, "CircuitCollection"]:
        """Generate an instance of self for each of the circuit categories."""
        c_categories: Dict[str, List[Circuit]] = defaultdict(list)
        for circuit in self.circuits:
            c_categories[circuit.category].append(circuit)

        return {
            category: CircuitCollection(self.droid_version, c_circuits)
            for category, c_circuits in c_categories.items()
        }
