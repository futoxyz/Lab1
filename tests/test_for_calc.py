import pytest
from src.calculate import calc


def calc_test():
    """
    Проверяет вычисления при описанных в README характеристиках
    :return: Данная функция ничего не возвращает
    """
    assert calc("1 2 +") == 3
    assert calc("1 2 3 + +") == 6
    assert calc("1 2 3+ +") == 6
    assert calc("1 2 3++") == 6
    assert calc("1 $ 2 ~ +") == -1
    assert calc("1$2~+") == -1
    assert calc("+1 -2 +") == -1
    assert calc("0.5 0,3 .2 + + 1. -") == 0
    assert calc("(1 2 +)") == 3
    assert calc("(1 2) +") == 3
    assert calc("(1 2) 3 * +") == 7
    assert calc("2 4 *") == 8
    assert calc("4 2 /") == 2
    assert calc("7 3 %") == 1
    assert calc("7 3 //") == 2
    assert calc("1 160 2 / + 0.5 **") == 9

    with pytest.raises(ZeroDivisionError):
        calc("1 0 /")
    with pytest.raises(ZeroDivisionError):
        calc("1 0 //")
    with pytest.raises(ZeroDivisionError):
        calc("1 0 %")
    with pytest.raises(SyntaxError):
        calc("1 @f 2 +")
    with pytest.raises(SyntaxError):
        calc("3 3")
    with pytest.raises(SyntaxError):
        calc("1 2 3 +")
    with pytest.raises(SyntaxError):
        calc("1 2 3 + - *")
    with pytest.raises(SyntaxError):
        calc("5 * 2")
    with pytest.raises(SyntaxError):
        calc("~5 2 +")
    with pytest.raises(SyntaxError):
        calc("(3 2 +")
    with pytest.raises(SyntaxError):
        calc("3 2 +)")
    with pytest.raises(ValueError):
        calc("1 ~ 0.5 **")
    with pytest.raises(ValueError):
        calc("0 1 ~ **")
    with pytest.raises(ValueError):
        calc("2.5 1.5 //")
    with pytest.raises(ValueError):
        calc("2.5 1.5 %")

