"""Class based patch generator interface."""

import argparse
import json
import textwrap

from abc import abstractmethod
from typing import (
    Any,
    Dict,
    List,
    Mapping,
    Optional,
    Tuple,
)

from .base import Circuit, Controller, Section
from .options import Option, BoolOption, NumberOption, EnumOption, Preset
from .utils import write_patch_section

DEFAULT_SECTION_NAME = "Generated Patch"


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


class MetaMetaPatch(type):
    """Metaclass for metapatches."""

    title: str
    description: str

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


class PatchGenerator(metaclass=MetaMetaPatch):
    """Patch Generator."""

    title: str
    description: str
    __patchvars__: List[str]

    def __new__(cls, **_: Any) -> "PatchGenerator":
        """Build class."""
        cls.__patchvars__ = []
        for param, opt in cls.__dict__.items():
            if hasattr(opt, "_ispatchoption"):
                cls.__patchvars__.append(param)

        return super().__new__(cls)

    def __init__(self, **kwargs: str) -> None:
        """Initialize class."""
        # Set all options not defined in the input to their defaults.
        for opt in self.__patchvars__:
            if opt not in kwargs:
                var = getattr(self, opt)
                assert issubclass(var, (BoolOption, EnumOption, NumberOption))
                setattr(self, opt, var.from_default().get_value())

        for key, value in kwargs.items():
            if key in self.__patchvars__:
                var = getattr(self, key)
                assert issubclass(var, (BoolOption, EnumOption, NumberOption))
                setattr(self, key, var(value).get_value())
            else:
                raise ValueError(f"Unknown parameter {key}")

        self.circuits: List[Circuit] = []
        self.controllers: List[Controller] = []
        self.labels: Dict[str, Tuple[str, str]] = {}
        self._section: Optional[str] = None
        # This dictionary stores comments for sections.
        self.sections: Dict[str, Optional[str]] = {}

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
            [f"{preset['name']:<12} {preset['title']:<12}" for preset in presets]
        )
        epilog = f"Available Presets:\n{presets_str}\n\n"
        params = "parameters (defaults are marked with *):\n\n"
        all_param_help = {}
        for key, value in cls.__dict__.items():
            if not hasattr(value, "_ispatchoption"):
                continue
            if issubclass(value, (BoolOption, EnumOption, NumberOption)):
                all_param_help[value.title] = value.help(key)

        longest = max(
            [
                len(varname[0])
                for param in list(all_param_help.values())
                for varname in param
            ]
        )
        for title, opthelp in all_param_help.items():
            params += textwrap.indent(title, "  ") + "\n"
            for opt, descr in opthelp:
                params += textwrap.indent(f"{opt:<{longest}}  {descr}", "    ")
                params += "\n"

            params += "\n"

        epilog += params
        parser.epilog = epilog

        args = parser.parse_args()

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
        self.circuits.append(
            Circuit(name=name, parameters=params, comment=comment, section=self.section)
        )

    def add_controller(self, type: str, position: int) -> None:
        """Add a controller at a given position.

        Args:
            type: Type of controller, e.g. B32
            position: controller position, e.g. 1
        """
        self.controllers.append(Controller(type, position))

    def set_labels(self, labels: Mapping[str, Tuple[str, str]]) -> None:
        """Set labels of jacks."""
        self.labels = {**self.labels, **labels}

    @property
    def section(self) -> Optional[str]:
        """Get section."""
        return self._section

    @section.setter
    def section(self, name: str) -> None:
        """Set the section."""
        if not isinstance(name, str):
            raise ValueError("Section name must be a string.")
        self._section = name

    def add_section(self, name: str, comment: Optional[str] = None) -> None:
        """Add a section with an optional comment."""
        if name in self.sections:
            return
        self.sections[name] = comment
        self._section = name

    @property
    def _has_sections(self) -> bool:
        """Check if sections are defined."""
        sections = [circuit.section for circuit in self.circuits]
        return any(sections)

    def _get_circuits_as_strings(self) -> str:
        """Get circuits as a string."""
        circuits = []
        current_section: Optional[str] = None

        if self._has_sections:
            if not self.circuits[0].section:
                # If circuits were added before a section was defined, then we
                # use a default name for this section.
                current_section = DEFAULT_SECTION_NAME
            else:
                current_section = self.circuits[0].section

            comment = self.sections.get(current_section)
            circuits.append(write_patch_section(current_section, comment))

        for circuit in self.circuits:
            if (
                current_section
                and circuit.section is not None
                and circuit.section != current_section
            ):
                comment = self.sections.get(circuit.section)
                circuits.append(write_patch_section(circuit.section, comment))
                current_section = circuit.section
            circuits.append(str(circuit))

        return "\n".join(circuits)

    def __str__(self) -> str:
        """Output patch as string."""
        self._generate()

        sorted_controllers = sorted(self.controllers, key=lambda x: x.position)
        controllers = "\n".join([str(controller) for controller in sorted_controllers])
        circuits = self._get_circuits_as_strings()

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
