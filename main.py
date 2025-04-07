from compiler.compiler import compile_custom
import os

if __name__ == "__main__":
    # Ensure output folder exists
    os.makedirs("output", exist_ok=True)

    with open("examples/demo.txt") as f:
        lines = [line.strip() for line in f if line.strip()]

    all_outputs = []

    print("Generated Python Code:\n")
    for line in lines:
        compiled = compile_custom(line)
        print(f"# {line}")
        print(compiled + "\n")
        all_outputs.append(f"# {line}\n{compiled}")

    with open("output/result.py", "w") as f:
        f.write("\n\n".join(all_outputs) + "\n")
