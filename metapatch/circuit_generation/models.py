"""Pydantic models to make parsing more precise."""

from collections.abc import Generator
import keyword
from enum import Enum
from typing import Any, Annotated
from pydantic import BaseModel, BeforeValidator, Discriminator, Tag, PrivateAttr

from .formatting import strip_latex, format_synopsis


def cleanup_description(description: str) -> str:
    """Clean up the description field for import.

    This will run as a validator.
    """
    assert isinstance(description, str), "Error: Unexpected description type."
    description = " ".join(description.splitlines())
    return strip_latex(description)


def ensure_valid_name(name: str) -> str:
    """Ensure that the parameter name does not collide with a python keyword."""
    assert isinstance(name, str), "Error: Expected name to be a string."
    if keyword.iskeyword(name) or name == "copy":
        name += "_"

    return name


def cleanup_title(title: str) -> str:
    """Clean up title."""
    assert isinstance(title, str), "Error: Expected title to be a string."
    return strip_latex(title)


class EssentialParameter(Enum):
    """The essentiality of a parameters.

    Just leaving it here for my own reference.
    """

    NOT_ESSENTIAL = 0
    TYPICAL = 1
    ESSENTIAL = 2


class DroidCircuitIOSpecSingle(BaseModel):
    """Single Input/output of a circuit."""

    _iotype: str = PrivateAttr(default="single")

    name: str
    default: str | None
    description: Annotated[str, BeforeValidator(cleanup_description)]
    ramhint: str
    short: str
    type: str
    essential: int

    @property
    def synopsis(self) -> str:
        """Format a synopsis for the docstring."""
        return format_synopsis(self.description)

    @property
    def parameter(self) -> str:
        """Generate a valid parameter name."""
        if keyword.iskeyword(self.name) or self.name == "copy":
            return self.name + "_"
        return self.name


class DroidCircuitIOSpecNumbered(BaseModel):
    """Numbered parameter."""

    _iotype: str = PrivateAttr(default="numbered")

    name: str
    default: str | None
    description: Annotated[str, BeforeValidator(cleanup_description)]
    ramhint: str
    short: str
    type: str
    essential: int
    prefix: str
    count: int
    start_at: int
    essential_count: int

    @property
    def synopsis(self) -> str:
        """Format a synopsis for the docstring."""
        return format_synopsis(self.description)

    def generate(self) -> list[DroidCircuitIOSpecSingle]:
        """Generate the individual parameter specs."""
        params: list[DroidCircuitIOSpecSingle] = []
        index = self.start_at
        for _ in range(self.count):
            name = self.prefix + str(index)
            shortname = self.short + str(index)
            essential = self.essential if index <= self.essential_count else 0
            params.append(
                DroidCircuitIOSpecSingle(
                    name=name,
                    default=None,
                    description=self.description,
                    ramhint=self.ramhint,
                    short=shortname,
                    type=self.type,
                    essential=essential,
                )
            )
            index += 1

        return params


def get_discriminator(v: Any) -> str:
    """Derive which IO type we are parsing."""
    if isinstance(v, dict):
        if "prefix" in v:
            return "numbered"
        return "single"
    raise ValueError("Unexpected data type when looking for an input/output dict.")


class DroidCircuitSpec(BaseModel):
    """Droid circuit specification class."""

    category: str
    title: Annotated[str, BeforeValidator(cleanup_title)]
    description: str
    inputs: list[
        Annotated[
            (
                Annotated[DroidCircuitIOSpecSingle, Tag("single")]
                | Annotated[DroidCircuitIOSpecNumbered, Tag("numbered")]
            ),
            Discriminator(get_discriminator),
        ],
    ]
    outputs: list[
        Annotated[
            (
                Annotated[DroidCircuitIOSpecSingle, Tag("single")]
                | Annotated[DroidCircuitIOSpecNumbered, Tag("numbered")]
            ),
            Discriminator(get_discriminator),
        ],
    ]
    presets: int
    manual: int
    ramsize: int | None

    def get_io(self) -> Generator[DroidCircuitIOSpecSingle]:
        """Get all inputs and outputs."""
        for param in self.inputs:
            if isinstance(param, DroidCircuitIOSpecSingle):
                yield param
            else:
                for numbered in param.generate():
                    yield numbered

        for param in self.outputs:
            if isinstance(param, DroidCircuitIOSpecSingle):
                yield param
            else:
                for numbered in param.generate():
                    yield numbered


class DroidCircuitControllerSpec(BaseModel):
    """Controller specification."""

    ramsize: int


class DroidCircuitSpecRoot(BaseModel):

    firmware_version: str
    jacktable_initial_size: int
    available_memory: dict[str, int]
    circuits: dict[str, DroidCircuitSpec]
    manual_references: dict[str, int]
    controllers: dict[str, DroidCircuitControllerSpec]

    def get_categories(self) -> dict[str, dict[str, DroidCircuitSpec]]:
        """Group circuits by category."""
        circuit_categories: dict[str, dict[str, DroidCircuitSpec]] = {}
        for name, circuit in self.circuits.items():
            category = circuit_categories.setdefault(circuit.category, {})
            category[name] = circuit

        return circuit_categories
