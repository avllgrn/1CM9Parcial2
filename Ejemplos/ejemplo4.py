from os import system
from ejemplo5 import *

def cuentaTiposDeCaracteres():
    cadena  = input('Ingresa tu cadena ')
    n = len(cadena)

    nNumeros = 0
    nMinusculas = 0
    nMayusculas = 0
    nEspeciales = 0
    for i in range(n):
        if esCaracterEspecial(cadena[i]):
            nEspeciales = nEspeciales+1
        elif esCaracterMayuscula(cadena[i]):
            nMayusculas = nMayusculas+1
        elif esCaracterMinuscula(cadena[i]):
            nMinusculas = nMinusculas+1
        else:
            nNumeros = nNumeros+1

    print(f'Tiene {n} caracteres')
    print(f'Tiene {nNumeros} números')
    print(f'Tiene {nMinusculas} minúsculas')
    print(f'Tiene {nMayusculas} mayúsculas')
    print(f'Tiene {nEspeciales} especiales')

if __name__ == '__main__':
    system('cls')
    cuentaTiposDeCaracteres()
