"""Base classes."""

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
