import os
import random

def muestraLista(lista):
    n = len(lista)

    for i in range(n):
        print(f'[{i}] = {lista[ i ]}')


def copiaLista(lista):
    n = len(lista)

    copia = []

    for i in range(n):
        copia.append(lista[ i ])

    return copia

if __name__ == '__main__':
    os.system('cls')

    cadena = 'politecnico'
    print(cadena)
    
    for i in range(len(cadena)):
        print(i, cadena[i])

    cadena[5] = 'P'

    print(cadena)
