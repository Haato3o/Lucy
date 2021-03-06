from enum import Enum
from dataclasses import dataclass
from typing import List, Any, Dict, Union, Callable
from .data import MutableData
from .operations import *
from .instruction import Instruction
from .operation import Operation

_operations: List[Instruction] = [
    # mov   reg, reg
    Instruction(
        operation = Operation.MOV,
        signature = (MutableData, MutableData),
        implementation = op_mov
    ),
    # mov   reg, value
    Instruction(
        operation = Operation.MOV,
        signature = (MutableData, Any),
        implementation = op_mov
    ),
    # push  reg
    Instruction(
        operation = Operation.PUSH,
        signature = (MutableData, ),
        implementation = op_push
    ),
    # push  value
    Instruction(
        operation = Operation.PUSH,
        signature = (Any, ),
        implementation = op_push
    ),
    # pop  value
    Instruction(
        operation = Operation.POP,
        signature = (MutableData, ),
        implementation = op_pop
    ),
    # add  reg, value
    Instruction(
        operation = Operation.ADD,
        signature = (MutableData, Any),
        implementation = op_add
    ),
    # add  reg, reg (both regs must carry the same value type)
    Instruction(
        operation = Operation.ADD,
        signature = (MutableData, MutableData),
        implementation = op_add
    ),
    # sub  reg, value
    Instruction(
        operation = Operation.SUB,
        signature = (MutableData, Any),
        implementation = op_sub
    ),
    # sub  reg, reg (both regs must carry the same value type)
    Instruction(
        operation = Operation.SUB,
        signature = (MutableData, MutableData),
        implementation = op_sub
    ),
    # mul  reg, value
    Instruction(
        operation = Operation.MUL,
        signature = (MutableData, Any),
        implementation = op_mul
    ),
    # mul  reg, reg (both regs must carry the same value type)
    Instruction(
        operation = Operation.MUL,
        signature = (MutableData, MutableData),
        implementation = op_mul
    ),
    # div  reg, value
    Instruction(
        operation = Operation.DIV,
        signature = (MutableData, Any),
        implementation = op_div
    ),
    # div  reg, reg (both regs must carry the same value type)
    Instruction(
        operation = Operation.DIV,
        signature = (MutableData, MutableData),
        implementation = op_div
    ),
    # mod  reg, value
    Instruction(
        operation = Operation.MOD,
        signature = (MutableData, Any),
        implementation = op_mod
    ),
    # mod  reg, reg (both regs must carry the same value type)
    Instruction(
        operation = Operation.MOD,
        signature = (MutableData, MutableData),
        implementation = op_mod
    ),
    Instruction(
        operation = Operation.CMP,
        signature = (MutableData, Any),
        implementation = op_cmp
    ),
    # jne  reg
    Instruction(
        operation = Operation.JNE,
        signature = (MutableData, ),
        implementation = op_jne
    ),
    # jne   address
    Instruction(
        operation = Operation.JNE,
        signature = (int, ),
        implementation = op_jne
    ),
    # jmp   reg
    Instruction(
        operation = Operation.JMP,
        signature = (MutableData, ),
        implementation = op_jmp
    ),
    # jmp   address
    Instruction(
        operation = Operation.JMP,
        signature = (int, ),
        implementation = op_jmp
    ),
    # dmp   reg
    Instruction(
        operation = Operation.DMP,
        signature = (MutableData, ),
        implementation = op_dmp
    ),
    # dmp   value
    Instruction(
        operation = Operation.DMP,
        signature = (Any, ),
        implementation = op_dmp
    ),
] 

def _build_operations_cache() -> Dict[Operation, List[Instruction]]:
    global _operations

    ops = {}

    for op in _operations:
        if op.operation not in ops:
            ops[op.operation] = [op]
        else:
            ops[op.operation].append(op)

    return ops

operations = _build_operations_cache()

def is_instruction_implemented(op_code: Operation) -> bool:
    return op_code in operations

def find_instruction(op_code: Operation) -> Instruction:
    if not is_instruction_implemented(op_code):
        raise Exception(f"operation {op_code} not implemented")
        
    return operations[op_code][0]

def calculate_max_params(op_code: Operation) -> int:
    n_params = 0

    for op in operations[op_code]:
        if op.operation == op_code:
            n_params = max(n_params, len(op.signature))
    
    return n_params

def validate_params(op_code: Operation, params_type: tuple) -> bool:
    
    for op_metadata in operations[op_code]:
        if len(op_metadata.signature) < len(params_type):
            return False
        
        if op_metadata.signature == params_type:
            return True
    
    return False