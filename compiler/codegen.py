def generate(node):
    if node.__class__.__name__ == "ModAdd":
        a = generate(node.a)
        b = generate(node.b)
        m = generate(node.mod)
        return f"(({a} % {m}) + ({b} % {m})) % {m}"
    elif node.__class__.__name__ == "Var":
        return node.value
    else:
        raise TypeError("Unknown node type")
