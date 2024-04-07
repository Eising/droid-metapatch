"""Class based patch generator interface."""

import argparse
import json
import textwrap

from abc import abstractmethod
from itertools import groupby
from typing import (
    Any,
    Dict,
    List,
    Mapping,
    Optional,
)

from .base import Circuit, Controller, Label
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
        return synopsis

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
        self.labels: List[Label] = []
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

        if all_param_help:
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

    def add_label(
        self, item: str, short_label: str, long_label: Optional[str] = None
    ) -> None:
        """Add a label.

        Args:
            item: string of the thing you want to label, e.g. O1 or G1.2
            short_label: The short label
            long_label: Optional longer label
        """
        self.labels.append(Label.from_item(item, short_label, long_label))

    def _generate_labels(self) -> str:
        """Generate label strings."""
        sorted_labels = {}
        for label in self.labels:
            if label.heading not in sorted_labels:
                sorted_labels[label.heading] = []
            sorted_labels[label.heading].append(label)

        labels = ""
        for heading, list_labels in sorted_labels.items():
            labels += f"# {heading.upper()}:\n"
            for label in list_labels:
                labels += str(label)
            labels += "\n"

        return labels

    def add_controller(self, type: str, position: int) -> None:
        """Add a controller at a given position.

        Args:
            type: Type of controller, e.g. B32
            position: controller position, e.g. 1
        """
        self.controllers.append(Controller(type, position))

    @property
    def section(self) -> Optional[str]:
        """Get section."""
        return self._section

    @section.setter
    def section(self, name: str) -> None:
        """Set the section."""
        if not isinstance(name, str):
            raise ValueError("Section name must be a string.")
        if name not in self.sections:
            self.sections[name] = None
        self._section = name

    def add_section(self, name: str, comment: Optional[str] = None) -> None:
        """Add a section with an optional comment."""
        self._section = name
        if name not in self.sections or self.sections.get(name) != comment:
            self.sections[name] = comment

    @property
    def _has_sections(self) -> bool:
        """Check if sections are defined."""
        sections = [circuit.section for circuit in self.circuits]
        return any(sections)

    def _get_circuits_as_strings(self) -> str:
        """Get circuits as a string.

        This is for circuits when there are no sections at all.
        """
        circuits = [str(circuit) for circuit in self.circuits]
        return "\n".join(circuits)

    def _get_circuits_with_sections(self) -> str:
        """Get circuits as a string with sections."""
        circuits = []

        groups = {}
        for section, grouped_circuits in groupby(self.circuits, lambda x: x.section):
            if section is None:
                section_name = DEFAULT_SECTION_NAME
            else:
                section_name = section
            if section_name not in groups:
                groups[section_name] = []
            groups[section_name].extend(grouped_circuits)

        for section_name, grouped_circuits in groups.items():
            if section_name == DEFAULT_SECTION_NAME:
                circuits.append(write_patch_section(DEFAULT_SECTION_NAME))
            else:
                comment = self.sections.get(section_name)
                circuits.append(write_patch_section(section_name, comment))

            for circuit in grouped_circuits:
                circuits.append(str(circuit))

        return "\n".join(circuits)

    def __str__(self) -> str:
        """Output patch as string."""
        self._generate()

        labels = self._generate_labels()
        sorted_controllers = sorted(self.controllers, key=lambda x: x.position)
        controllers = "\n".join([str(controller) for controller in sorted_controllers])
        if self._has_sections:
            circuits = self._get_circuits_with_sections()
        else:
            circuits = self._get_circuits_as_strings()

        return f"{labels}{controllers}\n\n{circuits}"

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
