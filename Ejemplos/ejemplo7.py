import os
import random

if __name__ == '__main__':
    os.system('cls')

    n = int(input('Dame n '))

    lista = [random.randrange(10) for i in range(n)]
    print(f'lista3 = {lista}')

    s = 0
    for i in range(n):
        s += lista[i]
    
    prom = s/n

    print(f's = {s}') 
    print(f'prom = {prom}') 



    menor = lista[0]
    for i in range(n):
        if lista[i] < menor:
            menor = lista[i]

    print(f'El menor es {menor}')

    mayor = lista[0]
    for i in range(n):
        if lista[i] > mayor:
            mayor = lista[i]

    print(f'El mayor es {mayor}')
