import functools
import pathlib
import re
from typing import List
import click
import validators
import os
import urllib.request
import trycortex

from trycortex.cli.callable import callable_config

# Regex pattern to match valid entry points: "module:object"
VAR_NAME_RE = r"(?![0-9])\w+"
ENTRY_POINT_PATTERN = re.compile(rf"^{VAR_NAME_RE}(\.{VAR_NAME_RE})*:{VAR_NAME_RE}$")
VISIBILITY_RE = r"^(Private|private|Public|public|Unlisted|unlisted)$"
VISIBILITY_PATTERN = re.compile(VISIBILITY_RE)
TEMPLATE_RE = r"^(barbone|chat|chat with history)$"
TEMPLATE_PATTERN = re.compile(TEMPLATE_RE)

REQUIREMENTS_TXT = "requirements.txt"
CURRENT_CORTEX_REQUIREMENT = f"trycortex ~= {trycortex.__version__}"
CORTEX_REQUIREMENT_PATTERN = re.compile(r"^\s*trycortex([^\w]|$)")

CALLABLE_TEMPLATE_URL = (
    "https://raw.githubusercontent.com/kinesysai/cortex-py/main/template.py"
)



@click.group(help="Callable-related commands")
def callable():
    pass

def _slugify(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_-]+", "-", s)
    s = s.strip("-")
    return s

def _update_callable_requirements(
    existing_requirements: List[str], new_requirements: List[str]
) -> List[str]:
    """Returns an updated list of callable requirements to go in requirements.txt."""

    # If the user specified a trycortex requirement, use that.
    cortex_requirement = next(
        filter(
            functools.partial(re.match, CORTEX_REQUIREMENT_PATTERN), new_requirements
        ),
        CURRENT_CORTEX_REQUIREMENT,
    )

    # Ensure that a compatible version of the Cortex SDK is present.
    resolved_requirements: List[str] = []

    for existing_requirement in existing_requirements:
        if (
            re.match(CORTEX_REQUIREMENT_PATTERN, existing_requirement)
            and existing_requirement != cortex_requirement
        ):
            # Ignore any existing (but different) cortex requirements.
            continue

        resolved_requirements.append(existing_requirement)

    for new_requirement in [cortex_requirement] + new_requirements:
        if new_requirement not in resolved_requirements:
            resolved_requirements.append(new_requirement)

    return resolved_requirements

@callable.command("init", help="Creates an callable.yaml file.")
@click.option("--name", help="Name of the callable.")
@click.option("--description", help="Description of the callable.")
@click.option("--visibility", help="Visibility of the callable.")
@click.option("--template", help="Template of the callable.")
@click.option("--entry-point", help="Python entry point of the callable.")
@click.option(
    "--requirement",
    multiple=True,
    type=str,
    help="Additional requirements for requirements.txt. Can be specified multiple times.",
)
@click.argument("path", required=False)
def init_callable(path, name, description, visibility, template, entry_point:str,requirement):
    click.echo("init callable")
    path = pathlib.Path(path or ".")
    path.mkdir(parents=True, exist_ok=True)

    try:
        current_config = callable_config.load_config(path)
    except FileNotFoundError:
        current_config = callable_config.CallableConfig(name=_slugify(path.resolve().name))

    
    while name is None or not validators.slug(name):
        if name is not None:
            click.secho("Name can be alpha numerics, underscores and dashes only.")
        name = click.prompt("Name", default=current_config.name)

    if description is None:
        description = click.prompt("Description", default=current_config.description)

    while entry_point is None or not ENTRY_POINT_PATTERN.match(entry_point):
        if entry_point is not None:
            click.echo(
                "Entrypoint must be in module:attribute format (e.g. 'main:callable', 'main:run')"
            )

        entry_point = click.prompt(
            "Python Entrypoint (module:attribute)", default=current_config.entry_point
        )
    
    while visibility is None or not VISIBILITY_PATTERN.match(visibility):
        if visibility is not None:
            click.secho("Visibility should be one of private, public or unlisted.")
        visibility = click.prompt("Visibility", default=current_config.visibility)

    while template is None or not TEMPLATE_PATTERN.match(template):
        if template is not None:
            click.secho("Template should be one of barbone, chat or chat with history")
        template = click.prompt("Template", default=current_config.template)
    
    current_config.name = name
    current_config.description = description
    current_config.entry_point = entry_point
    current_config.visibility = visibility
    current_config.template = template
    callable_config.save_config(current_config, path)

    entry_module, _ = entry_point.split(":")
    expected_main_path = path / (entry_module.replace(".", "/") + ".py")
    if not os.path.exists(expected_main_path):
        urllib.request.urlretrieve(CALLABLE_TEMPLATE_URL, expected_main_path)
        click.secho(
            f"Initialized callable.yaml and made a template callable file at {expected_main_path}",
            fg="green",
        )
    else:
        click.secho(f"Initialized callable.yaml.", fg="green")
    
    try:
        with open(path / REQUIREMENTS_TXT, "rt") as requirements_txt:
            existing_requirements = list(
                r.strip() for r in requirements_txt.readlines()
            )
    except FileNotFoundError:
        existing_requirements = []

    resolved_requirements = _update_callable_requirements(
        existing_requirements, list(requirement)
    )
    if not existing_requirements:
        write_requirements = True
    else:
        new_requirements = [
            r for r in resolved_requirements if r not in existing_requirements
        ]
        removed_requirements = [
            r for r in existing_requirements if r not in resolved_requirements
        ]

        if new_requirements or removed_requirements:
            click.secho(
                f"{path / REQUIREMENTS_TXT} already exists.",
                fg="yellow",
            )
            if new_requirements:
                click.secho(
                    f"The following requirements will be added: {new_requirements}",
                    fg="yellow",
                )
            if removed_requirements:
                click.secho(
                    f"The following requirements will be removed: {removed_requirements}",
                    fg="yellow",
                )
            write_requirements = click.confirm("Okay to proceed?", default=True)
        else:
            write_requirements = False

    if write_requirements:
        with open(path / REQUIREMENTS_TXT, "wt") as requirements_txt:
            requirements_txt.writelines(r + "\n" for r in resolved_requirements)
