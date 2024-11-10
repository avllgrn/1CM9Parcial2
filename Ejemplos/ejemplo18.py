from os import system
from ejemplo17 import *

if __name__ == '__main__':
    system('cls')

    M1 = Monomio()
    M2 = Monomio()
    M3 = Monomio()
    M4 = Monomio()
    M5 = Monomio()
    M6 = Monomio()
    M7 = Monomio()
    M8 = Monomio()
    M9 = Monomio()
    M10 = Monomio()

    M1.pideleAlUsuarioTuEstado()
    M2.pideleAlUsuarioTuEstado()

    M3 = suma(M1, M2)
    M4 = M1 + M2
    M5 = resta(M1, M2)
    M6 = M1 - M2
    M7 = multiplica(M1, M2)
    M8 = M1 * M2
    M9 = divide(M1, M2)
    M10 = M1 / M2
    
    print(f'M1 = {M1}')
    print(f'M2 = {M2}')
    print(f'M1+M2 = {M3}')
    print(f'M1+M2 = {M4}')
    print(f'M1-M2 = {M5}')
    print(f'M1-M2 = {M6}')
    print(f'M1*M2 = {M7}')
    print(f'M1*M2 = {M8}')
    print(f'M1/M2 = {M9}')
    print(f'M1/M2 = {M10}')
