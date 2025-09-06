from runtime import variables, functions

def define_function(lines, start_index):
    header = lines[start_index].strip()
    name_part = header.split()[1]
    func_name = name_part.split("(")[0]
    args_part = name_part[name_part.find("(")+1:name_part.find(")")]
    args = [a.strip() for a in args_part.split(",") if a.strip()]

    body = []
    i = start_index + 1
    while i < len(lines):
        line = lines[i].strip()
        if line == "}" or line.endswith("."):
            break
        body.append(lines[i])
        i += 1

    functions[func_name] = (args, body)
    return i

def call_function(name, arg_values):
    if name not in functions:
        print(f"[Ollof] Невідома функція: {name}")
        return
    args, body = functions[name]
    local_vars = dict(zip(args, arg_values))
    old_vars = variables.copy()
    variables.update(local_vars)

    from commands import run_line

    for line in body:
        run_line(line)

    variables.clear()
    variables.update(old_vars)
