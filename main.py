from compiler.compiler import compile_custom
import os

if __name__ == "__main__":
    # Ensure output folder exists
    os.makedirs("output", exist_ok=True)

    print("Enter custom instructions (type 'done' to finish):")
    user_lines = []

    while True:
        line = input(">>> ").strip()
        if line.lower() == "done":
            break
        if line:
            user_lines.append(line)

    # Write user input to demo.txt
    with open("examples/demo.txt", "w") as f:
        for line in user_lines:
            f.write(line + "\n")

    # Read from demo.txt and compile
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
