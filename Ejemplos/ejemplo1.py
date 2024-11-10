from math import sqrt
from os import system

if __name__ == '__main__':
    system('cls')

    a = float(input('Ingresa a '))
    b = float(input('Ingresa b '))
    c = float(input('Ingresa c '))
    disc = pow(b,2) - 4*a*c

    if disc < 0:
        print('Error! Raíces imaginarias...')

    elif a==0:
        print('Error! Raíces indeterminadas...')

    else:
        x1 = (-b + sqrt(disc)) / (2*a)
        x2 = (-b - sqrt(disc)) / (2*a)
        print(f'a = {a}')
        print(f'b = {b}')
        print(f'c = {c}')
        print(f'x1 = {x1}')
        print(f'x2 = {x2}')

    print('\n\nFin del if-else')
