from src.is_float import is_float
from src.constants import OPERATORS


def correction(tok):
    """
    Проверка не введенных идеально токенов (отдельно через пробел). Проверяет и наличие лишних символов
    :param tok: Отдельное выражение (либо не разделенные токены, либо содержащее лишние символы)
    :return: Правильный для обработки список токенов
    """
    for op in OPERATORS:
        if op in tok:
            tok = tok.replace(op, f" {op} ")

    if ',' in tok:
        tok = tok.replace(',', '.')

    tok = tok.split()

    for part in tok:
        if not (part in OPERATORS or is_float(part)):
            raise SyntaxError(f"Wrong input: {part}")
    return tok
