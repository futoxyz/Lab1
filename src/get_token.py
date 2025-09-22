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
        try: # Корректная открывающая скобка должна: иметь два идущих после неё числа (унарные операции уже проведены), затем оператор и закрывающая скобка. При любом расхождении -> вызов ошибки
            float(tokens[tokens.index('(') + 1])
            float(tokens[tokens.index('(') + 2])
            if tokens[tokens.index('(') + 3] in OPERATORS and tokens[tokens.index('(') + 4] == ')':
                tokens.remove('(') # Верные скобки никак не влияют на выражение в RPN, поэтому удаляем
                tokens.remove(')')
            else:
                raise SyntaxError('Invalid brackets')
        except:
            raise SyntaxError('Invalid brackets')
    if ')' in tokens:
        raise SyntaxError('Invalid brackets') # После предыдущего цикла while открывающих скобок в токенах остаться не могло, значит если осталась хоть одна закрывающая скобка, то она и не открыта -> вызов ошибки
    print(tokens)
    return tokens # В списке токенов есть только числа и операторы независимо от ввода (либо была бы вызвана ошибка, либо преобразовано)
