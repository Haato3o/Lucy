from typing import List, Any

class MutableData:
    def __init__(self):
        self.value: List[Any] = [0]

    def get_value(self) -> Any:
        return self.value[0]

    def set_value(self, new_value: Any):
        self.value[0] = new_value