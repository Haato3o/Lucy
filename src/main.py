from core.emulator import CPU
from sys import argv

if __name__ == "__main__":
    processor = CPU()

    if len(argv) < 2:
        print("ERROR: .asm file path must be specified!")
        exit(1)

    file = argv[1]

    if not file.endswith(".asm"):
        print("ERROR: file is not an .asm file!")
        exit(1)


    with open(file, "r") as f:
        program = f.read()
            
    compiled = processor.compile(program)
    processor.run(compiled)