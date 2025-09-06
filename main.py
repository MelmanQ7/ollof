import os
from commands import run_line
from functions import define_function

if os.path.exists("program.ollof"):
    with open("program.ollof", "r", encoding="utf-8") as f:
        code_lines = f.readlines()
else:
    print("Файл program.ollof не знайдено. Введіть код вручну (exit щоб вийти):")
    code_lines = []
    while True:
        line = input("> ")
        if line.strip().lower() == "exit":
            break
        code_lines.append(line + "\n")

i = 0
while i < len(code_lines):
    line = code_lines[i].strip()
    if line.startswith(("fn ", "def ", "function ")):
        i = define_function(code_lines, i)
    else:
        run_line(line)
    i += 1
