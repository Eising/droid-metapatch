"""Formatting functions.

This module deals primarily with stripping latex and other formatting from the
raw circuits.
"""

import re
import textwrap

from pylatexenc.latex2text import LatexNodes2Text  # type: ignore


# Mathias' Custom LaTeX macros.
CUSTOM_MACROS = [(r"\\msixteen", "MASTER"), (r"\\meighteen", "MASTER18")]

# The line length in generated circuits.
LINE_WRAP = 88


def strip_latex(text: str) -> str:
    """Strip latex formatting from string."""
    for pat, replacement in CUSTOM_MACROS:
        text = re.sub(pat, replacement, text)
    text = LatexNodes2Text().latex_to_text(text).strip("\t")
    # Modify those frameboxes that remain
    text = text.replace("[5mm][c]", "")
    return text


def reformat_inline_list(text: str, indent: int, line_wrap: int = LINE_WRAP) -> str:
    """Find inline lists."""
    if "*" not in text:
        return text
    # dedent the text
    list_indent = indent * " "
    continuation = list_indent + "  "
    text = textwrap.dedent(text)
    lines = ""
    sections = []
    for line in re.split(r"\s{2,}", text):
        line = line.replace("\n", " ")
        if line.startswith("*"):
            sections.append((True, line))
        else:
            sections.append((False, line))
    for is_list, line in sections:
        if not is_list:
            lines += "\n".join(
                textwrap.wrap(
                    line,
                    width=line_wrap,
                    initial_indent=list_indent,
                    subsequent_indent=list_indent,
                )
            )
        else:
            lines += "\n".join(
                textwrap.wrap(
                    line,
                    width=line_wrap,
                    initial_indent=list_indent,
                    subsequent_indent=continuation,
                )
            )
        lines += "\n"
    return lines


def format_synopsis(
    text: str, line_wrap: int = LINE_WRAP, start_indent: int = 10
) -> str:
    """Format synopsis."""
    descr_indent = " " * start_indent
    body = "\n".join(
        textwrap.wrap(
            text,
            width=LINE_WRAP,
            initial_indent=descr_indent,
            subsequent_indent=descr_indent,
        )
    )
    if "*" in body:
        body = reformat_inline_list(body, start_indent)
    return body
