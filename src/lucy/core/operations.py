from .data import MutableData
from .register import Register
from .stack import Stack
from typing import Any, Union

def op_mov(target: MutableData, value: Any) -> None:
    if isinstance(value, MutableData):
        value = value.get()
    
    target.set(value)

def op_push(stack: Stack, value: Any) -> None:
    if isinstance(value, MutableData):
        value = value.get()

    stack.push(value)

def op_pop(stack: Stack, out: MutableData) -> None:
    if not isinstance(out, MutableData):
        raise Exception("Out parameter must be MutableData")
    
    return out.set(stack.pop())

def _check_arithmetics(left: MutableData, right: Union[MutableData, Any]) -> Any:
    if not isinstance(left, MutableData):
        raise Exception("wrong type for left parameter")
    
    if isinstance(right, MutableData):
        right = right.get()

    if left.get_type() != type(right):
        raise Exception("left and right parameters should be of the same type")

    return right

def op_add(left: MutableData, right: Union[MutableData, Any]):
    right = _check_arithmetics(left, right)
    left.set(left.get() + right)

def op_sub(left: MutableData, right: Union[MutableData, Any]):
    right = _check_arithmetics(left, right)
    left.set(left.get() - right)

def op_mul(left: MutableData, right: Union[MutableData, Any]):
    right = _check_arithmetics(left, right)
    left.set(left.get() * right)

def op_div(left: MutableData, right: Union[MutableData, Any]):
    right = _check_arithmetics(left, right)
    left.set(left.get() / right)

def op_mod(left: MutableData, right: Union[MutableData, Any]):
    right = _check_arithmetics(left, right)
    left.set(left.get() % right)

def op_jne(zf_flag: bool, pc: MutableData, address: Union[MutableData, int]):
    if isinstance(address, MutableData):
        address = address.get()
    
    if not zf_flag:
        pc.set(address)

def op_jmp(pc: MutableData, address: Union[MutableData, int]):
    if isinstance(address, MutableData):
        address = address.get()

    pc.set(address)