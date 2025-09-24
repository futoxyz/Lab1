from src.is_float import is_float
from src.correction import correction
from src.constants import OPERATORS, UNARY, BRACKETS


def get_token(expr): # Создание списка токенов
    tokens = []
    for tok in expr:
        if is_float(tok) or tok in OPERATORS or tok in UNARY or tok in BRACKETS:
            tokens.append(tok) # Добавляем в список токенов (будущий стек) всё, что на вводе было указано верно: числа, операторы, унарные знаки, скобки
        else:
            tokens += correction(tok) # Всё, что не указано идеально идёт на исправление
    while '$' in tokens:
        try:
            tokens[tokens.index('$') - 1] = float(tokens[tokens.index('$') - 1]) # Применяем унарный + сразу в токенизаторе
            tokens.remove('$')
        except:
            raise SyntaxError('Invalid "$" input')
    while '~' in tokens:
        try:
            tokens[tokens.index('~') - 1] = (-1) * float(tokens[tokens.index('~') - 1]) # Применяем унарный - сразу в токенизаторе
            tokens.remove('~')
        except:
            raise SyntaxError('Invalid "~" input')
    while '(' in tokens:
        stack = []
        for tok in tokens: # Проверка закрытия каждой скобки при наличии
            if tok == '(':
                stack.append(tok) # Открывающая скобка добавляется в стек
                tokens.remove('(')
            if tok == ')' and stack:
                stack.pop() # Закрывающая скобка вытаскивает скобку из стека
                tokens.remove(')')
        if stack:
            raise SyntaxError('Invalid brackets') # Если стек не остался пустым - есть незакрытые скобки
    if ')' in tokens:
        raise SyntaxError('Invalid brackets') # Предыдущий цикл гарантированно удаляет все открывающиеся скобки (или выдает ошибку), поэтому доп. проверка на закрывающиеся
    print(tokens)
    return tokens # В списке токенов есть только числа и операторы независимо от ввода (либо была бы вызвана ошибка, либо преобразовано)
