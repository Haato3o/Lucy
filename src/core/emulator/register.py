from core.data import MutableData

class Register(MutableData):
    def __init__(self, name: str):
        super().__init__()
        self.Name = name

    def __repr__(self):
        return self.Name
    