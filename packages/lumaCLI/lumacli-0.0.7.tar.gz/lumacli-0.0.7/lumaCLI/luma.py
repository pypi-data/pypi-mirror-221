#!/usr/bin/env python

import typer
import lumaCLI.dbt as dbt
import lumaCLI.postgres as postgres
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


app = typer.Typer(
    name="lumaCLI", no_args_is_help=True, pretty_exceptions_show_locals=False
)

app.add_typer(dbt.app, name="dbt")
app.add_typer(postgres.app, name="postgres")


def cli():
    """For python script installation purposes (flit)"""
    app()


if __name__ == "__main__":
    app()
