from .data import MutableData
from .register import Register
from .stack import Stack
from typing import Any, Union
from .flag import Flags

def op_mov(context: object, target: MutableData, value: Any) -> None:
    if isinstance(value, MutableData):
        value = value.get()
    
    target.set(value)

def op_push(context: object, value: Any) -> None:
    if isinstance(value, MutableData):
        value = value.get()

    context.Stack.push(value)

def op_pop(context: object, out: MutableData) -> None:
    if not isinstance(out, MutableData):
        raise Exception("Out parameter must be MutableData")
    
    return out.set(context.Stack.pop())

def _check_arithmetics(left: MutableData, right: Union[MutableData, Any]) -> Any:
    if not isinstance(left, MutableData):
        raise Exception("wrong type for left parameter")
    
    if isinstance(right, MutableData):
        right = right.get()

    if left.get_type() != type(right):
        raise Exception("left and right parameters should be of the same type")

    return right

def op_add(context: object, left: MutableData, right: Union[MutableData, Any]):
    right = _check_arithmetics(left, right)
    left.set(left.get() + right)

def op_sub(context: object, left: MutableData, right: Union[MutableData, Any]):
    right = _check_arithmetics(left, right)
    left.set(left.get() - right)

def op_mul(context: object, left: MutableData, right: Union[MutableData, Any]):
    right = _check_arithmetics(left, right)
    left.set(left.get() * right)

def op_div(context: object, left: MutableData, right: Union[MutableData, Any]):
    right = _check_arithmetics(left, right)
    left.set(left.get() / right)

def op_mod(context: object, left: MutableData, right: Union[MutableData, Any]):
    right = _check_arithmetics(left, right)
    left.set(left.get() % right)

def op_jne(context: object, address: Union[MutableData, int]):
    if isinstance(address, MutableData):
        address = address.get()
    
    if not context.Flags.ZF.get():
        context.PC.set(address)

def op_jmp(context: object, address: Union[MutableData, int]):
    if isinstance(address, MutableData):
        address = address.get()

    context.PC.set(address)

def op_cmp(context: object, left: MutableData, right: Any):
    if isinstance(right, MutableData):
        right = right.get()

    if not left.get_type() == type(right):
        raise Exception(f"{right} is not the same type as {left}")
    
    context.Flags.ZF.set(left.get() == right)

def op_dmp(context: object, value: Union[MutableData, Any]):
    if isinstance(value, MutableData):
        value = value.get()

    print(value)