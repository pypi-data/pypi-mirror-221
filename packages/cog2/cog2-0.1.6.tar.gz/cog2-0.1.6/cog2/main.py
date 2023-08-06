import webbrowser
import os
from typing import List
import typer
import requests
from typing_extensions import Annotated
import platform
import subprocess

app = typer.Typer()


def check_os_cog():
    if platform.system() == 'Darwin' or platform.system() == "Linux":
        rc = subprocess.call(['which', 'cog'])
        if rc == 0:
            pass
        else:
            typer.echo("Setting up cog2 for the first time")
            if platform.system() == 'Darwin':
                os.system('brew install cog')
            if platform.system() == 'Linux':
                os.system(
                    "sudo curl -o /usr/local/bin/cog -L https://github.com/replicate/cog/releases/latest/download/cog_`uname -s`_`uname -m`")
                os.system("sudo chmod +x /usr/local/bin/cog")


check_os_cog()


@app.command()
def login():
    typer.echo(
        "This command will authenticate Docker with WizModel's Docker registry. You will need a WizModel.com account."
    )
    input(
        "Hit enter to get started. A browser will open with an authentication token that you need to paste here."
    )
    webbrowser.open("https://www.wizmodel.com/models")
    token = typer.prompt("Paste your token here and press Enter to login")
    data = {"token": token}
    response = requests.post(url="https://api.stagingwazs.online/cog/v1/verify-token", json=data).json()
    user_name = response['username']
    password = response['docker_token']
    os.system("docker login -u {} -p {} registry.wizmodel.com".format(user_name, password))  # noqa: E501


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


@app.command()
def version():
    typer.echo('0.1.6')


@app.command()
def debug():
    os.system("cog debug")
