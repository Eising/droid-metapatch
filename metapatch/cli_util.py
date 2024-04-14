#!/usr/bin/env python3
"""This is a small helper script that can be used to speed up some of the patch building."""
import argparse
import sys
import os
import re
import keyword

from dataclasses import dataclass
from typing import Iterator, Dict, List, Optional

import metapatch.factory


def get_patch_stdin() -> str:
    """Read a patch from stdin."""
    buffer = []
    empty_lines = 0
    while True:
        line = sys.stdin.readline()
        if line == "\n":
            empty_lines += 1
            if empty_lines == 2:
                break
            else:
                buffer.append(line.rstrip("\n"))
        elif line == "":
            break
        else:
            buffer.append(line.rstrip("\n"))

    return "\n".join(buffer)


def cli() -> argparse.Namespace:
    """Parse cli."""
    parser = argparse.ArgumentParser(description="Metapatch helper script.")
    parser.add_argument(
        "infile",
        nargs="?",
        type=argparse.FileType("r", encoding="utf-8"),
        default=sys.stdin,
        help="Input file. Defaults to stdin.",
    )
    parser.add_argument(
        "outfile",
        nargs="?",
        type=argparse.FileType("w", encoding="utf-8"),
        default=sys.stdout,
        help="Output file. Defaults to stdout.",
    )
    parser.add_argument(
        "--boilerplate",
        action="store_true",
        help="Generate a full example patch generator.",
    )
    parser.epilog = (
        "If called without any arguments, you may input one or more droid circuits, "
        "and get the corresponding python code back."
    )
    args = parser.parse_args()
    return args


def main() -> None:
    """Main function."""
    args = cli()
    if args.infile.isatty():
        print("Paste a circuit configuration and finish with ctrl-d.\n")
    buffer = args.infile.read()
    if args.boilerplate:
        # output = generate_boilerplate(buffer)
        output = metapatch.factory.generate_boilerplate(buffer)
    else:
        output = metapatch.factory.generate_snippet(buffer)

    args.outfile.write(output + os.linesep)


if __name__ == "__main__":
    main()
