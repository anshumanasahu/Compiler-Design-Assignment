# check_project.py
import os

required_files = [
    "main.py",
    "README.md",
    "examples/demo.txt",
    "compiler/__init__.py",
    "compiler/lexer.py",
    "compiler/parser.py",
    "compiler/codegen.py",
    "compiler/compiler.py"
]

print("📦 Verifying Project Structure...\n")

for file in required_files:
    if not os.path.exists(file):
        print(f"Missing: {file}")
    else:
        print(f"Found: {file}")

if os.path.exists("output/result.py"):
    with open("output/result.py") as f:
        code = f.read().strip()
    if code == "x = (a / b) + (c / d)":
        print("\nOutput looks correct!")
    else:
        print("\nOutput file found but content may be wrong:")
        print(code)
else:
    print("\noutput/result.py not found. Run `python main.py` to generate it.")
