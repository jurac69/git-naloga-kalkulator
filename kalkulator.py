"""Študentski kalkulator z osnovnimi matematičnimi operacijami."""
import sys


def sestej(a, b):
    return a + b


def odstej(a, b):
    return a - b


def zmnozi(a, b):
    return a * b


def deli(a, b):
    if b == 0:
        raise ValueError("Deljenje z nič ni dovoljeno.")
    return a / b


def potenca(a, b):
    return a ** b


def ostanek(a, b):
    return a % b


def koren(a, b):
    return a ** (1 / b)


OPERACIJE = {"+": sestej, "-": odstej, "*": zmnozi, "/": deli, "^": potenca, "%": ostanek, "r": koren}


def main(argumenti):
    if len(argumenti) != 3:
        print("Uporaba: python3 kalkulator.py <a> <+|-|*|/|^|%> <b>")
        return 1
    a, operacija, b = argumenti
    try:
        print(OPERACIJE[operacija](float(a), float(b)))
    except ValueError as napaka:
        print(f"Napaka: {napaka}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
