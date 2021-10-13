from ..parser.token import TokenType, Token
from .instruction import LucyInstruction
from .environment import LucyEnvironment
from ..core.register import Register
from ..core.instructions import find_instruction
from typing import List, Dict

class LucyByteCode(object):
    def __init__(self):
        self._instructions: List[LucyInstruction] = []

    def push_instruction(self, instruction: LucyInstruction):
        self._instructions.append(instruction)
    
    def instruction_at(self, index: int) -> LucyInstruction:
        return self._instructions[index]

    @staticmethod
    def _params_to_string(params: tuple) -> str:
        string = []
        for p in params:
            if isinstance(p, Register):
                string.append(p.Name)
            else:
                if type(p) is str:
                    p = f"\"{p}\""
                string.append(str(p))
        return ", ".join(string)

    def size(self):
        return len(self._instructions)

    def asm(self) -> str:
        stringfied = ""

        for inst in self._instructions:
            stringfied += f"{inst.op_code.operation.name}   {LucyByteCode._params_to_string(inst.parameters)}\n"
        
        return stringfied

class LucyVM(object):
    def __init__(self):
        self.env: LucyEnvironment = LucyEnvironment()

    def run(self, byte_code: LucyByteCode):

        while self.env.PC.get() < byte_code.size():
            inst = byte_code.instruction_at(self.env.PC.get())
            inst.op_code.implementation(self.env, *inst.parameters)

            self.env.PC.set(self.env.PC.get() + 1)
        
        self.env.PC.set(0)
        

    def compile(self, tokens: List[Token]) -> LucyByteCode:
        program_counter = 0
        bytecode = LucyByteCode()
        checkpoints: Dict[str, int] = {}
        last_instruction = None
        params = []
        while program_counter < len(tokens):
            tkn = tokens[program_counter]

            if tkn.typ == TokenType.CHECKPOINT:
                if tkn.value not in checkpoints:
                    checkpoints[tkn.value[1:]] = bytecode.size()
                    tokens.pop(program_counter)
                    continue
            elif tkn.typ == TokenType.GOTO:
                tokens[program_counter] = Token(TokenType.DATA, checkpoints[tkn.value])
                continue
            elif tkn.typ == TokenType.INSTRUCTION:
                if last_instruction != None:
                    bytecode.push_instruction(LucyInstruction(last_instruction, tuple(params)))
                params = []
                last_instruction = find_instruction(tkn.value)
            elif tkn.typ == TokenType.DATA:
                params.append(tkn.value)
            elif tkn.typ == TokenType.REGISTER:
                params.append(self.env.registers[tkn.value.value])
            elif tkn.typ == TokenType.COMMENT:
                tokens.pop(program_counter)
                continue
        
            program_counter += 1

        if last_instruction != None:
            bytecode.push_instruction(LucyInstruction(last_instruction, tuple(params)))
        
        return bytecode
