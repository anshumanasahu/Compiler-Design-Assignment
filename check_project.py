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
        print(f"❌ Missing: {file}")
    else:
        print(f"✅ Found: {file}")

print("\n🔍 Checking Output...")

expected_snippet = "((17 % 10) + (29 % 10)) % 10"

output_path = "output/result.py"
if os.path.exists(output_path):
    with open(output_path) as f:
        code = f.read().strip()
    if expected_snippet in code:
        print("✅ Output looks correct for modadd!")
    else:
        print("⚠️ Output found but may be incorrect:")
        print(code)
else:
    print("❌ output/result.py not found. Run `python main.py` to generate it.")
