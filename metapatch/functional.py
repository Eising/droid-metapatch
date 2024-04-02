"""Functional implementation."""

from dataclasses import dataclass, field
from typing import Callable, List, Mapping, Optional, Tuple, TypeVar, Union

from .metapatch import Circuit, Controller, Option, BoolOption, EnumOption, NumberOption

PatchVars = Union[str, int, bool]

PatchFun = Callable[..., None]

FC = TypeVar("FC", bound=PatchFun)


@dataclass
class Section:
    """Section of options."""

    name: str
    options: List[Option] = field(default_factory=list)


@dataclass
class PatchContext:
    """Context class."""

    title: str
    description: str
    generator: Optional[Callable[..., None]] = None
    circuits: List[Circuit] = field(default_factory=list)
    controllers: List[Controller] = field(default_factory=list)
    presets: Mapping[str, Mapping[str, PatchVars]] = field(default_factory=dict)
    sections: List[Section] = field(default_factory=list)

    @classmethod
    def run(cls) -> None:
        """Run patch generator."""

    def add_circuit(
        self, name: str, comment: Optional[str] = None, **params: str
    ) -> None:
        """Add a circuit."""
        self.circuits.append(Circuit(name, comment=comment, parameters=params))

    def add_controller(self, controller_type: str, position: int) -> None:
        """Add controller."""
        self.controllers.append(Controller(controller_type, position))

    def generate(self) -> None:
        """Generate patch."""
        if not self.generator:
            raise RuntimeError("No generator method registered!")
        if not self.circuits and not self.controllers:
            self.generator(self)

    def __str__(self) -> str:
        """Generate patch as string."""
        self.generate()
        sorted_controllers = sorted(self.controllers, key=lambda x: x.position)
        controllers = "\n".join([str(controller) for controller in sorted_controllers])

        circuits = "\n".join([str(circuit) for circuit in self.circuits])
        return f"{controllers}\n\n{circuits}"


def patch_generator(
    title: str, description: str
) -> Callable[[Callable[..., None]], PatchContext]:
    """Generate patch generator class as generator."""

    def wrapper(fun: Callable[..., None]) -> PatchContext:
        """Wrap function."""
        return PatchContext(title, description, generator=fun)

    return wrapper


def option(
    description: str,
    section: str = "Options",
    *,
    choices: Optional[List[Tuple[str, str]]] = None,
    minimum: Optional[int] = None,
    maximum: Optional[int] = None,
) -> Callable:
    """Define a configurable variable.

    Args:
        description: Description of the variable
        section: The name of the configuration pane where this option should be shown.

    A number of different option types can be generated. Without any further
    options, the option will be a boolean true/false.

    Number Option:
        minimum: integer
        maximum: integer

    Enumeration Option:
        choices: List of tuples. The Tuples define (value, description)

    Note that all options will be instantiated as strings in your patch
    generator.
    """
