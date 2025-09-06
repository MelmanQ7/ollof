from runtime import variables

def eval_expr(expr: str):
    expr = expr.strip()
    # Підстановка змінних
    for name, value in variables.items():
        if isinstance(value, str):
            expr = expr.replace(name, f'"{value}"')
        else:
            expr = expr.replace(name, str(value))
    try:
        return eval(expr, {"__builtins__": None}, {})
    except Exception:
        return expr
