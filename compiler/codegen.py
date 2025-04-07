def generate(node):
    if node.__class__.__name__ == "Assign":
        return f"{node.var} = {generate(node.expr)}"
    elif node.__class__.__name__ == "Add":
        return f"({generate(node.left)} + {generate(node.right)})"
    elif node.__class__.__name__ == "Divide":
        return f"({generate(node.numerator)} / {generate(node.denominator)})"
    elif node.__class__.__name__ == "Var":
        return node.name
    else:
        raise TypeError("Unknown node type")
