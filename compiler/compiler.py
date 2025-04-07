from .lexer import tokenize
from .parser import parse
from .codegen import generate

def compile_custom(code):
    tokens = tokenize(code)
    ast = parse(tokens)
    return generate(ast)
