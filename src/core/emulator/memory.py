from typing import Any, List, Dict

class Stack:
    def __init__(self):
        self._stack: List[Any] = []

    def push(self, value: Any):
        self._stack.append(value)
    
    def pop(self) -> Any:
        return self._stack.pop()

    def peek(self) -> Any:
        return self._stack[-1]

    def peek(self, index: int) -> Any:
        if index < len(self._stack):
            return self._stack[index]

        raise IndexError("Index out of range")
    
class Heap:
    MEMORY_SIZE = 0xffff
    def __init__(self):
        self._memory: List[Any] = [0] * Heap.MEMORY_SIZE
        self._memory_map: Dict[int, bool] = {}
        self._populate_memory_map()
        
    def malloc(self) -> int:
        for addr, free in self._memory_map.items():
            if free:
                self._memory_map[addr] = False
                return addr

        raise Exception("out of memory")

    def free(self, address: int) -> bool:
        if not self._memory_map[address]:
            self._memory_map[address] = True

    def _populate_memory_map(self):
        for i in range(len(self._memory)):
            self._memory_map[i] = True
        