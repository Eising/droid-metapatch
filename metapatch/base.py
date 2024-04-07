"""Base classes."""

import re
from dataclasses import dataclass, field
from typing import Optional, Mapping

from .utils import format_comment, write_patch_section


@dataclass
class Circuit:
    """Circuit container class."""

    name: str
    parameters: Mapping[str, str] = field(default_factory=dict)
    comment: Optional[str] = None
    section: Optional[str] = None

    def __str__(self) -> str:
        """Output circuit as patch."""
        indent = 4 * " "
        comment = ""
        if self.comment:
            comment = format_comment(self.comment) + "\n"
        params = "\n".join(
            [f"{indent}{key} = {value}" for key, value in self.parameters.items()]
        )
        patch = f"{comment}[{self.name}]\n{params}\n"
        return patch


@dataclass
class Controller:
    """Droid controller container class."""

    type: str
    position: int

    def __str__(self) -> str:
        """Generate controller string."""
        return f"[{self.type}]"


@dataclass
class Section:
    """Section class."""

    name: str
    comment: Optional[str] = None

    def __str__(self) -> str:
        """Return section string."""
        output = ""
        if self.comment:
            output += format_comment(self.comment)

        output += write_patch_section(self.name)
        return output


@dataclass
class Label:
    """Label class."""

    heading: str
    item: str
    short_label: str
    long_label: Optional[str] = None

    def __str__(self) -> str:
        """Generate label.

        Does not include the heading.
        """
        label = f"#  {self.item}: [{self.short_label}]"
        if self.long_label:
            label += f" {self.long_label}"

        label += "\n"
        return label

    @classmethod
    def from_item(
        cls, item: str, short_label: str, long_label: Optional[str] = None
    ) -> "Label":
        """Construct from item."""
        if item.startswith("I"):
            # Input label
            section = "inputs"
        elif item.startswith("O"):
            section = "outputs"
        elif res := re.match(r"([A-Z])(\d+)\.(\d+)", item):
            module_num = res.group(2)
            controller_type = res.group(1)
            if controller_type == "G":
                if "." in item:
                    section = f"gates on module {module_num}"
                else:
                    section = "gates on x7"
            else:
                section = f"controller {module_num}"

        return cls(section, item, short_label, long_label)
