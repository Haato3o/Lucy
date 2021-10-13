from dataclasses import dataclass
from typing import Callable
from ..core.instruction import Instruction

@dataclass
class LucyInstruction:
    op_code: Instruction
    parameters: tuple