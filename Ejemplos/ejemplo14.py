from os import system
from ejemplo13 import *

if __name__ == '__main__':
    system('cls')

    C1 = Complejo()
    C2 = Complejo()
    C3 = Complejo()
    C4 = Complejo()
    C5 = Complejo()
    C6 = Complejo()
    C7 = Complejo()
    C8 = Complejo()
    C9 = Complejo()
    C10 = Complejo()

    C1.pideleAlUsuarioTuEstado()
    C2.pideleAlUsuarioTuEstado()

    C3 = suma(C1, C2)
    C4 = C1 + C2
    C5 = resta(C1, C2)
    C6 = C1 - C2
    C7 = multiplica(C1, C2)
    C8 = C1 * C2
    C9 = divide(C1, C2)
    C10 = C1 / C2
    
    print(f'C1 = {C1}')
    print(f'C2 = {C2}')
    print(f'C1+C2 = {C3}')
    print(f'C1+C2 = {C4}')
    print(f'C1-C2 = {C5}')
    print(f'C1-C2 = {C6}')
    print(f'C1*C2 = {C7}')
    print(f'C1*C2 = {C8}')
    print(f'C1/C2 = {C9}')
    print(f'C1/C2 = {C10}')
