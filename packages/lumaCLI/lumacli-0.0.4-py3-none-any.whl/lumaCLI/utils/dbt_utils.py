import json
import os
from pathlib import Path
from rich.panel import Panel
from rich import print


def validate_json(json_path: Path, endswith: str = ".json") -> bool:
    """
    Validates whether the provided file is a valid JSON file and ends with the specified string.

    Args:
        json_path (str): The full path to the file to be validated.
        endswith (str, optional): The string the file should end with. Defaults to ".json".

    Returns:
        bool: True if valid, False otherwise.
    """

    # Check that file exists
    if not json_path.is_file():
        error_message = f"[red]Error[/red]: [yellow]{json_path.absolute()}[/yellow] [blue]is not a file[/blue]"
        print(Panel(error_message))
        return False

    # Check that filename ends with the required string
    if not str(json_path).endswith(endswith):
        error_message = f"[red]Error[/red]: [blue]File[/blue] [yellow]{os.path.basename(json_path.absolute())}[/yellow] [blue]does not have the required structure, it should end with [/blue][yellow]'{endswith}'[/yellow]"
        print(Panel(error_message))
        return False

    return True


def json_to_dict(json_path):
    """
    Converts a JSON file to a dictionary.

    Args:
        json_path (str): The full path to the JSON file.

    Returns:
        dict: The JSON data as a dictionary.
    """
    with open(json_path, "r") as json_file:
        json_data: dict = json.load(json_file)
    return json_data


def print_response(response):
    """
    Prints the HTTP response.

    Args:
        response (Response): The HTTP response to be printed.
    """
    if not response.ok:
        try:
            error_message = f"[red]An HTTP error occurred, response status code[/red]: {response.status_code} {response.json()['detail']}"
        except:
            error_message = f"[red]An HTTP error occurred, response status code[/red]: {response.status_code} {response.text}"
        print(Panel(error_message))
    else:
        success_message = (
            "[green]The dbt ingestion to luma was successful!\nItems ingested:[/green]"
        )
        print(Panel(success_message))
        try:
            print(response.json())
        except:
            print(Panel("[red]Error at printing items ingested[/red]"))
