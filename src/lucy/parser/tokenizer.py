from typing import Union, List
from ..core.register import Registers
from ..core.operation import Operation
from ..core.stack import Stack
from .token import Token, TokenType, Tokens

class LucyTokenizer(object):
    def __init__(self, stream: str):
        self._stream: str = stream
        self._cursor: int = 0
        self._checkpoints = []

    def __call__(self) -> List[Token]:
        tokens: Stack = Stack()

        while self._cursor < len(self._stream):
            
            if (token := self._read_token()) != None:
                tokens.push(token)

        return tokens.as_list()

    def _read_token(self) -> Union[Token, None]:
        char = self._read()
        peek = self._peek()

        if char == Tokens.DOUBLE_QUOTE:
            return self._read_string()
        elif char == Tokens.SEMI_COLON:
            return self._read_comment()
        else:
            raw = self._read_raw()

            if not raw:
                return None

            if LucyTokenizer.is_integer(raw):
                return self._tokenize_int(raw)
            elif LucyTokenizer.is_operation(raw):
                return self._tokenize_instruction(raw)
            elif LucyTokenizer.is_register(raw):
                return self._tokenize_register(raw)
            elif LucyTokenizer.is_checkpoint(raw):
                return self._tokenize_checkpoint(raw)
            elif self.is_goto(raw):
                return self._tokenize_goto(raw)
            else:
                raise Exception(f"invalid token: {raw}")

    def _read(self) -> str:
        char = self._stream[self._cursor]
        return char
    
    def _peek(self) -> str:
        if (self._cursor + 1) >= len(self._stream):
            return None

        char = self._stream[self._cursor + 1]
        return char

    def _consume_char(self) -> str:
        char = self._stream[self._cursor]
        self._cursor += 1
        return char
    
    def _consume_chars(self, chars: List[str]):
        while self._stream[self._cursor] in chars:
            c = self._consume_char()

    def _read_raw(self) -> str:
        raw: str = ""
        
        while self._cursor < len(self._stream) and (c := self._consume_char()) not in [' ', ',', '\n', '\r', '\t']:
            raw += c

        if len(raw) > 0:
            return raw
        
        return None

    def _read_string(self) -> Token:
        value: str = ""
        stack = [self._consume_char()]
        # TODO: Parse escaped quotes
        while len(stack) > 0:
            char = self._consume_char()

            if char == Tokens.DOUBLE_QUOTE:
                stack.pop()
                continue

            value += char
        
        return Token(TokenType.DATA, value)

    def _read_comment(self) -> Token:
        comment: str = ""
        while (self._cursor < len(self._stream)) and (c := self._consume_char()) not in ['\n', '\r']:
            comment += c
        
        return Token(TokenType.COMMENT, comment)

    @staticmethod
    def from_hex(string: str) -> int:
        def is_hex(val: str) -> bool:
            valid_chars = "0123456789ABCDEFabcdef"

            for c in val:
                if c not in valid_chars:
                    return False

            return True

        if string.startswith("0x") and is_hex(string[2:]):
            string = string[2:]
        elif string[-1] in ["h", "H"] and is_hex(string[:-1]):
            string = string[:-1]
        else:
            raise Exception("Invalid hex value")
        
        return int(string, 16)

    def _tokenize_int(self, raw: str) -> Token:
        if raw.lower().startswith("0x") or raw.lower().endswith("h"):
            return Token(TokenType.DATA, LucyTokenizer.from_hex(raw))
        else:
            return Token(TokenType.DATA, int(raw))
    
    def _tokenize_register(self, raw: str) -> Token:
        try:
            reg = Registers[raw.upper()]
        except:
            raise Exception(f"Invalid register name: {raw.upper()}")

        return Token(TokenType.REGISTER, reg)
    
    def _tokenize_instruction(self, raw: str) -> Token:
        try:
            op = Operation[raw.upper()]
        except:
            raise Exception(f"Invalid op name: {raw.upper()}")
        
        return Token(TokenType.INSTRUCTION, op)

    def _tokenize_checkpoint(self, raw: str) -> Token:
        self._checkpoints.append(raw[1:])

        return Token(TokenType.CHECKPOINT, raw)

    def _tokenize_goto(self, raw: str) -> Token:
        return Token(TokenType.GOTO, raw)

    @staticmethod
    def is_register(name: str):
        try:
            Registers[name.upper()]
            return True
        except:
            return False

    @staticmethod
    def is_operation(name: str):
        try:
            Operation[name.upper()]
            return True
        except:
            return False

    @staticmethod
    def is_integer(value: str):
        return value.lower().startswith("0x") or value.lower().endswith("h") or value.isnumeric()
    
    @staticmethod
    def is_checkpoint(value: str):
        return value.startswith(Tokens.COLON)
    
    def is_goto(self, value: str):
        return value in self._checkpoints