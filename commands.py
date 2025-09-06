from runtime import variables, commands
from eval_expr import eval_expr

def command(*names):
    def wrapper(func):
        for n in names:
            commands[n] = func
        return func
    return wrapper

@command("print", "console.log", "echo", "log", "say", "speak", "out")
def cmd_print(arg):
    result = eval_expr(arg)
    print(result)

@command("let", "var")
def cmd_let(arg):
    parts = arg.split("=")
    if len(parts) == 2:
        name = parts[0].strip()
        value = eval_expr(parts[1].strip())
        variables[name] = value

def run_line(line: str):
    line = line.strip()
    if not line:
        return

    # Виклик функції
    if "(" in line and line.endswith(")"):
        name = line[:line.find("(")].strip()
        args = line[line.find("(")+1:-1].split(",")
        args = [eval_expr(a.strip()) for a in args if a.strip()]
        if name in commands:
            commands[name](",".join(str(a) for a in args))
            return
        elif name in variables:  # на випадок майбутніх об’єктів
            pass
        else:
            # Імпортуємо тут, щоб уникнути циклічного імпорту
            from functions import call_function
            call_function(name, args)
            return

    # 🔹 Присвоєння без let/var (як у Python)
    if "=" in line and not line.startswith(("let ", "var ")):
        parts = line.split("=", 1)
        name = parts[0].strip()
        value = eval_expr(parts[1].strip())
        variables[name] = value
        return

    # Стандартні команди (print x, let x=5)
    for cmd in commands:
        if line.startswith(cmd + " "):
            content = line[len(cmd):].strip()
            commands[cmd](content)
            return
