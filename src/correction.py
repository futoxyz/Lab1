from src.is_float import is_float
from src.constants import OPERATORS, UNARY, BRACKETS


def correction(tok):
    if '(' in tok: # В циклах ниже ищем "склеившиеся" операторы и знаки
        tok = tok.replace('(', ' ( ')
    if ')' in tok:
        tok = tok.replace(')', ' ) ')
    if '**' in tok:
        tok = tok.replace('**', ' ** ')
    if '~' in tok:
        tok = tok.replace('~', ' ~ ')
    if '$' in tok:
        tok = tok.replace('$', ' $ ')
    if '*' in tok and '**' not in tok:
        tok = tok.replace('*', ' * ')
    if '//' in tok:
        tok = tok.replace('//', ' // ')
    if '/' in tok and '//' not in tok:
        tok = tok.replace('/', ' / ')
    if '+' in tok:
        tok = tok.replace('+', ' + ')
    if '-' in tok:
        tok = tok.replace('-', ' - ')
    if '%' in tok:
        tok = tok.replace('%', ' % ')
    tok = tok.split()
    for part in tok:
        if not (part in OPERATORS  or part in UNARY or part in BRACKETS or is_float(part)):
            raise SyntaxError(f"Wrong input: {part}") # Наличие лишних символов
    return tok
