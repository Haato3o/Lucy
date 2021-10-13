from .data import MutableData
from enum import Enum

counter = 0
def auto():
    global counter
    tmp = counter
    counter += 1
    return tmp

class Registers(Enum):
    EAX = RAX     = auto()
    EBX = RBX     = auto()
    ECX = RCX     = auto()
    EDX = RDX     = auto()
    ESI = RSI     = auto()
    EDI = RDI     = auto()
    ESP = RSP     = auto()
    EBP = RBP     = auto()
    # Total of registers
    COUNT   = auto()

class Register(MutableData):
    def __init__(self, name: str):
        super().__init__()
        self.Name = name
        self._value = 0
        

    def __repr__(self):
        return f"<REG: {self.Name}>"