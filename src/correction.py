from src.is_float import is_float
from src.constants import ALL_TOKENS


def correction(tok):
    """
    Проверка не введенных идеально токенов (отдельно через пробел). Проверяет и наличие лишних символов
    :param tok: Отдельное выражение (либо не разделенные токены, либо содержащее лишние символы)
    :return: Правильный для обработки список токенов
    """
    for op in ALL_TOKENS:
        if op in tok:
            tok = tok.replace(op, f" {op} ")

    if ',' in tok:
        tok = tok.replace(',', '.')

    tok = tok.split()

    for part in tok:
        if not (part in ALL_TOKENS or is_float(part)):
            raise SyntaxError(f"Wrong input: {part}")
    return tok
