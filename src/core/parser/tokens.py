from enum import Enum
from dataclasses import dataclass
from typing import Any

class TokenType(Enum):
    GOTO = 0
    STRING = 1
    HEX_NUMBER = 2
    NUMBER = 3
    FLOAT = 4
    DOUBLE = 5
    INSTRUCTION = 6
    REGISTER = 7
    

@dataclass
class Token:
    value: Any
    token_type: TokenType

    def __repr__(self):
        return f"<Token {self.token_type}, {self.value}>"