"""Generate circuits.

This generates objects that matches the available circuits with all their
parameters. These can be used instead of adding circuits by hand.
"""

import argparse
from metapatch.circuit_generation import generate


def cli() -> None:
    """Handle CLI."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "circuitsfile",
        help="circuits.json file.",
    )

    parser.add_argument("directory", help="Directory to write circuits to.")

    args = parser.parse_args()

    generate(args.circuitsfile, args.directory)


if __name__ == "__main__":
    cli()
