from dataclasses import dataclass

@dataclass
class Instruction:
    mnemonic: str
    args: tuple