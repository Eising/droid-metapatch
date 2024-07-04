"""Circuit writer functions."""

from pathlib import Path
from typing import Dict

from jinja2 import Environment, PackageLoader, select_autoescape

from .types import CircuitCollection


env = Environment(
    loader=PackageLoader("metapatch.circuit_generation"),
    autoescape=select_autoescape(),
    trim_blocks=True,
    lstrip_blocks=True,
)


def _generate_category(collection: CircuitCollection) -> str:
    """Generate category."""
    template = env.get_template("category.j2")
    return template.render(
        droid_version=collection.droid_version, circuits=collection.circuits
    )


def _generate_init(droid_version: str, categories: Dict[str, CircuitCollection]) -> str:
    """Generate module init file."""
    template = env.get_template("init.j2")
    return template.render(droid_version=droid_version, categories=categories)


def _generate_circuits(categories: Dict[str, CircuitCollection]) -> Dict[str, str]:
    """Generate circuits."""
    return {
        category: _generate_category(c_collection)
        for category, c_collection in categories.items()
    }


def write_circuits(collection: CircuitCollection, output_directory: Path) -> None:
    """Write circuits to a directory."""
    assert output_directory.exists(), "Error: Output directory does not exist!"
    assert output_directory.is_dir(), "Error: Output directory is not a directory!"
    init_destination = output_directory / "__init__.py"
    categories = collection.split_categories()

    category_templates = _generate_circuits(categories)
    for category, contents in category_templates.items():
        filename = output_directory / f"{category}.py"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(contents)

    with open(init_destination, "w", encoding="utf-8") as f:
        f.write(_generate_init(collection.droid_version, categories))
