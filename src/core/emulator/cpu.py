from core.data import MutableData
from core.instruction import Instruction, Instructions
from .register import Register
from .memory import Stack, Heap
from .flag import Flags
import sys
from typing import List, Any, Tuple
from time import time_ns
import re

class CPU:
    def __init__(self):
        self.EAX: Register = Register("EAX")
        self.EBX: Register = Register("EBX")
        self.ECX: Register = Register("ECX")
        self.EDX: Register = Register("EDX")
        self.ESI: Register = Register("ESI")
        self.EDI: Register = Register("EDI")
        self.ESP: Register = Register("ESP")
        self.EBP: Register = Register("EBP")

        self.Stack: Stack = Stack()
        self.Heap: Heap = Heap()

        # Program counter
        self.PC = 0

        self.Flags: Flags = Flags()
        self._instructions: Instructions = Instructions()

    def run(self, program: List[Any]):

        start = time_ns()
        print("==== STARTED EMULATING ASSEMBLY ====\n")
        
        self._emulate_program(program)

        end = time_ns()

        print("\n==== FINISHED EMULATING ASSEMBLY ====")
        print(f"Time taken: {(end - start) / 1000}μs")

    def compile(self, program: str) -> List[Any]:
        registers = {
            "EAX": self.EAX,
            "EBX": self.EBX,
            "ECX": self.ECX,
            "EDX": self.EDX,
            "ESI": self.ESI,
            "EDI": self.EDI,
            "ESP": self.ESP,
            "EBP": self.EBP
        }
        parsed: List[Any] = []
        splitted = re.split(" |\n", program.upper())
        
        for step in splitted:
            step = step.strip("\n,")
            
            if len(step) == 0:
                continue

            if step not in registers:
                parsed.append(self._parse_arg(step))
            else:
                parsed.append(registers[step])
        print(parsed)
        return parsed

    def _parse_arg(self, arg: str):
        if arg.isnumeric():
            return int(arg)
        if arg.startswith("0x") or arg.startswith("0X"):
            return int(arg, 16)
        else:
            return arg

    def _emulate_program(self, program: List[Any]):
        while self.PC < len(program):
            instruction_mnemonic: str = program[self.PC]
            instruction_info = self._instructions.find_instruction(instruction_mnemonic)[0]
            instruction_params: Tuple[Any] = tuple(program[self.PC + 1: self.PC + 1 + len(instruction_info.args)])
            self._interpret_instruction(instruction_info, *instruction_params)
 
    def _interpret_instruction(self, instruction: Instruction, *args):
        if len(args) < len(instruction.args):
            raise Exception(f"wrong number of parameters for instruction: {instruction.mnemonic}")

        params = args[0: len(instruction.args)]

        #print(f"Executing {instruction.mnemonic} with {params}")

        if instruction.mnemonic == "NOP":
            self._nop()
        elif instruction.mnemonic == "MOV":
            self._mov(*params)
        elif instruction.mnemonic == "PUSH":
            self._push(*params)
        elif instruction.mnemonic == "POP":
            self._pop(*params)
        elif instruction.mnemonic == "JMP":
            self._jmp(*params)
        elif instruction.mnemonic == "JNE":
            self._jne(*params)
        elif instruction.mnemonic == "JE":
            self._je(*params)
        elif instruction.mnemonic == "CMP":
            self._cmp(*params)
        elif instruction.mnemonic == "ADD":
            self._add(*params)
        elif instruction.mnemonic == "DMP":
            self._dmp(*params)
        elif instruction.mnemonic == "SYS_WRITE":
            self._sys_write(*params)
        else:
            raise Exception(f"Not implemented: {instruction.mnemonic}")
        
        self.PC += len(instruction.args) + 1

    def _nop(self):
        return

    def _mov_mut(self, target: MutableData, value: MutableData):
        target.set_value(value.get_value())

    def _mov(self, target: MutableData, value: Any):
        target.set_value(value)

    def _push(self, value: Any):
        self.Stack.push(value)

    def _pop(self, target: MutableData):
        target.set_value(self.Stack.pop())
    
    def _jmp(self, location: Any):
        if location is Register:
            location = location.get_value()

        self.PC = location - 2

    def _jne(self, location: Any):
        if isinstance(location, MutableData):
            location = location.get_value()
        
        if not self.Flags.ZF:
            self.PC = location - 2
    
    def _je(self, location: Any):
        if location is Register:
            location = location.get_value()
        
        if self.Flags.ZF:
            self.PC = location - 2

    def _cmp(self, left: MutableData, right: Any):
        if isinstance(right, MutableData):
            right = right.get_value()

        if left.get_value() == right:
            self.Flags.ZF = 1
            return

        self.Flags.ZF = 0

    def _add(self, left: MutableData, right: Any):
        if isinstance(right, MutableData):
            right = right.get_value()

        left.set_value(
            left.get_value() + right
        )

    def _mul(self, left: MutableData, right: Any):
        left.set_value(
            left.get_value() * right.get_value()
        )
    
    def _sub(self, left: MutableData, right: Any):
        left.set_value(
            left.get_value() - right.get_value()
        )
    
    def _div(self, left: MutableData, right: Any):
        left.set_value(
            left.get_value() / right.get_value()
        )

    def _dmp(self, value: MutableData):
        print(value.get_value())

    def _sys_write(self, value: MutableData):
        val = value.get_value()
        if type(val) == int and 0 < val < 0xFF:
            val = chr(val)

        sys.stdout.write(val)
    
