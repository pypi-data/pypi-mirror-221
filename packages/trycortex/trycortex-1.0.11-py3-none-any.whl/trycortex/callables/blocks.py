import dataclasses

from trycortex.cli import utils

@dataclasses.dataclass
class DatasetConfig:
    dataset: str = ""

@dataclasses.dataclass
class InputBlock(utils.DataClassYamlMixin):
    """Represents an input block in a callable."""
    type: str = "input"
    name: str = "INPUT"
    indent: int = 0
    spec: dict = {}
    configa: dict = {"dataset": ""}

@dataclasses.dataclass
class OutputBlock(utils.DataClassYamlMixin):
    """Represents an output block in a callable."""
    type: str = "output"
    name: str = "OUTPUT"
    indent: int = 0
    spec: dict = {}

@dataclasses.dataclass
class CodeBlock(utils.DataClassYamlMixin):
    """Represents a code block in a callable."""
    type: str = "code"
    name: str
    indent: int = 0
    spec: dict = { "code": "_fun = (env) => {\n  // use `env.state.BLOCK_NAME` to refer output from previous blocks.\n return; \n}"}
    config: dict = {}