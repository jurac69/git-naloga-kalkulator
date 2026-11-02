"""Preprost kalkulator za ukazno vrstico."""
import sys


def sestej(a, b):
    return a + b


def odstej(a, b):
    return a - b


def zmnozi(a, b):
    return a * b


def deli(a, b):
    return a / b


OPERACIJE = {"+": sestej, "-": odstej, "*": zmnozi, "/": deli}


def main(argumenti):
    if len(argumenti) != 3:
        print("Uporaba: python3 kalkulator.py <a> <+|-|*|/> <b>")
        return 1
    a, operacija, b = argumenti
    print(OPERACIJE[operacija](float(a), float(b)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
