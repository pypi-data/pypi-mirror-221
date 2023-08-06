from typing import List
import typer
from sentential.lib.clients import clients
from sentential.lib.drivers.local_images import LocalImagesDriver
from sentential.lib.drivers.local_lambda import LocalLambdaDriver
from sentential.lib.drivers.aws_ecr import AwsEcrDriver
from sentential.lib.drivers.aws_lambda import AwsLambdaDriver
from sentential.lib.template import Init
from sentential.lib.shapes import Architecture, Runtimes
from sentential.lib.ontology import Ontology
from sentential.lib.joinery import Joinery
from rich import print

root = typer.Typer()


@root.command()
def init(repository_name: str, runtime: Runtimes):
    """initialize sentential project"""
    aws_supported_image = f"public.ecr.aws/lambda/{runtime.value}:latest"
    Init(repository_name, aws_supported_image).scaffold()


@root.command()
def build(
    arch: Architecture = typer.Option(Architecture.system().value),
    ssh_agent: bool = typer.Option(False),
):
    """build lambda image"""
    ontology = Ontology()
    LocalLambdaDriver(ontology).destroy()
    LocalImagesDriver(ontology).build(arch, ssh_agent)


@root.command()
def publish(
    major: bool = typer.Option(False),
    minor: bool = typer.Option(False),
    arch: List[Architecture] = typer.Option([Architecture.system().value]),
    multiarch: bool = typer.Option(False),
    ssh_agent: bool = typer.Option(False),
):
    """publish lambda image"""
    ontology = Ontology()
    tag = AwsEcrDriver(ontology).next(major, minor)
    docker = LocalImagesDriver(ontology)

    if multiarch:
        docker.publish(tag, [a for a in Architecture], ssh_agent)
    else:
        docker.publish(tag, [a for a in arch], ssh_agent)


@root.command()
def login():
    """login to ecr"""
    clients.docker.login_ecr()


@root.command()
def ls(verbose: bool = typer.Option(False)):
    """list image information"""
    print(Joinery(Ontology()).list(verbose))


@root.command()
def clean(
    remote: bool = typer.Option(False),
    remote_logs: bool = typer.Option(False),
    stores: bool = typer.Option(False),
):
    """clean images (and logs)"""
    ontology = Ontology()
    LocalImagesDriver(ontology).clean()
    if remote:
        AwsEcrDriver(ontology).clean()
    if (
        remote_logs
    ):  # MAYBE: is it time to graduate to `clean local` and `clean remote`?
        AwsLambdaDriver(ontology).clean()
    if stores:
        Ontology().clear_stores()
