from typing import List
from .tokens import Token, TokenType

class ASMParser:
    def __init__(self, assembly: str):
        self._stream: str = assembly
        self._cursor = 0
        pass

    '''
        mov eax, "string here"
        :loop
        jmp loop
    '''


    def _parse(self) -> List[Token]:
        trash = ['', '\n']
        tokens: List[Token] = []

        while self._cursor < len(self._stream):

            if (char := self._read_token()) != None:
                tokens.append(char)


        return tokens

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

    def _read_string(self) -> Token:
        value: str = ""
        stack = [self._consume_char()]
        while len(stack) > 0:
            char = self._consume_char()

            if char == '"':
                stack.pop()
                continue

            value += char
        
        return Token(value, TokenType.STRING)
    
    def _read_token(self) -> Token:
        c = self._read()
        peek = self._peek()
        if c == '"':
            return self._read_string()
        else:
            token = self._read_raw_value()
            
            if token is None:
                return None

            if token.isnumeric():
                return self._int(token)
            elif self._is_hex(token):
                return self._int_hex(token)

            return self._instruction(token)

    def _read_raw_value(self) -> str:
        value: str = ""
        
        while (c := self._consume_char()) not in [' ', ',', '\n']:
            value += c
        
        if len(value) > 0:
            return value

        return None

    def _is_hex(self, string: str) -> int:
        def hex(val: str) -> bool:
            valid_chars = "1234567890ABCDEFabcdef"
            
            for i in val:
                if i not in valid_chars:
                    return False
            
            return True

        if string.startswith("0x") and hex(string[2:]):
            return True
        elif string[-1] in ["h", "H"] and hex(string[0:-1]):
            return True
        else:
            return False

    def _from_hex(self, string: str) -> int:
        def hex(val: str) -> bool:
            valid_chars = "1234567890ABCDEFabcdef"
            
            for i in val:
                if i not in valid_chars:
                    return False
            
            return True

        if string.startswith("0x") and hex(string[2:]):
            return int(string[2:], 16)
        elif string[-1] in ["h", "H"] and hex(string[0:-1]):
            return int(string[0:-1], 16)

    def _register(self, raw: str) -> Token:
        return Token(raw, TokenType.REGISTER)

    def _instruction(self, raw: str) -> Token:
        return Token(raw, TokenType.INSTRUCTION)

    def _int_hex(self, raw: str) -> Token:
        return Token(self._from_hex(raw), TokenType.NUMBER)

    def _int(self, raw: str) -> Token:
        return Token(int(raw), TokenType.NUMBER)