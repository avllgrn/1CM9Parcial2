from os import system
from ejemplo15 import *

if __name__ == '__main__':
    system('cls')

    F1 = Fraccion()
    F2 = Fraccion()
    F3 = Fraccion()
    F4 = Fraccion()
    F5 = Fraccion()
    F6 = Fraccion()
    F7 = Fraccion()
    F8 = Fraccion()
    F9 = Fraccion()
    F10 = Fraccion()

    F1.pideleAlUsuarioTuEstado()
    F2.pideleAlUsuarioTuEstado()

    F3 = suma(F1, F2)
    F4 = F1 + F2
    F5 = resta(F1, F2)
    F6 = F1 - F2
    F7 = multiplica(F1, F2)
    F8 = F1 * F2
    F9 = divide(F1, F2)
    F10 = F1 / F2
    
    print(f'F1 = {F1}')
    print(f'F2 = {F2}')
    print(f'F1+F2 = {F3}')
    print(f'F1+F2 = {F4}')
    print(f'F1-F2 = {F5}')
    print(f'F1-F2 = {F6}')
    print(f'F1*F2 = {F7}')
    print(f'F1*F2 = {F8}')
    print(f'F1/F2 = {F9}')
    print(f'F1/F2 = {F10}')
