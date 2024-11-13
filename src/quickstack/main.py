import os

import click
from copier import run_copy


@click.command()
@click.option(
    "--destination",
    prompt="Enter destination path",
    help="Path to generate the project",
)
def generate_project(destination: str):
    """Generate a project from the template."""
    template_path = os.path.join(os.path.dirname(__file__), "../project_template")
    run_copy(template_path, destination)
    click.echo("Project generated successfully at {}".format(destination))


if __name__ == "__main__":
    generate_project()
