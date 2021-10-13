from enum import Enum

enum_counter = 0
def auto() -> int:
    global enum_counter
    tmp = enum_counter
    enum_counter += 1
    return tmp

class Operation(Enum):
    MOV     = auto()
    PUSH    = auto()
    POP     = auto()
    ADD     = auto()
    SUB     = auto()
    MUL     = auto()
    DIV     = auto()
    MOD     = auto()
    CMP     = auto()
    JNE     = auto()
    JMP     = auto()
    JE      = auto()
    INC     = auto()
    OR      = auto()
    AND     = auto()
    XOR     = auto()
    CALL    = auto()
    RET     = auto()
    STDOUT  = auto()
    STDIN   = auto()
    DMP     = auto()
    MALLOC  = auto()
    FREE    = auto()

operations = []