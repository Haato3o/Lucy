from core.parser.asm import ASMParser
from lucy.parser import LucyTokenizer, Token, LucyValidator


if __name__ == "__main__":
    test = '''
        mov eax, "string here"
        mov edi, 0x10
        :loop
        jmp non_existent
    '''

    lucy = LucyTokenizer(test)
    program = lucy()

    validator = LucyValidator(program)
    if validator.validate():
        print("Program is syntatically valid!")