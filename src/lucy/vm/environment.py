from ..core.register import Register, Registers
from ..core.flag import Flags
from ..core.stack import Stack
from typing import List

class LucyEnvironment(object):
    def __init__(self):
        self.registers: List[Register] = []
        
        self.PC: Register = Register("PC")
        self.Flags: Flags = Flags()
        self.Stack: Stack = Stack()
        self._initialize_registers()

    def _initialize_registers(self):
        for reg in Registers:
            self.registers.append(Register(reg.name))