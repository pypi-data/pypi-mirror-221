import webbrowser
import os
from typing import List
import typer
import requests
from typing_extensions import Annotated

app = typer.Typer()


@app.command()
def login():
    typer.echo(
        "This command will authenticate Docker with WizModel's Docker registry. You will need a WizModel.com account."
    )
    input(
        "Hit enter to get started. A browser will open with an authentication token that you need to paste here."
    )
    webbrowser.open("https://www.wizmodel.com/")
    token = typer.prompt("Paste your token here and press Enter to login")
    data = {"token": token}
    response = requests.post(url="https://api.stagingwazs.online/cog/v1/verify-token", json=data).json()
    user_name = response['username']
    password = response['docker_token']
    os.system("docker login -u {} -p {} registry.gpu-backend-prod.xyz".format(user_name, password))  # noqa: E501
    typer.echo("Login cmd finished")


@app.command()
def build(
        tag: Annotated[str, typer.Option("--tag", "-t")] = "",
        no_cache: bool = typer.Option(False),
        separate_weights: bool = typer.Option(False),
        secret: Annotated[str, typer.Option("--secret")] = ""
):  # noqa: E501
    typer.echo("Building image with tag %s" % tag)
    prefix_cmd = "cog build"
    if tag != "":
        prefix_cmd = prefix_cmd + " -t {}".format(tag)
    if no_cache:
        prefix_cmd = prefix_cmd + " --no-cache"
    if separate_weights:
        prefix_cmd = prefix_cmd + " --separate-weights"
    if len(secret) > 0:
        prefix_cmd = prefix_cmd + " --secret {}".format(secret)
    os.system(prefix_cmd)
    typer.echo("Build cmd finish: " + prefix_cmd)


@app.command()
def push(
        no_cache: bool = typer.Option(False),
        separate_weights: bool = typer.Option(False),
        secret: Annotated[str, typer.Option("--secret")] = ""
):
    prefix_cmd = "cog push"
    if no_cache:
        prefix_cmd = prefix_cmd + " --no-cache"
    if separate_weights:
        prefix_cmd = prefix_cmd + " --separate-weights"
    if len(secret) > 0:
        prefix_cmd = prefix_cmd + " --secret {}".format(secret)
    os.system(prefix_cmd)
    typer.echo("Push cmd finish: " + prefix_cmd)


@app.command()
def predict(input: Annotated[List[str], typer.Option("--input", "-i")] = [],
            output: Annotated[str, typer.Option("--output", "-o")] = ""):  # noqa: E501
    prefix_cmd = "cog predict"
    if len(input) > 0:
        for item in input:
            prefix_cmd = prefix_cmd + " -i {}".format(item)
    if output != "":
        prefix_cmd = prefix_cmd + " --output {}".format(output)
    os.system(prefix_cmd)
    typer.echo("Predict cmd finished: " + prefix_cmd)


@app.command()
def run(publish: Annotated[str, typer.Option("--publish", "-p")] = ""):
    prefix_cmd = "cog run"
    if len(publish) > 0:
        prefix_cmd = prefix_cmd + " -p {}".format(publish)
    os.system(prefix_cmd)
    typer.echo("Run cmd finished: " + prefix_cmd)
