from src.calculate import calc
from sys import stdin


def main():
    for line in stdin:
        calc(line.rstrip())


if __name__ == "__main__":
    main()
