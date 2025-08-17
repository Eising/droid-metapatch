"""Circuit writer functions."""

import json
from pathlib import Path
from jinja2 import Environment, PackageLoader, select_autoescape

from .models import DroidCircuitSpecRoot, DroidCircuitSpec


env = Environment(
    loader=PackageLoader("metapatch.circuit_generation"),
    autoescape=select_autoescape(),
    trim_blocks=True,
    lstrip_blocks=True,
)


def _generate_category(
    droid_version: str, circuits: dict[str, DroidCircuitSpec]
) -> str:
    """Generate category."""
    template = env.get_template("category.j2")
    return template.render(droid_version=droid_version, circuits=circuits)


def _generate_init(
    droid_version: str, categories: dict[str, dict[str, DroidCircuitSpec]]
) -> str:
    """Generate module init file."""
    template = env.get_template("init.j2")
    return template.render(droid_version=droid_version, categories=categories)


def _generate_circuits(
    droid_version: str, categories: dict[str, dict[str, DroidCircuitSpec]]
) -> dict[str, str]:
    """Generate circuits."""
    return {
        category: _generate_category(droid_version, circuits)
        for category, circuits in categories.items()
    }


def _generate_translator(circuits: dict[str, DroidCircuitSpec]) -> str:
    """Generate a translation JSON for parameter name lookup."""
    template = env.get_template("aliases.j2")
    return template.render(circuits=circuits)


def write_circuits(spec: DroidCircuitSpecRoot, output_directory: Path) -> None:
    """Write circuits to a directory."""
    assert output_directory.exists(), "Error: Output directory does not exist!"
    assert output_directory.is_dir(), "Error: Output directory is not a directory!"
    init_destination = output_directory / "__init__.py"
    alias_destination = output_directory / "aliases.py"
    categories = spec.get_categories()
    category_templates = _generate_circuits(spec.firmware_version, categories)
    for category, contents in category_templates.items():
        filename = output_directory / f"{category}.py"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(contents)
    with open(init_destination, "w", encoding="utf-8") as f:
        f.write(_generate_init(spec.firmware_version, categories))

    with open(alias_destination, "w", encoding="utf-8") as f:
        f.write(_generate_translator(spec.circuits))
