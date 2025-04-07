class ASTNode: pass

class Assign(ASTNode):
    def __init__(self, var, expr): self.var, self.expr = var, expr

class Add(ASTNode):
    def __init__(self, left, right): self.left, self.right = left, right

class Divide(ASTNode):
    def __init__(self, numerator, denominator):
        self.numerator, self.denominator = numerator, denominator

class Var(ASTNode):
    def __init__(self, name): self.name = name

def parse(words):
    if words[0] != "assign" or words[3] != "merge":
        raise ValueError("Invalid syntax")

    var_name = words[1]

    if words[4] != "slice" or words[6] != "by":
        raise ValueError("First divide must be 'slice <a> by <b>'")
    left = Divide(Var(words[5]), Var(words[7]))

    if words[8] != "with" or words[9] != "slice" or words[11] != "by":
        raise ValueError("Second divide must be 'slice <c> by <d>'")
    right = Divide(Var(words[10]), Var(words[12]))

    return Assign(var_name, Add(left, right))
