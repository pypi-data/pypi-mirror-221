from enum import Enum
from typing import Callable, List, TypedDict, Optional
from typing_extensions import NotRequired

from ..models.block import Block
import itertools

from ..models.form import Form

# composition type: parallel, exclusive
CompositionType = Enum("parallel", "exclusive")


class InteractiveRssType:
    def __init__(self, article: str, url: str, paragraphs: list[Block]):
        self.article = article
        self.url = url
        self.paragraphs = paragraphs


class InteractiveFunctionResultType:
    def __init__(self, blocks: List[Block], global_block: Optional[Block]):
        self.blocks = blocks
        self.global_block = global_block


class InteractiveFunctionType:
    def __init__(self, id: str, name: str, description: str,
                 function: Callable[[InteractiveRssType, dict], InteractiveFunctionResultType],
                 form: Optional[Form] = None,
                 ):
        self.id = id
        self.name = name
        self.description = description
        self.function = function
        self.form = form


class InteractiveTaskConfiguration(TypedDict):
    name: str
    description: str
    task_type: str
    # task is one of the values in TaskType
    task: Callable
    form: NotRequired[Form]


class InteractiveTaskType:
    id_iter = itertools.count()

    def __init__(self, config: InteractiveTaskConfiguration):
        self.id = str(next(self.id_iter))
        self.name = config['name']
        self.description = config['description']
        self.task_type = config['task_type']
        self.task = config['task']

        if 'form' in config:
            self.form = config['form']
        else:
            self.form = None


class ModelConfiguration:
    def __init__(self, name: str, description: str,
                 functions: List[InteractiveFunctionType],
                 composition: CompositionType):
        self.name = name
        self.description = description
        self.functions = functions
        self.composition = composition

    def get_function(self, _id: str) -> InteractiveFunctionType or None:
        for function in self.functions:
            if function.id == _id:
                return function
        return None

    def __str__(self):
        return f'{self.name}: {self.description}'

    def __repr__(self):
        return f'{self.name}: {self.description}'

    def __dict__(self):
        return {
            'name': self.name,
            'description': self.description,
        }
