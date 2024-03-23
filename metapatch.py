"""Class based patch generator interface."""

import argparse
import json
import sys

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, List, Mapping, Optional, Tuple, Type, Union


def _split_params(params: List[str]) -> Dict[str, Union[str, int, bool]]:
    """Split input parameters."""
    patch_params: Dict[str, Union[str, int, bool]] = {}
    for param in params:
        if "=" not in param:
            raise ValueError("Parameters must be input as key=value")
        key, value = param.split("=")
        if key in patch_params:
            raise ValueError(f"Duplicate key {key} found.")
        # I think this is how booleans are represented
        if value in ("true", "false"):
            bool_value = True if value == "true" else False
            patch_params[key] = bool_value
        elif value.isnumeric():
            patch_params[key] = int(value)

        else:
            patch_params[key] = str(value)

    return patch_params


@dataclass
class Option:
    """Base option class."""

    title: str
    section: str

    def asdict(self, varname: str) -> Dict[str, Any]:
        """Return as dictionary."""
        return {
            "name": varname,
            "title": self.title,
        }


@dataclass
class EnumOption(Option):
    """Enumeration option."""

    enum: List[Tuple[str, str]]

    def asdict(self, varname: str) -> Dict[str, Any]:
        """Return as dictionary."""
        base = super().asdict(varname)
        base["enum"] = self.enum
        return base


@dataclass
class NumberOption(Option):
    """NUmber option."""

    number: Tuple[int, int]

    def asdict(self, varname: str) -> Dict[str, Any]:
        """Return as dictionary."""
        base = super().asdict(varname)
        base["number"] = self.number
        return base


def option(
    description: str,
    section: str = "Options",
    *,
    choices: Optional[List[Tuple[str, str]]] = None,
    minimum: Optional[int] = None,
    maximum: Optional[int] = None,
) -> Option:
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

    """
    if choices:
        return EnumOption(description, section, choices)
    elif minimum and maximum:
        return NumberOption(description, section, (minimum, maximum))
    else:
        return Option(description, section)


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


class PatchMeta:
    """Base patch meta class.

    Subclass this and define your configuration options.
    """

    title: str
    description: str

    def __init__(self) -> None:
        """Instantiate patch."""
        sections: Dict[str, Dict[str, Option]] = {}
        presets: List[Dict[str, Any]] = []

        for param, opt in type(self).__dict__.items():
            if isinstance(opt, Option):
                if opt.section not in sections:
                    sections[opt.section] = {}
                sections[opt.section][param] = opt
            elif isinstance(opt, Preset):
                presets.append(opt.asdict(param))

        # Convert section dictionary into a list of dictionaries
        self.sections = []
        for section_name, opts in sections.items():
            subsection = {"title": section_name, "options": []}
            for var, opt in opts.items():
                subsection["options"].append(opt.asdict(var))

            self.sections.append(subsection)

        self.presets = presets

    @property
    def vars(self) -> List[str]:
        """Return a list of all the expected variables."""
        opts: List[str] = []
        for section in self.sections:
            opts.extend([opt["name"] for opt in section["options"]])
        return opts

    @classmethod
    def get_presets(cls) -> List[Tuple[str, str]]:
        """Return available presets."""
        patch = cls()
        return [(preset["name"], preset["title"]) for preset in patch.presets]

    @classmethod
    def from_preset(cls, name: str) -> Dict[str, Any]:
        """Extract parameters from preset."""
        patch = cls()
        matching_preset = [preset for preset in patch.presets if preset["name"] == name]
        if not matching_preset:
            raise ValueError(f"Could not find a preset named {name}.")
        return next(iter(matching_preset))["parameters"]

    @classmethod
    def get_vars(cls) -> List[str]:
        """Get expected variables as class method."""
        patch = cls()
        return patch.vars

    @classmethod
    def synopsis(cls) -> Dict[str, Any]:
        """Print synospsis as JSON."""
        meta = cls()
        synopsis = {
            "title": cls.title,
            "description": cls.description,
            "sections": meta.sections,
            "presets": meta.presets,
        }
        return {"synopsis": synopsis}

    @classmethod
    def run_cli(cls) -> Dict[str, Any]:
        """Process parameters given via command line arguments."""
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
        presets = cls.get_presets()
        presets_str = "\n".join(
            [
                f"{presetname:<12} {presettitle:<12}"
                for presetname, presettitle in presets
            ]
        )
        epilog = f"Available Presets:\n{presets_str}\n\n"
        params = "Parameters:\n"
        for key, value in cls.__dict__.items():
            if not isinstance(value, Option):
                continue
            if isinstance(value, EnumOption):
                usage = "|".join(choice[0] for choice in value.enum)
            elif isinstance(value, NumberOption):
                usage = f"{value.number[0]}..{value.number[1]}"
            else:
                usage = "True/False"

            keyusage = f"{key}={usage}"

            params += f"{'':<4}{keyusage:<16} {'-':^4} {value.title:<16}\n"
        epilog += params
        parser.epilog = epilog

        args = parser.parse_args()
        if args.synopsis:
            return cls.synopsis()
        if args.preset:
            return cls.from_preset(args.preset)

        patch_parameters: List[str] = args.parameters
        if not patch_parameters:
            parser.print_help()
            sys.exit()
        parameters = _split_params(patch_parameters)
        for var in cls.get_vars():
            if var not in parameters:
                raise ValueError(
                    f"Cannot extract patch parameters: Missing parameter {var}"
                )

        return parameters


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

    type: str
    position: int

    def __str__(self) -> str:
        """Generate controller string."""
        return f"[{self.type}]"


class PatchGenerator(ABC):
    """Droid Patch generator class.

    You must subclass this class and define your patch logic.

    All given parameters are available in the `self.parameters` instance
    dictionary.
    """

    def __init__(self, parameters: Dict[str, Any]) -> None:
        """Initialize patch."""
        self.circuits: List[Circuit] = []
        self.parameters = parameters
        self.controllers: List[Controller] = []

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
        sorted_controllers = sorted(self.controllers, key=lambda x: x.position)
        controllers = "\n".join([str(controller) for controller in sorted_controllers])

        circuits = "\n".join([str(circuit) for circuit in self.circuits])
        return f"{controllers}\n\n{circuits}"

    @abstractmethod
    def generate(self) -> None:
        """Generate patch."""

    @classmethod
    def setup(cls, patch: Type[PatchMeta]) -> None:
        """Set up patch generator."""
        params = patch.run_cli()
        if "synopsis" in params:
            print(json.dumps(params["synopsis"], indent=2))
            return

        generator = cls(params)
        generator.generate()
        print(str(generator))
