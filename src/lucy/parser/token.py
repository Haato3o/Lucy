from dataclasses import dataclass
from enum import Enum
from ..core.data import MutableData
from ..core.register import Registers
from ..core.data import MutableData
from ..core.operation import Operation
from typing import Union

counter = 0
def auto():
    global counter
    tmp = counter
    counter += 1
    return tmp

class TokenType(Enum):
    # For jump loops, start with : (e.g: ':loop')
    CHECKPOINT      = auto()
    # goto name
    GOTO            = auto()
    # Primitive datas (int, float, string, byte, etc)
    DATA            = auto()
    # mov, push, pop, etc
    INSTRUCTION     = auto()
    # rax, rbx, rcx, etc
    REGISTER        = auto()
    # for comment lines starting in ;
    COMMENT         = auto()

@dataclass
class Token(object):
    typ: TokenType
    value: Union[MutableData, Registers, Operation, str, int, float]

    def __repr__(self):
        return f"<{self.typ.name} value = {self.value}>"

class Tokens:
    DOUBLE_QUOTE = '"'
    COLON = ':'
    SEMI_COLON = ';'