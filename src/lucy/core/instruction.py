from .operation import Operation
from dataclasses import dataclass
from typing import Callable, Any

@dataclass
class Instruction:
    operation: Operation
    signature: tuple
    implementation: Callable

    def __call__(self) -> Any:
        return self.implementation()