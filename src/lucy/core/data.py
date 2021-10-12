from typing import Any

class MutableData:
    def __init__(self):
        self._value: Any
    
    def get(self) -> Any:
        return self._value

    def set(self, new_value: Any) -> Any:
        self._value = new_value
    
    def get_type(self) -> type:
        return type(self._value)