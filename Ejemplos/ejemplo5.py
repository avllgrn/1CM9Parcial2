from os import system
from math import pow

def factorial(n):
    f=1
    for i in range(1, n+1):
        f = f*i
    return f

if __name__ == '__main__':
    system('cls')
    print('Programa que calcula e^x con n términos\n\n')
    n = int(input('Dame n '))
    x = float(input('Dame x '))

    s=0
    for i in range(n+1):
        s = s + pow(x, i)/factorial(i)
        #print(i, s)

    print(f'Con for, e^{x} = {s}')

    s=0
    i=0
    while i<n+1:
        s=s + pow(x, i)/factorial(i)
        #print(i, s)
        i=i+1

    print(f'Con while, e^{x} = {s}')
