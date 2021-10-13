from .register import Register

class Flag(Register):
    def __init__(self, name: str):
        super().__init__(name)

class Flags(object):
    def __init__(self):
        # Carry flag
        self.CF = Flag("CF")
        
        # Parity flag
        self.PF = Flag("PF")

        # Adjust flag
        self.AF = Flag("AF")

        # Zero flag
        self.ZF = Flag("ZF")

        # Sign flag
        self.SF = Flag("SF")
        
        # Trap flag
        self.TF = Flag("TF")
        
        # Interrupt flag
        self.IF = Flag("IF")

        # Direction flag
        self.DF = Flag("DF")

        # Overflow flag
        self.OF = Flag("OF")