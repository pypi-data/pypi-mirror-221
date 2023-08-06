import typer
from typing import List, Dict
import requests
from rich import print
from rich.panel import Panel
from lumaCLI.utils import (
    print_response,
    get_db_metadata,
)


app = typer.Typer(no_args_is_help=True, pretty_exceptions_show_locals=False)


def ask_for_endpoint_if_not_dry_run(endpoint, ctx: typer.Context):
    if ctx.resilient_parsing:
        return
    dry_run = ctx.params.get("dry_run", False)

    if endpoint or dry_run:
        return endpoint

    # Raise a typer.BadParameter exception to simulate the same error as missing 'endpoint'
    raise typer.BadParameter("Missing argument 'ENDPOINT'")


@app.command()
def ingest(
    endpoint: str = typer.Argument(
        None,
        callback=ask_for_endpoint_if_not_dry_run,
        envvar="LUMA_POSTGRES_INGEST_ENDPOINT",
        help="URL of the Luma Postgres ingestion endpoint.",
    ),
    username: str = typer.Option(
        ...,
        "--username",
        "-u",
        envvar="LUMA_POSTGRES_USERNAME",
        help="PostgreSQL username.",
        prompt="PostgreSQL username: ",
    ),
    database: str = typer.Option(
        ...,
        "--database",
        "-d",
        envvar="LUMA_POSTGRES_DATABASE",
        help="PostgreSQL database.",
        prompt="PostgreSQL database: ",
    ),
    host: str = typer.Option(
        "localhost",
        "--host",
        "-h",
        envvar="LUMA_POSTGRES_HOST",
        help="PostgreSQL host.",
    ),
    port: str = typer.Option(
        "5432",
        "--port",
        "-p",
        envvar="LUMA_POSTGRES_PORT",
        help="PostgreSQL port.",
    ),
    password: str = typer.Option(
        ...,
        "--password",
        "-P",
        envvar="LUMA_POSTGRES_PASSWORD",
        help="PostgreSQL password.",
        prompt="PostgreSQL password: ",
        hide_input=True,
    ),
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        "-D",
        help="Whether to do a dry run. Print but not send the payload",
    ),
):
    """
    Creates dictionary with Postgres Metadata Information and sends it to the Luma Postgres ingest endpoint.
    """
    db_metadata: Dict[str, List[Dict]] = get_db_metadata(
        username=username, database=database, host=host, port=port, password=password
    )

    if dry_run:
        print(db_metadata)
        return db_metadata

    try:
        # Send payload to Luma endpoint
        response = requests.post(
            endpoint, json=db_metadata, verify=False, timeout=(3.05, 60 * 30)
        )
        print_response(response)
        return response
    except requests.exceptions.RequestException as e:
        error_message = f"[red]An error occurred while sending the request to the Luma endpoint:[/red] {str(e)}"
        print(Panel(error_message))
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
