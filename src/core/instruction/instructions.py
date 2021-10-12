from typing import List, Any
from . import Instruction
from core.data import MutableData

defaultInstructions: List[Instruction] = [
    Instruction(
        mnemonic = "NOP",
        args = ()
    ),
    Instruction(
        mnemonic = "MOV",
         args = (MutableData, Any)
    ),
    Instruction(
        mnemonic = "PUSH",
        args = (MutableData, )
    ),
    Instruction(
        mnemonic = "POP",
        args = (MutableData, )
    ),
    Instruction(
        mnemonic = "JMP",
        args = (int, )
    ),
    Instruction(
        mnemonic = "CMP",
        args = (MutableData, MutableData)
    ),
    Instruction(
        mnemonic = "ADD",
        args = (MutableData, MutableData)
    ),
    Instruction(
        mnemonic = "MUL",
        args = (MutableData, MutableData)
    ),
    Instruction(
        mnemonic = "SUB",
        args = (MutableData, MutableData)
    ),
    Instruction(
        mnemonic = "DIV",
        args = (MutableData, MutableData)
    ),
    Instruction(
        mnemonic = "DMP",
        args = (MutableData, )
    ),
    Instruction(
        mnemonic = "JNE",
        args = (int, )
    ),
    Instruction(
        mnemonic = "JE",
        args = (int, )
    ),
    Instruction(
        mnemonic = "SYS_WRITE",
        args = (MutableData, )
    ),
]


class Instructions(object):
    def __init__(self):
        self.instructions: List[Instruction] = defaultInstructions

    def find_instruction(self, mnemonic: str) -> List[Instruction]:
        instructions: List[Instruction] = []

        for ins in self.instructions:
            if ins.mnemonic == mnemonic:
                instructions.append(ins)

        return instructions

    def add_instructions(self, *args):
        for instruction in args:
            self.instructions.append(instruction)

