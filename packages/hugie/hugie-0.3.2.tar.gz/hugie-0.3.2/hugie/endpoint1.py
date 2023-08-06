from typing import Optional

import requests
import typer

from hugie.models import InferenceEndpointConfig
from hugie.settings import Settings
from hugie.utils import TokenNotSetError, format_table, handle_request_error, load_json

settings = Settings()

app = typer.Typer()

headers = {
    "Authorization": f"Bearer {settings.token}",
    "Content-Type": "application/json",
}
API_ERROR_MESSAGE = "An error occured while making the API call"


if not settings.token:
    raise TokenNotSetError


@app.command("ls")
@app.command("list")
def list(
    json: Optional[bool] = typer.Option(
        None, "--json", help="Prints the full output in JSON."
    )
):
    """
    List all the deployed endpoints
    """
    response = requests.get(settings.endpoint_url, headers=headers)

    if json:
        return typer.echo(response.json())

    else:
        data = response.json()

        if data.get("items"):

            names = []
            states = []
            models = []
            revs = []
            url = []

            for item in data["items"]:
                names.append(item["name"])
                states.append(item["status"]["state"])
                models.append(item["model"]["repository"])
                revs.append(item["model"]["revision"])
                url.append(item["status"].get("url"))

                table = format_table(
                    ["Name", "State", "Model", "Revision", "Url"],
                    names,
                    states,
                    models,
                    revs,
                    url,
                )

            typer.secho(table)
        else:
            typer.secho("No endpoints found")


@app.command()
def create(
    data: str = typer.Argument(..., help="Path JSON data to create the endpoint"),
    json: Optional[bool] = typer.Option(
        None, "--json", help="Prints the full output in JSON."
    ),
):
    """
    Create an endpoint

    Args:
        data (str): Path to JSON data to create the endpoint
    """

    data = InferenceEndpointConfig.from_json(data).model_dump()
    name = data["name"]
    vendor = data["provider"]["vendor"]
    repository = data["model"]["repository"]

    try:
        # Try to create the endpoint

        response = requests.post(settings.endpoint_url, headers=headers, json=data)
        response.raise_for_status()

    except (requests.exceptions.HTTPError, requests.exceptions.RequestException) as e:

        handle_request_error(e)

    except Exception as e:

        # Catch all other exceptions

        typer.secho("An unexpected error occured", fg=typer.colors.RED)
        raise SystemExit(e)

    else:

        # If the command succeeds print this output and exit with code 0

        typer.secho(
            f"Endpoint {name} created successfully on {vendor} using {repository}",
            fg=typer.colors.GREEN,
        )

        if json:
            typer.echo(response.json())
        typer.exit(0)


@app.command()
def update(
    name: str = typer.Argument(..., help="Endpoint name"),
    data: str = typer.Argument(..., help="Path to JSON data to update the endpoint"),
    json: Optional[bool] = typer.Option(
        None, "--json", help="Prints the full output in JSON."
    ),
):
    """
    Update an endpoint
    """
    data = InferenceEndpointConfig.from_json(data).model_dump()

    try:
        response = requests.put(
            f"{settings.endpoint_url}/{name}", headers=headers, json=data
        )
        response.raise_for_status()

    except (requests.exceptions.HTTPError, requests.exceptions.RequestException) as e:

        handle_request_error(e)

    except Exception as e:

        # Catch all other exceptions

        typer.secho("An unexpected error occured", fg=typer.colors.RED)
        raise SystemExit(e)

    else:
        typer.secho("Endpoint updated successfully", fg=typer.colors.GREEN)

        if json:
            typer.echo(response.json())

        typer.exit(0)


@app.command()
def delete(
    name: str = typer.Argument(..., help="Endpoint name"),
    force: bool = typer.Option(
        False, "--force", "-f", help="Force deletion without asking user confirmation"
    ),
):
    """
    Delete an endpoint
    """

    if not force:
        delete_endpoint = typer.confirm(
            "Are you sure you want to delete endpoint. Use --force to override"
        )

        if not delete_endpoint:
            typer.echo("Not deleting endpoint")
            raise typer.Abort()

    if force or delete_endpoint:
        try:
            response = requests.delete(
                f"{settings.endpoint_url}/{name}", headers=headers, json={}
            )
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            if response.status_code == 404:
                typer.secho(
                    f"Endpoint {name} does not exist so it cannot be deleted",
                    fg=typer.colors.YELLOW,
                )
                raise SystemExit
            else:
                typer.secho(API_ERROR_MESSAGE, fg=typer.colors.RED)
                raise SystemExit(e)

        typer.secho("Endpoint deleted successfully", fg=typer.colors.GREEN)


@app.command()
def info(
    name: str = typer.Argument(..., help="Endpoint name"),
    json: Optional[bool] = typer.Option(
        None, "--json", help="Prints the full output in JSON."
    ),
):
    """
    Get info about an endpoint
    """

    try:
        response = requests.get(
            f"{settings.endpoint_url}/{name}", headers=headers, json={}
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        typer.secho(API_ERROR_MESSAGE, fg=typer.colors.RED)
        raise SystemExit(e)

    info = response.json()

    if info.get("name"):

        if json:
            typer.echo(info)

        else:
            names = []
            states = []
            models = []
            revs = []
            url = []

            names.append(info["name"])
            states.append(info["status"]["state"])
            models.append(info["model"]["repository"])
            revs.append(info["model"]["revision"])
            url.append(info["status"].get("url"))

            table = format_table(
                ["Name", "State", "Model", "Revision", "Url"],
                names,
                states,
                models,
                revs,
                url,
            )

            typer.secho(table)
    else:
        typer.secho(f"Endpoint {name} not found")


@app.command()
def logs(name: str = typer.Argument(..., help="Endpoint name")):
    """
    Get logs about an endpoint
    """
    try:
        response = requests.get(
            f"{settings.endpoint_url}/{name}/logs", headers=headers, json={}
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        typer.secho(API_ERROR_MESSAGE, fg=typer.colors.RED)
        raise SystemExit(e)

    typer.echo(response.content)


@app.command()
def test(
    name: str = typer.Argument(..., help="Endpoint name"),
    inputs: str = typer.Argument(None, help="Input to send the model."),
    input_file: str = typer.Option(
        None, help="Path to JSON file containing queries to send to the model."
    ),
):
    """
    Test an endpoint
    """

    if not inputs and not input_file:
        typer.secho(
            "You must provide either an input string or an input JSON containing your queries",
            fg=typer.colors.RED,
        )
        raise typer.Abort()

    # Get the endpoint url from endpoint info
    try:
        response = requests.get(
            f"{settings.endpoint_url}/{name}", headers=headers, json={}
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        typer.secho(API_ERROR_MESSAGE, fg=typer.colors.RED)
        raise SystemExit(e)

    info = response.json()
    url = info["status"]["url"]

    if input_file:
        data = load_json(input_file)
    else:
        data = {"inputs": inputs}

    # Send a call to the endpoint
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        typer.secho(API_ERROR_MESSAGE, fg=typer.colors.RED)
        raise SystemExit(e)

    typer.echo(response.json())
