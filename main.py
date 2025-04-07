from compiler.compiler import compile_custom

if __name__ == "__main__":
    with open("examples/demo.txt") as f:
        custom_code = f.read().strip()

    python_code = compile_custom(custom_code)

    print("Generated Python Code:")
    print(python_code)

    with open("output/result.py", "w") as f:
        f.write(python_code + "\n")
