from .parser import ASTNode, Var, ModAdd

def generate(node):
    if isinstance(node, ModAdd):
        a = generate(node.a)
        b = generate(node.b)
        m = generate(node.mod)
        return f"result = (({a} % {m}) + ({b} % {m})) % {m}\nprint(result)"

    elif isinstance(node, Var):
        return node.value

    else:
        raise TypeError(f"Unknown node type: {type(node)}")
