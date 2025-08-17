"""Base classes."""

import re
from pydantic import BaseModel, Field
from collections.abc import Mapping

from .utils import format_comment, write_patch_section


class Circuit(BaseModel):
    """Circuit container class."""

    name: str
    parameters: Mapping[str, str] = Field(default_factory=dict)
    comment: str | None = None
    section: str | None = None

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


class Controller(BaseModel):
    """Droid controller container class."""

    type: str
    position: int

    def __str__(self) -> str:
        """Generate controller string."""
        return f"[{self.type}]"


class Section(BaseModel):
    """Section class.

    TODO: I don't seem to call this... Is it needed?
    """

    name: str
    comment: str | None = None

    def __str__(self) -> str:
        """Return section string."""
        output = ""
        if self.comment:
            output += format_comment(self.comment)

        output += write_patch_section(self.name)
        return output


class Label(BaseModel):
    """Label class."""

    heading: str
    item: str
    short_label: str
    long_label: str | None = None

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
        cls, item: str, short_label: str, long_label: str | None = None
    ) -> "Label":
        """Construct from item."""
        section: str | None = None
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

        if not section:
            raise RuntimeError("Unable to resolve section.")
        return cls(heading=section, item=item, short_label=short_label, long_label=long_label)
