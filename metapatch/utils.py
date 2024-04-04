"""Utility functions."""

import textwrap
from typing import Optional

COMMENT_LINE_LENGTH = 88


def write_patch_section(name: str, comment: Optional[str] = None) -> str:
    """Write a patch section."""
    delim = f"# {'-'*49}"
    if not comment:
        comment = ""
    else:
        comment = format_comment(comment) + "\n"
    return f"{delim}\n# {name}\n{comment}{delim}\n"


def format_comment(comment_str: str, dedent: bool = False) -> str:
    """Format comments."""
    if dedent:
        comment_str = textwrap.dedent(comment_str)
    lines = textwrap.wrap(comment_str, COMMENT_LINE_LENGTH)
    commented_lines = [f"# {line}" for line in lines]
    return "\n".join(commented_lines)
