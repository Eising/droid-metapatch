"""Patch Generator module.

.. include:: ../README.md

# Public API

"""

from .metapatch import PatchGenerator
from .options import option, preset
from . import circuits
from .circuits.base import transform, DroidCircuit

__docformat__ = "google"

__all__ = [
    "PatchGenerator",
    "option",
    "preset",
    "circuits",
    "transform",
    "DroidCircuit",
]
