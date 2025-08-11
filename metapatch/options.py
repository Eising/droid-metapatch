"""Option classes."""

from dataclasses import dataclass
from typing import Any, ClassVar

# choices: list[tuple[str | int | bool, str]],
ParamType = str | int | bool
ChoiceType = list[tuple[ParamType, str]]

def _negate_description(description: str) -> str:
    """Negate a description.

    This is extremely crude, but maybe it is good enough.
    """
    # Decapitalize it.
    lower_description = f"{description[0].lower()}{description[1:]}"
    return f"Don't {lower_description}"


def generate_multi_help_statement(
    varname: str,
    choices: ChoiceType,
    default: str | int | bool,
) -> list[tuple[str, str]]:
    """Generate a help statement for a multiple choice option."""
    is_default = "* "
    is_not_default = "  "

    options: list[tuple[str, str]] = []
    for choice in choices:
        choiceval, choicedescr = choice
        if choiceval == default:
            options.append((f"{is_default}{varname}={choiceval}", choicedescr))
        else:
            options.append((f"{is_not_default}{varname}={choiceval}", choicedescr))

    return options


class Option:
    """Base option class."""

    title: ClassVar[str]
    default: ClassVar[ParamType]
    _ispatchoption: ClassVar[bool] = True

    def __init__(self, value: str | int | bool) -> None:
        """Initialize option with value."""
        self.value: str | int | bool = value

    @classmethod
    def asdict(cls, varname: str) -> dict[str, Any]:
        """Return as dictionary."""
        return {
            "name": varname,
            "title": cls.title,
        }


class BoolOption(Option):
    """Boolean option."""

    def get_value(self) -> bool:
        """Return value."""
        if isinstance(self.value, str):
            if self.value.lower() in ("false", "off", "no", "0"):
                return False
            elif self.value.lower() in ("true", "on", "yes", "1"):
                return True

        return bool(self.value)

    @classmethod
    def from_default(cls) -> "BoolOption":
        """Instantiate with default value."""
        return cls(cls.default)

    @classmethod
    def help(cls, varname: str) -> list[tuple[str, str]]:
        """Generate a help text."""
        choices: ChoiceType = [(True, cls.title), (False, _negate_description(cls.title))]
        return generate_multi_help_statement(varname, choices, cls.default)


class EnumOption(Option):
    """Enumeration option."""

    enum: ClassVar[list[tuple[str, str]]]

    def __init__(self, value: ParamType) -> None:
        """Validate input."""
        choices = [choice[0] for choice in self.enum]
        if str(value) not in choices:
            raise ValueError(f"Unsupported choice: {value}")
        super().__init__(value)

    def get_value(self) -> str:
        """Return value."""
        return str(self.value)

    @classmethod
    def from_default(cls) -> "EnumOption":
        """Instantiate with default value."""
        return cls(cls.default)

    @classmethod
    def asdict(cls, varname: str) -> dict[str, Any]:
        """Return as dictionary."""
        base = super().asdict(varname)
        base["enum"] = cls.enum
        return base

    @classmethod
    def help(cls, varname: str) -> list[tuple[str, str]]:
        """Generate a help text."""
        # Coerce choices to make mypy happy
        choices: ChoiceType = [
            choice for choice in cls.enum
        ]
        return generate_multi_help_statement(varname, choices, cls.default)


class NumberOption(Option):
    """NUmber option."""

    number: ClassVar[tuple[int, int]]

    def __init__(self, value: ParamType) -> None:
        """Validate input."""
        if isinstance(value, str):
            if not value.isdecimal():
                raise ValueError(f"Expected a decimal number, but got {value}.")

        super().__init__(value)

    def get_value(self) -> int:
        """Return value."""
        return int(self.value)

    @classmethod
    def help(cls, varname: str) -> list[tuple[str, str]]:
        """Generate a help statement."""
        # We won't list every number value, so we specify the options as a range instead.
        return [(f"  {varname}={cls.number[0]}..{cls.number[1]}", cls.title)]

    @classmethod
    def asdict(cls, varname: str) -> dict[str, Any]:
        """Return as dictionary."""
        base = super().asdict(varname)
        base["number"] = cls.number
        return base

    @classmethod
    def from_default(cls) -> "NumberOption":
        """Instantiate with default value."""
        return cls(cls.default)


def option(
    description: str,
    section: str = "Options",
    *,
    choices: list[tuple[str, str]] | None = None,
    minimum: int | None = None,
    maximum: int | None = None,
    default: str | int | bool | None = None,
) -> Any:
    """Define a configurable variable.

    Args:
        description: Description of the variable
        section: The name of the configuration pane where this option should be shown.

    A number of different option types can be generated. Without any further
    options, the option will be a boolean true/false.

    ### Boolean Option

    Example:
    ```python
    enable_arpeggiator: bool = metapatch.option("Enable arpeggiator")
    ```

    ### Number Option
    - minimum: integer
    - maximum: integer

    Example:
    ```python
    midi_channel: int = metaclass.option("MIDI channel", minimum=1, maximum=16)
    ```

    ### Enumeration Option
    - choices: List of tuples. The Tuples define (value, description)

    Example:
    ```python
    clock_source: str = metapatch.option(
        "Clock Source",
        choices=[("internal", "Internal clock"), ("external", "External clock")]
    )
    ```


    ### Defaults
    You can specify a default for any option, otherwise it will be derived as follows:
    - Bool: True
    - Number: Lowest number
    - Enum: First value.

    Example:
    ```python
    enable_arpeggiator: bool = metapatch.option("Enable arpeggiator", default=True)
    ```

    """
    params: dict[str, Any] = {
        "title": description,
        "section": section,
    }
    bases: tuple[type, ...]
    if default:
        params["default"] = default

    if choices:
        # Slightly hacky. We construct a dynamic child class that sets the given
        # title and section. This allows us to use it as a string.
        params["enum"] = choices
        if not default:
            params["default"] = choices[0][0]
        bases = (EnumOption, Option)
        return type("LocalEnumOption", bases, params)  # type: ignore
    elif minimum is not None and maximum is not None:
        params["number"] = (minimum, maximum)
        if not default:
            params["default"] = minimum
        bases = (NumberOption, Option)

        return type("LocalNumberOption", bases, params)  # type: ignore
    else:
        bases = (BoolOption, Option)
        if not default:
            params["default"] = True
        return type("LocalBoolOption", bases, params)  # type: ignore


@dataclass
class Preset:
    """Preset class."""

    title: str
    parameters: dict[str, Any]

    def asdict(self, name: str) -> dict[str, Any]:
        """Construct preset dictionary."""
        return {"name": name, "title": self.title, "parameters": self.parameters}


def preset(title: str, parameters: dict[str, Any]) -> Preset:
    """Define a preset.

    Args:
        title: The name of the preset.
        parameter: A dictionary containing parameter to value mappings.

    This helper function allows you to define presets for your patch generators.
    Presets are essentially just predefined values for your options defined as a python
    dictionary.

    See `metapatch.option` for how to define options.

    Example:
        simple = metapatch.preset("The simplest version", {"voices": 1, "clock_source": "internal"})
    """
    return Preset(title, parameters)
