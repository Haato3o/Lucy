from lucy.parser import LucyTokenizer, Token, LucyValidator
from lucy.vm import LucyVM


if __name__ == "__main__":
    # test = '''
    #     mov edi, 0 
    #     :loop
    #     dmp edi
    #     add edi, 1
    #     cmp edi, 10
    #     jne loop
    # '''

    # lucy = LucyTokenizer(test)
    # program = lucy()
    # validator = LucyValidator(program)
    
    # if validator.validate():
    #     print("Program is syntatically valid!")

    #     vm = LucyVM()
    #     compiled = vm.compile(program)
    #     print(compiled.asm())

    #     vm.run(compiled)

    #exit(1)
    vm = LucyVM()
    print("Lucy interpreter v1.0.0 @ Author: Haato")
    while True:
        try:
            lines = []
            stdin = input(">>> ")
            while stdin != "":
                lines.append(stdin)
                stdin = input("... ")

            tokenizer = LucyTokenizer("\n".join(lines))
            tokens = tokenizer()
            compiled = vm.compile(tokens)
            print("Compiled code to")
            print(compiled.asm())
            print("Output:")
            vm.run(compiled)
        except EOFError:
            exit(0)
        except Exception as err:
            print(err)
