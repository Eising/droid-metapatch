#!/usr/bin/env python3
"""This is a small helper script that can be used to speed up some of the patch building."""
import argparse
import sys
import os
from typing import TextIO


import metapatch.factory


DEFAULT_TITLE = "Draft Patch Generator"
DEFAULT_DESCRIPTION = "A short description"
DEFAULT_CLASSNAME = "PatchGenerator"


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

    subparsers = parser.add_subparsers(help="actions", metavar="action", dest="action")

    convert_parser = subparsers.add_parser(
        "convert", help="Convert (partial) droid patches to python statements."
    )

    convert_parser.add_argument(
        "infile",
        nargs="?",
        type=argparse.FileType("r", encoding="utf-8"),
        default=sys.stdin,
        help="Input file. Defaults to stdin.",
    )
    boilerplate_parser = subparsers.add_parser(
        "generate", help="Generate a patch generator from a droid patch."
    )
    boilerplate_parser.add_argument(
        "infile", type=argparse.FileType("r", encoding="utf-8")
    )
    boilerplate_parser.add_argument(
        "outfile",
        nargs="?",
        type=argparse.FileType("w", encoding="utf-8"),
        default=sys.stdout,
        help="Output file. Defaults to stdout.",
    )

    boilerplate_parser.add_argument(
        "--title", help="Title of your patch generator.", default=DEFAULT_TITLE
    )
    boilerplate_parser.add_argument(
        "--description",
        help="Description of your patch generator.",
        default=DEFAULT_DESCRIPTION,
    )
    boilerplate_parser.add_argument(
        "--classname",
        help="Name of the python class for the patch generator.",
        default=DEFAULT_CLASSNAME,
    )

    parser.epilog = (
        "If called without any arguments, you may input one or more droid circuits, "
        "and get the corresponding python code back."
    )
    args = parser.parse_args()
    if not args.action:
        if not sys.stdin.isatty():
            parser.exit(1)
        else:
            args.action = "convert"
            args.infile = sys.stdin

    return args


def cli_convert(infile: TextIO) -> None:
    """Convert on the CLI."""
    if infile.isatty():
        print("Paste a circuit configuration and finish with ctrl-d.\n")
    buffer = infile.read()

    print(metapatch.factory.generate_snippet(buffer))


def cli_boilerplate(args: argparse.Namespace) -> None:
    """Generate boilerplate."""
    buffer = args.infile.read()
    output = metapatch.factory.generate_boilerplate(
        buffer, args.title, args.description, args.classname
    )
    args.outfile.write(output + os.linesep)


def main() -> None:
    """Main function."""
    args = cli()

    if args.action == "convert":
        cli_convert(args.infile)
    elif args.action == "generate":
        cli_boilerplate(args)
    else:
        print(f"Unsupported action: {args.action}")


if __name__ == "__main__":
    main()
