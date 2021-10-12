from ..parser import Token, TokenType
from ..core.instructions import calculate_max_params, validate_params, Operation, Instruction, is_instruction_implemented
from ..core.data import MutableData
from typing import Any, List, Dict

class LucyValidator(object):
    def __init__(self, tokens: List[Token]):
        self.tokens: List[Token] = tokens
        self.checkpoints: Dict[str, int] = {}

    def validate(self) -> bool():
        program_counter = 0
        while program_counter < len(self.tokens):
            tkn: Token = self.tokens[program_counter]
            count = 0
            
            if tkn.typ == TokenType.CHECKPOINT:
                if not self.validate_checkpoint(tkn.value, program_counter):
                    raise Exception(f"Invalid checkpoint at {program_counter}")
            elif tkn.typ == TokenType.INSTRUCTION:

                if not self.is_instruction_implemented(tkn):
                    print(f"Instruction not implemented yet: {tkn.value}")
                    exit(1)

                n_params = self.get_instruction_params(tkn)
                params = self.tokens[program_counter + 1: program_counter + 1 + n_params]
                valid, count = self.validate_params(tkn.value, params)

                if not valid:
                    print(f"Invalid instruction at {program_counter}")
                    exit(1)
            elif tkn.typ == TokenType.COMMENT:
                pass
            
            program_counter += count + 1
        return True

    def is_instruction_implemented(self, instruction: Token) -> bool:
        return is_instruction_implemented(instruction.value)

    def get_instruction_params(self, instruction: Token) -> int:
        
        if instruction.typ != TokenType.INSTRUCTION:
            raise Exception(f"Token {instruction} is not an instruction")

        return calculate_max_params(instruction.value)

    def _get_equivalent_type(self, token: Token) -> type:
        if token.typ == TokenType.DATA:
            return Any
        elif token.typ == TokenType.REGISTER:
            return MutableData
        elif token.typ == TokenType.GOTO:
            return int

    def validate_params(self, opcode: Operation, params: List[Token]) -> (bool, int):
        params_types: List[type] = []

        for param in params:
            if param.typ in [TokenType.DATA, TokenType.REGISTER, TokenType.GOTO]:
                params_types.append(self._get_equivalent_type(param))

        return (validate_params(opcode, tuple(params_types)), len(params_types))

    def validate_checkpoint(self, name: str, addr: int) -> bool:
        if name in self.checkpoints:
            return False

        self.checkpoints[name[1:]] = addr
        return True

    def validate_goto(self, name: str) -> bool:
        return name in self.checkpoints