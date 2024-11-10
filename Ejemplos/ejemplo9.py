from os import system
from math import sqrt, pow

if __name__ == '__main__':
    system('cls')

    x1 = float(input('Dame x1 '))
    y1 = float(input('Dame y1 '))

    x2 = float(input('Dame x2 '))
    y2 = float(input('Dame y2 '))

    x3 = x1+x2
    y3 = y1+y2

    x4 = x1-x2
    y4 = y1-y2

    d = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    m = (y2 - y1) / (x2 - x1)

    print(f'P1({x1}, {y1})')
    print(f'P2({x2}, {y2})')
    print(f'd = {d}')
    print(f'm = {m}')
    print(f'P3({x3}, {y3})')
    print(f'P3({x4}, {y4})')
    print(f'd = {d})')
