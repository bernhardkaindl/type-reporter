"""Command-line interface."""

import click

from type_reporter.type_reporter import main as reporter_main


@click.command()
@click.version_option()
def main(**kwargs: str) -> int:
    """Type Reporter."""
    return reporter_main()


if __name__ == "__main__":
    main(prog_name="type-reporter")  # pragma: no cover
