from ..instruction import Instruction
from typing import List

class Instructions:

    _defaultInstructions: List[Instruction] = [
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
        )
    ]

    @staticmethod
    def find_instruction(mnemonic: str) -> List[Instruction]:
        instructions: List[Instruction] = []
        
        for instruction in Instructions._defaultInstructions:
            if instruction.mnemonic == mnemonic:
                instructions.append(instruction)

        if len(instructions) == 0:
            raise Exception(f"No instruction found with name {mnemonic}")

        return instructions