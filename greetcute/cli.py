# -*- coding: utf-8 -*-

"""Console script for greetcute."""
import sys
import click

from greetcute import greet


@click.command()
def main(args=None):
    """Console script for greetcute."""
    greet()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
