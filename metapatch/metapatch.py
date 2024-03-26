"""Class based patch generator interface."""

import argparse
import json

from abc import abstractmethod
from dataclasses import dataclass, field
from typing import (
    Any,
    Dict,
    Generic,
    List,
    Mapping,
    Optional,
    Tuple,
    TypeVar,
    Union,
)


def _split_params(params: List[str]) -> Dict[str, str]:
    """Split input parameters."""
    patch_params: Dict[str, str] = {}
    for param in params:
        if "=" not in param:
            raise ValueError("Parameters must be input as key=value")
        key, value = param.split("=")
        if key in patch_params:
            raise ValueError(f"Duplicate key {key} found.")
        # We convert everything to strings.
        patch_params[key] = str(value)

    return patch_params


T = TypeVar("T")


class Option(Generic[T]):
    """Base option class."""

    title: str
    section: str
    _ispatchoption = True

    def __init__(self, value: Union[str, int, bool]) -> None:
        """Initialize option with value."""
        self.value: Union[str, int, bool] = value

    def __str__(self) -> str:
        """Return string."""
        return str(self.value)

    def __eq__(self, lvalue: Any) -> bool:
        """Compare like a string."""
        return self.value == lvalue

    @classmethod
    def asdict(cls, varname: str) -> Dict[str, Any]:
        """Return as dictionary."""
        return {
            "name": varname,
            "title": cls.title,
        }


class BoolOption(Option):
    """Boolean option."""

    def get_value(self) -> bool:
        """Return value."""
        return bool(self.value)


class EnumOption(Option):
    """Enumeration option."""

    enum: List[Tuple[str, str]]

    def __init__(self, value: Union[str, int, bool]) -> None:
        """Validate input."""
        choices = [choice[0] for choice in self.enum]
        if str(value) not in choices:
            raise ValueError(f"Unsupported choice: {value}")
        super().__init__(value)

    def get_value(self) -> str:
        """Return value."""
        return str(self.value)

    @classmethod
    def asdict(cls, varname: str) -> Dict[str, Any]:
        """Return as dictionary."""
        base = super().asdict(varname)
        base["enum"] = cls.enum
        return base


class NumberOption(Option):
    """NUmber option."""

    number: Tuple[int, int]

    def __init__(self, value: Union[str, int, bool]) -> None:
        """Validate input."""
        if isinstance(value, str):
            if not value.isdecimal():
                raise ValueError(f"Expected a decimal number, but got {value}.")

        super().__init__(value)

    def get_value(self) -> int:
        """Return value."""
        return int(self.value)

    @classmethod
    def asdict(cls, varname: str) -> Dict[str, Any]:
        """Return as dictionary."""
        base = super().asdict(varname)
        base["number"] = cls.number
        return base


def option(
    description: str,
    section: str = "Options",
    *,
    choices: Optional[List[Tuple[T, T]]] = None,
    minimum: Optional[T] = None,
    maximum: Optional[T] = None,
) -> T:
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
    params: Dict[str, Any] = {
        "title": description,
        "section": section,
    }
    bases: Tuple[type, ...]

    if choices:
        # Slightly hacky. We construct a dynamic child class that sets the given
        # title and section. This allows us to use it as a string.
        params["enum"] = choices
        bases = (EnumOption, Option)
        return type("LocalEnumOption", bases, params)  # type: ignore
    elif minimum and maximum:
        params["number"] = (minimum, maximum)
        bases = (NumberOption, Option)

        return type("LocalNumberOption", bases, params)  # type: ignore
    else:
        bases = (BoolOption, Option)
        return type("LocalBoolOption", bases, params)  # type: ignore


@dataclass
class Preset:
    """Preset class."""

    title: str
    parameters: Dict[str, Any]

    def asdict(self, name: str) -> Dict[str, Any]:
        """Construct preset dictionary."""
        return {"name": name, "title": self.title, "parameters": self.parameters}


def preset(title: str, parameters: Dict[str, Any]) -> Preset:
    """Define a preset.

    Args:
        title: The name of the preset.
        parameter: A dictionary containing parameter to value mappings.
    """
    return Preset(title, parameters)


class MetaMetaPatch(type):
    """Metaclass for metapatches."""

    title: str
    description: str

    def __new__(
        mcs, name: str, bases: Tuple[type, ...], params: Dict[str, Any], **kwargs: Any
    ) -> "MetaMetaPatch":
        """Construct metaclass."""
        if "__annotations__" not in params:
            params["__annotations__"] = {}
        for key, value in params.items():
            if hasattr(value, "_ispatchoption"):
                if issubclass(value, BoolOption):
                    params["__annotations__"][key] = bool
                elif issubclass(value, EnumOption):
                    params["__annotations__"][key] = str
                elif issubclass(value, NumberOption):
                    params["__annotations__"][key] = int
                else:
                    raise ValueError(f"Unknown option type: {value!r}")

        return super().__new__(mcs, name, bases, params)

    @property
    def synopsis(cls) -> Dict[str, Any]:
        """Get synopsis."""
        sections: Dict[str, Dict[str, Option]] = {}
        presets: List[Dict[str, Any]] = []
        for name, opt in cls.__dict__.items():
            if hasattr(opt, "_ispatchoption"):
                if opt.section not in sections:
                    sections[opt.section] = {}
                sections[opt.section][name] = opt
            elif isinstance(opt, Preset):
                presets.append(opt.asdict(name))

        section_list: List[Dict[str, Any]] = []
        for section_name, options in sections.items():
            subsection: Dict[str, Any] = {"title": section_name, "options": []}
            for option_name, option in options.items():
                subsection["options"].append(option.asdict(option_name))
            section_list.append(subsection)

        synopsis = {
            "title": cls.title,
            "description": cls.description,
            "sections": section_list,
            "presets": presets,
        }
        return {"synopsis": synopsis}

    @property
    def presets(cls) -> List[Dict[str, Any]]:
        """Fetch presets."""
        presets: List[Dict[str, Any]] = []
        for name, opt in cls.__dict__.items():
            if isinstance(opt, Preset):
                presets.append(opt.asdict(name))

        return presets

    @property
    def vars(cls) -> List[str]:
        """Return variables."""
        return [
            name for name, opt in cls.__dict__.items() if hasattr(opt, "_ispatchoption")
        ]


class PatchGenerator(metaclass=MetaMetaPatch):
    """Patch Generator."""

    title: str
    description: str
    __patchvars__: List[str]

    def __new__(cls, **args: Any) -> "PatchGenerator":
        """Build class."""
        cls.__patchvars__ = []
        for param, opt in cls.__dict__.items():
            if hasattr(opt, "_ispatchoption"):
                cls.__patchvars__.append(param)

        return super().__new__(cls)

    def __init__(self, **kwargs: str) -> None:
        """Initialize class."""
        for key, value in kwargs.items():
            if key in self.__patchvars__:
                var = getattr(self, key)
                assert issubclass(var, (BoolOption, EnumOption, NumberOption))
                setattr(self, key, var(value).get_value())
            else:
                raise ValueError(f"Unknown parameter {key}")

        self.circuits: List[Circuit] = []
        self.controllers: List[Controller] = []

    @classmethod
    def load_preset(cls, preset_name: str) -> "PatchGenerator":
        """Load preset."""
        preset = getattr(cls, preset_name)
        if preset:
            return cls(**preset.parameters)
        raise ValueError(f"Uknown preset: {preset_name}")

    @classmethod
    def _handle_cli(cls) -> argparse.Namespace:
        """Handle CLI."""
        parser = argparse.ArgumentParser(
            f'DROID patch generator "{cls.title}"',
            formatter_class=argparse.RawDescriptionHelpFormatter,
        )
        parser.description = cls.description
        parser.add_argument(
            "parameters",
            nargs="*",
            help="Patch generator parameters.",
            metavar="param=value ...",
        )
        parser.add_argument(
            "--synopsis",
            "-s",
            action="store_true",
            help="Output possible parameters as JSON",
        )
        parser.add_argument(
            "-p", "--preset", metavar="P", help="Use settings from preset P"
        )
        presets = cls.presets
        presets_str = "\n".join(
            [
                f"{presetname:<12} {presettitle:<12}"
                for presetname, presettitle in presets
            ]
        )
        epilog = f"Available Presets:\n{presets_str}\n\n"
        params = "Parameters:\n"
        for key, value in cls.__dict__.items():
            if not issubclass(value, Option):
                continue
            if issubclass(value, EnumOption):
                usage = "|".join(choice[0] for choice in value.enum)
            elif issubclass(value, NumberOption):
                usage = f"{value.number[0]}..{value.number[1]}"
            else:
                usage = "True/False"

            keyusage = f"{key}={usage}"

            params += f"{'':<4}{keyusage:<16} {'-':^4} {value.title:<16}\n"
        epilog += params
        parser.epilog = epilog

        args = parser.parse_args()
        if not args.parameters:
            parser.print_help()

        return args

    @classmethod
    def run(cls) -> None:
        """Process parameters given via command line arguments."""
        args = cls._handle_cli()
        if args.synopsis:
            print(json.dumps(cls.synopsis))
            return
        if args.preset:
            patch = cls.load_preset(args.preset)
            print(str(patch))
            return

        patch_parameters: List[str] = args.parameters
        parameters = _split_params(patch_parameters)
        for var in cls.vars:
            if var not in parameters:
                raise ValueError(
                    f"Cannot extract patch parameters: Missing parameter {var}"
                )

        patch = cls(**parameters)
        print(str(patch))

    def add_circuit(
        self,
        name: str,
        params: Mapping[str, str],
        comment: Optional[str] = None,
    ) -> None:
        """Add a circuit.

        Args:
            name: Circuit name, e.g. copy for a [copy] circuit
            params: Dictionary of circuit parameters.
            comment: Optional comment for the circuit.
        """
        self.circuits.append(Circuit(name=name, parameters=params, comment=comment))

    def add_controller(self, type: str, position: int) -> None:
        """Add a controller at a given position.

        Args:
            type: Type of controller, e.g. B32
            position: controller position, e.g. 1
        """
        self.controllers.append(Controller(type, position))

    def __str__(self) -> str:
        """Output patch as string."""
        self._generate()
        sorted_controllers = sorted(self.controllers, key=lambda x: x.position)
        controllers = "\n".join([str(controller) for controller in sorted_controllers])

        circuits = "\n".join([str(circuit) for circuit in self.circuits])
        return f"{controllers}\n\n{circuits}"

    def _generate(self) -> None:
        """Generate patch.

        This is an internal function that ensures that we reset the patch if needed.
        """
        if not self.circuits and not self.controllers:
            self.generate()

    @abstractmethod
    def generate(self) -> None:
        """Generate patch.

        Define this in your subclass, and use it to add circuits and controllers.
        """


@dataclass
class Circuit:
    """Circuit container class."""

    name: str
    parameters: Mapping[str, str] = field(default_factory=dict)
    comment: Optional[str] = None

    def __str__(self) -> str:
        """Output circuit as patch."""
        indent = 4 * " "
        comment = f"# {self.comment}\n" if self.comment else ""
        params = "\n".join(
            [f"{indent}{key} = {value}" for key, value in self.parameters.items()]
        )
        patch = f"[{comment}{self.name}]\n{params}\n"
        return patch


@dataclass
class Controller:
    """Droid controller container class."""

    type: str
    position: int

    def __str__(self) -> str:
        """Generate controller string."""
        return f"[{self.type}]"
