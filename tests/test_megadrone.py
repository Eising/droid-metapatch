"""Test megadrone."""
import importlib.machinery
from pathlib import Path

import pytest

scriptpath = Path(__file__).parent

pg = scriptpath / ".." / "examples" / "e4megadrone"
megadrone = importlib.machinery.SourceFileLoader("e4megadrone", str(pg)).load_module()


def test_megadrone():
    """Test megadrone output."""
    patch = megadrone.MegaDrone.load_preset("default")
    expected_file = Path(__file__).parent / "e4megadrone.ini"
    with open(str(expected_file), "r", encoding="utf-8") as f:
        expected = f.read()
        f.flush()

    assert str(patch) == expected
