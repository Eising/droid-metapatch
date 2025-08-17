"""Test helpers."""

import types
import importlib.machinery
from typing import cast
import metapatch
from pathlib import Path


GENERATORDIR = (Path(__file__).parent / "patch_generators").absolute()
PATCHDIR = (Path(__file__).parent / "patches").absolute()

def _import_patch_generator(
    modulename: str | Path,
    classname: str,
) -> type[metapatch.PatchGenerator]:
    """Evaluate a patch generator from file."""
    if isinstance(modulename, str):
        if modulename.endswith(".py"):
            actual_modulename = modulename.split(".py")[0]
        else:
            actual_modulename = modulename
        parent_path = GENERATORDIR
        pg = parent_path / modulename
    else:
        parent_path = modulename.parent.absolute()
        if modulename.name.endswith(".py"):
            actual_modulename = modulename.name.split(".py")[0]
        else:
            actual_modulename = modulename.name
        pg = modulename.absolute()

    loader = importlib.machinery.SourceFileLoader(actual_modulename, str(pg))
    patch_generator_mod = types.ModuleType(loader.name)
    loader.exec_module(patch_generator_mod)
    patch_generator = getattr(patch_generator_mod, classname)

    return cast(type[metapatch.PatchGenerator], patch_generator)

def _compare_output(patch: str, filename: str | Path) -> None:
    """Compare output of patch generator with patch in file."""
    __tracebackhide__ = True  # Hide this function from traceback.
    if isinstance(filename, str):
        filepath = PATCHDIR / filename
    else:
        filepath = filename.absolute()
    with open(filepath, "r", encoding="utf-8") as f:
        expected = f.read()

    assert patch.rstrip("\n") == expected.rstrip("\n")



class MetapatchTestHelper:

    def __init__(
        self, modulename: str | Path, classname: str = "TestMetaPatch"
    ) -> None:
        """Initialize test helper class."""
        self.patch_generator = _import_patch_generator(modulename, classname)
        self.pg_instance: metapatch.PatchGenerator | None = None

    def run(self, **kwargs: str) -> metapatch.PatchGenerator:
        """Instantiate patch generator."""
        if not self.pg_instance:
            self.pg_instance = self.patch_generator(**kwargs)

        return self.pg_instance

    def validate(self, expected: str | Path, **kwargs: str) -> None:
        """Validate patch generator."""
        if not self.pg_instance:
            self.run(**kwargs)

        assert self.pg_instance is not None
        assert isinstance(self.pg_instance, metapatch.PatchGenerator)
        patch = str(self.pg_instance)
        _compare_output(patch, expected)

    @classmethod
    def test(
        cls,
        modulename: str | Path,
        expected: str | Path,
        classname: str = "TestMetaPatch",
        **kwargs: str,
    ) -> None:
        """Run a test from a single function."""
        tester = cls(modulename, classname)
        tester.validate(expected, **kwargs)
