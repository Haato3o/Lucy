from typing import Any, List

class Stack:
    def __init__(self):
        self._stack: List[Any] = []

    def push(self, value: Any):
        self._stack.append(value)

    def pop(self) -> Any:
        return self._stack.pop()
    
    def peek(self) -> Any:
        if len(self._stack) > 0:
            return self._stack[-1]
        
        return None

    def as_list(self) -> List[Any]:
        return self._stack

    def size(self) -> int:
        return len(self._stack)

    def __repr__(self):
        return str(self._stack)