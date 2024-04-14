"""Formatting utilities."""

import textwrap

from typing import Optional

DEFAULT_LINEWIDTH = 88


def find_string_indent_level(text: str) -> int:
    """Find the indentation level of a string."""
    if not text.startswith(" "):
        return 0

    indent = 0
    for index in range(0, len(text)):
        if text[index] == " ":
            continue
        else:
            indent = index
            break

    if indent > 0:
        return int(indent / 4)

    return indent


def find_last(text: str, char: str, maxpos: Optional[int] = None) -> Optional[int]:
    """Find the last position of something in a string."""
    length = len(text)
    if not text.find(char):
        return None
    startpos = text.find(char) + 1
    pos = startpos
    while startpos < length:
        newpos = text.find(char, startpos, -1)
        if maxpos and newpos > maxpos:
            break
        if newpos > -1:
            pos = newpos
            startpos = newpos + 1
        else:
            break
    return pos


def format_line(text: str) -> str:
    """Format line so that long lines are nicely wrapped.

    Args:
        full_line: The entire line
        specific_item: The item that needs to be formatted
    """
    if len(text.rstrip()) < DEFAULT_LINEWIDTH:
        return text

    if '"' in text:
        # We break at the first assignment
        pos = text.find('"')
        startstr = text[:pos]
        if len(startstr) > DEFAULT_LINEWIDTH:
            # We should do something about that...
            startstr = format_line(startstr)

        # The text before might have become multiline, so we only count the final line
        start_last_line = startstr.splitlines()[-1]
        indent = find_string_indent_level(start_last_line)

        # We insert a (, go down a line, and then we have the current indentation as width.
        startstr = startstr.rstrip() + "(\n"

        # our new maximum string length is LINEWIDTH - indent - 4 (one level deeper than the last line)
        available_width = DEFAULT_LINEWIDTH - (4 * indent + 4)
        quoted = text[pos:]
        # We could split it at the original line ending, or we can just combine everything to one big string.
        lines = quoted.split("\\n")
        new_lines = []
        for index, line in enumerate(lines):
            if index == 0:
                start_indent = ""
            else:
                start_indent = "\\n"
            new_lines.extend(
                [
                    subline
                    for subline in textwrap.wrap(
                        line,
                        width=available_width,
                        initial_indent=start_indent,
                        subsequent_indent="\\n",
                    )
                ]
            )

        parent_indentstr = "    " * indent
        indentstr = "    " * (indent + 1)
        termination = '"'

        # Make groups of lines
        groups = []
        had_comma = False
        for index, part in enumerate(new_lines):
            if index == 0:
                groupstr = f"{indentstr}{part}"
            else:
                groupstr = f"{indentstr}{termination}{part}"

            if groupstr.endswith('",'):
                # This is the last one, we need to remove the comma.
                groupstr = groupstr[:-1]
                had_comma = True
            elif not groupstr.endswith(termination):
                groupstr += termination

            groups.append(groupstr)

        # Join everything up
        if had_comma:
            epilogue = "),\n"
        else:
            epilogue = ")\n"
        endstr = "\n".join(groups) + f"\n{parent_indentstr}{epilogue}"
        return startstr + endstr

    # If there's no quoted assignment, we split last possible parenthesis
    last_paren = find_last(text, "(", DEFAULT_LINEWIDTH)
    if last_paren:
        splitpos = last_paren + 1
        before = text[splitpos:]
        after = text[:splitpos]
        endsplit = find_last(after, ")")
        assert endsplit is not None
        content = after[:endsplit]
        inner = textwrap.indent(content, "    ")
        after_inner = after[endsplit:]
        return "\n".join([before, inner, after_inner])

    # If no parens, I don't know what to do.
    return text
