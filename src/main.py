from src.calculate import calc
from sys import stdin


def main():
    """
    Запуск программы
    :return: Данная функция ничего не возвращает
    """
    for line in stdin:
        print(calc(line.rstrip()))


if __name__ == "__main__":
    main()
