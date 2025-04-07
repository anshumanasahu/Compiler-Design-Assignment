# Compiler Design Assignment
This project is a Python-based mini-compiler that transforms human-readable arithmetic instructions using simplified custom keywords like assign, merge, and slice. It converts them into valid Python code using a modular compiler pipeline with tokenization, parsing, and code generation.

## 📥 Clone the Repository

```bash
 
 
git clone https://github.com/anshumanasahu/Compiler-Design-Assignment.git
cd Compiler-Design-Assignment
```


## 📦 Requirements
Make sure you're running **Python 3.8** or later`pip` is available. Install the required package:

```bash
pip install ttkbootstrap
```

All other modules used in the project are part of the Python standard library or part of the local `compiler/` folder.

## ▶️ Running the Compiler
Use the following command to run the compiler and transform custom instructions into Python code:
```bash
 
 
python main.py
```
This reads a line of code from examples/demo.txt and writes the equivalent Python code into output/result.py.

## 🧩 Key Features
- **Custom Arithmetic Language**: Write expressions using intuitive terms like merge, slice, and assign.

- **Simple to Extend**: Modular compiler design makes it easy to add new instructions.

- **Automatic Code Generation**: Translates your instruction into valid Python expressions.

- **Readable Output**: Compiled code is clean, direct, and Pythonic.

## 📁 Project Layout

compiler-design-assignment/
│
├── main.py                    # Entry point that  connects everything
│
├── compiler/                  # Core compilation logic
│   ├── __init__.py
│   ├── lexer.py               # Tokenizes the instruction
│   ├── parser.py              # Converts tokens into AST
│   ├── codegen.py             # Generates Python code from AST
│   └── compiler.py            # Coordinates the compile process
│
├── examples/
│   └── demo.txt               # Sample input using custom syntax
│
├── output/
│   └── result.py              # Final Python output file
│
└── README.md                  # Project overview and usage guide
Ensure all these files are present when running main.py.

## 🛠 Example Custom Instruction
Place this in examples/demo.txt:
```
assign total to merge slice 100 by 5 with slice 40 by 4
```
Then run:
```bash
python main.py
```
# The compiler will output the following in output/result.py:
```python
total = (100 / 5) + (40 / 4)
```
This performs the calculation 100 ÷ 5 + 40 ÷ 4.

## 🧪 How It Works
The process involves:

Lexical Analysis: Tokenizing the input into keywords and values.

Parsing: Constructing an abstract syntax tree (AST).

Code Generation: Turning the AST into valid Python code.

You can explore each stage in the compiler/ directory.

## 📘 Summary
This project provides a clean example of how simple compilers work, using custom arithmetic instructions as input and generating native Python code. It’s ideal for educational purposes or for building quick domain-specific compilers.

Happy compiling! 🧠💻✨
