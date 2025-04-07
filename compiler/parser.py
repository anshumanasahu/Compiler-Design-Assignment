class ASTNode: pass

class ModAdd(ASTNode):
    def __init__(self, a, b, mod):
        self.a = a
        self.b = b
        self.mod = mod

class Var(ASTNode):
    def __init__(self, value):
        self.value = value

def parse(words):
    if words[0] == "modadd":
        if len(words) != 4:
            raise ValueError("Expected format: modadd <a> <b> <mod>")
        return ModAdd(Var(words[1]), Var(words[2]), Var(words[3]))
    
    raise ValueError("Unknown instruction")
