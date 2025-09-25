from src.is_float import is_float
from src.correction import correction
from src.constants import OPERATORS, UNARY, BRACKETS


def get_token(expr):
    """
    Создает из выражения список токенов для вычисления. Список содержит лишь числа и операторы
    :param expr: Выражение
    :return: Список токенов
    """
    tokens = []
    for tok in expr:
        if is_float(tok) or tok in OPERATORS or tok in UNARY or tok in BRACKETS:
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
