from os import system
from ejemplo5 import *

def muestraASCII():
    for i in range(256):
        print(i, end=' ')
        print(chr(i),end=' ')
        if esCaracterEspecial(chr(i)):
            print('caracter especial')
        elif esCaracterMayuscula(chr(i)):
            print('letra mayúscula')
        elif esCaracterMinuscula(chr(i)):
            print('letra minúscula')
        else:
            print('número')

if __name__ == '__main__':
    system('cls')
    muestraASCII()
