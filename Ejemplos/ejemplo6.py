import os

if __name__ == '__main__':
    os.system('cls')

    lista = ['11', '22', '33', '44', '55']
    n = len(lista)

    print(lista, 'tiene', n, 'numeros')

    for i in range(n):
        print(i, lista[i], lista[i].upper())
    