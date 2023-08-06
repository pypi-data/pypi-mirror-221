import csv
import datetime
import logging
import logging.config
import sys
from dataclasses import asdict, fields
from typing import Annotated, Final

import pkg_resources
import typer

from iscwatch.advisory import Advisory
from iscwatch.logconfig import logging_config
from iscwatch.scrape import iter_advisories

logging.config.dictConfig(logging_config)

PACKAGE_NAME: Final = "iscwatch"


def cli():
    """CLI entry point executes typer-wrapped main function"""
    typer.run(main)


def main(
    since: Annotated[
        datetime.datetime,
        typer.Option(
            help="Output only those summaries released or updated since specified date."
        ),
    ] = datetime.datetime.min,
    version: Annotated[bool, typer.Option(help="Output product version and exit.")] = False,
    headers: Annotated[
        bool, typer.Option(help="Include column headers in CSV output.")
    ] = True,
):
    """Disposition command line and vector work to appropriate sub-function."""
    if version:
        print_version()
    else:
        if since:
            selected_advisories = [a for a in iter_advisories() if a.updated >= since.date()]
        else:
            selected_advisories = list(iter_advisories())
        print_csv_advisories(selected_advisories, headers)


def print_csv_advisories(advisories: list[Advisory], use_headers: bool):
    """Convert advisories into dictionaries and output in CSV format."""
    fieldnames = [field.name for field in fields(Advisory)]
    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
    if use_headers:
        writer.writeheader()
    writer.writerows(asdict(advisory) for advisory in advisories)


def print_version():
    """Output current version of the application."""
    try:
        distribution = pkg_resources.get_distribution(PACKAGE_NAME)
        print(f"{distribution.project_name} {distribution.version}")
    except pkg_resources.DistributionNotFound:
        logging.error(f"The package ({PACKAGE_NAME}) is not installed.")
