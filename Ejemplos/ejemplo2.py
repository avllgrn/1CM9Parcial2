from os import system

def esCaracterNumerico(c):
    ascii = ord(c)
    return ascii>=48 and ascii<=57

def esCaracterMayuscula(c):
    ascii = ord(c)
    return ascii>=65 and ascii<=90

def esCaracterMinuscula(c):
    ascii = ord(c)
    return ascii>=97 and ascii<=122

def esCaracterLetra(c):
    return esCaracterMayuscula(c) or esCaracterMinuscula(c)

def esCaracterEspecial(c):
    return not esCaracterNumerico(c) and not esCaracterLetra(c)

def tipoDeCaracter():
    caracter = input('Ingresa un solo caracter ')

    if esCaracterNumerico(caracter):
        print(f'{caracter} es numérico.')
    else:
        print(f'{caracter} no es numérico.')

    if esCaracterMayuscula(caracter):
        print(f'{caracter} es mayúscula.')
    else:
        print(f'{caracter} no es mayúscula.')

    if esCaracterMinuscula(caracter):
        print(f'{caracter} es minúscula.')
    else:
        print(f'{caracter} no es minúscula.')

    if esCaracterLetra(caracter):
        print(f'{caracter} es letra.')
    else:
        print(f'{caracter} no es letra.')

    if esCaracterEspecial(caracter):
        print(f'{caracter} es caracter especial.')
    else:
        print(f'{caracter} no es caracter especial.')


if __name__ == '__main__':
    system('cls')
    tipoDeCaracter()
