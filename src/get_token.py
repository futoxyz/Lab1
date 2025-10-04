from src.is_float import is_float
from src.correction import correction
from src.constants import ALL_TOKENS


def get_token(expr):
    """
    Создает из выражения список токенов для вычисления. Список содержит лишь числа и операторы
    :param expr: Выражение
    :return: Список токенов
    """
    expr = expr.split()
    tokens = []
    for tok in expr:
        if is_float(tok) or tok in ALL_TOKENS:
            tokens.append(tok)
        else:
            tokens += correction(tok)
    while '$' in tokens:
        try:
            tokens[tokens.index('$') - 1] = float(tokens[tokens.index('$') - 1])
            tokens.remove('$')
        except:
            raise SyntaxError('Invalid "$" input')
    while '~' in tokens:
        try:
            tokens[tokens.index('~') - 1] = (-1) * float(tokens[tokens.index('~') - 1])
            tokens.remove('~')
        except:
            raise SyntaxError('Invalid "~" input')
    while '(' in tokens:
        stack = []
        for tok in tokens:
            if tok == '(':
                stack.append(tok)
                tokens.remove('(')
            if tok == ')' and stack:
                stack.pop()
                tokens.remove(')')
        if stack:
            raise SyntaxError('Invalid brackets')
    if ')' in tokens:
        raise SyntaxError('Invalid brackets')
    return tokens
