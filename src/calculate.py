from src.is_float import is_float
from src.get_token import get_token

def calc(expr):
    """
    Вычисляет введённое выражение
    :param expr: Выражение в RPN
    :return: Результат вычисления
    """
    stack = []
    for tok in get_token(expr.split()):
        if is_float(tok):
            stack.append(float(tok))
        else:
            if stack:
                op1 = stack.pop()
            else:
                raise SyntaxError(f"No numbers for {tok} operation")
            if stack:
                op2 = stack.pop()
            else:
                raise SyntaxError(f"No number for {tok} operation")

            match tok:
                case '+':
                    res = op2 + op1
                case '-':
                    res = op2 - op1
                case '*':
                    res = op2 * op1
                case '**':
                    if op2 < 0 and not op1.is_integer():
                        raise ValueError(f'Cannot get negative number in float power for real numbers ({op2} to {op1} power)')
                    elif op2 == 0 and op1 < 0:
                        raise ValueError(f'Cannot raise zero in negative power ({op1})')
                    else:
                        res = op2 ** op1
                case '/':
                    if op1 != 0:
                        res = op2 / op1
                    else:
                        raise ZeroDivisionError("Division by 0")
                case '//':
                    if op2.is_integer() and op1.is_integer() and op1 != 0:
                        res = op2 // op1
                    elif op1 != 0:
                        raise ValueError("Integers are necessary for /")
                    else:
                        raise ZeroDivisionError("Division by 0")
                case '%':
                    if op2.is_integer() and op1.is_integer() and op1 != 0:
                        res = op2 % op1
                    elif op1 != 0:
                        raise ValueError("Integers are necessary for %")
                    else:
                        raise ZeroDivisionError("Division by 0")
            stack.append(res)

    res = stack.pop()
    if not stack:
        return res
    else:
        raise SyntaxError(f"No operators for numbers left")
