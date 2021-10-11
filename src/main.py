from core.emulator import CPU
from sys import argv

if __name__ == "__main__":
    processor = CPU()

    file = argv[1]

    with open(file, "r") as f:
        program = f.read()
    # liv = f'''
    #     push {0x0A}
    #     push {0x75}
    #     push {0x6F}
    #     push {0x79}
    #     push {0x20}
    #     push {0x65}
    #     push {0x76}
    #     push {0x6F}
    #     push {0x6C}
    #     push {0x20}
    #     push {0x49}
    #     mov ecx, 0
    #     pop eax
    #     sys_write eax
    #     add ecx, 1
    #     cmp ecx, 11
    #     jne 25
    # '''

    # program = '''
    #             mov eax, 34
    #             mov edx, 35
    #             add eax, edx
    #             cmp eax, 69
    #             jne 16
    #             dmp eax
    #             nop
    #         '''
            
    compiled = processor.compile(program)
    processor.run(compiled)