from src.is_float import is_float
from src.get_token import get_token

def calc(expr):
    stack = []
    for tok in get_token(expr.split()): # Выражение сразу делится по пробелам в список, из которого создается уже список токенов
        if is_float(tok):
            stack.append(float(tok)) # Добавляем числа в стек
            print(f'number: {tok}')
        else: # Не число - значит оператор (токенизатор больше ничего не выдает)
            print(f'operator: {tok}')
            if stack: # Убеждаемся, что у нас есть числа в стеке для операции
                op1 = stack.pop()
            else:
                raise SyntaxError(f"No numbers for {tok} operation")
            if stack: # Убеждаемся дважды
                op2 = stack.pop()
            else:
                raise SyntaxError(f"No number for {tok} operation")

            match tok:
                case '+': # Проводим операции
                    res = op2 + op1
                case '-':
                    res = op2 - op1
                case '*':
                    res = op2 * op1
                case '**':
                    if op2 != 0 or op1 >= 0: # Проверка на то, что ноль не возводится в отрицательную степень (то же деление на 0)
                        res = op2 ** op1
                    else:
                        raise ValueError('Zero to negative power')
                case '/':
                    if op1 != 0: # Проверка деления на 0
                        res = op2 / op1
                    else:
                        raise ZeroDivisionError("Division by 0")
                case '//':
                    if op2.is_integer() and op1.is_integer() and op1 != 0: # Проверка деления на 0 и проверка операции для целых чисел по условию для //
                        res = op2 // op1
                    elif op1 != 0:
                        raise ValueError("Integers are necessary for /")
                    else:
                        raise ZeroDivisionError("Division by 0")
                case '%':
                    if op2.is_integer() and op1.is_integer() and op1 != 0: # Аналогичные проверки для %
                        res = op2 % op1
                    elif op1 != 0:
                        raise ValueError("Integers are necessary for %")
                    else:
                        raise ZeroDivisionError("Division by 0")
            stack.append(res) # Возвращаем в стек

    res = stack.pop()
    if not stack:
        print(res) # Финальный вывод, если удалось вычислить конечный результат
    else:
        raise SyntaxError(f"No operators for numbers left") # Оставшиеся числа в стеке говорят о том, что операторов не хватает для конечного вычисления
