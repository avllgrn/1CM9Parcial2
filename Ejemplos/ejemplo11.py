from os import system
from ejemplo10 import *

if __name__ == '__main__':
    system('cls')

    P1 = Punto2D()
    P2 = Punto2D()
    P3 = Punto2D()
    P4 = Punto2D()
    P5 = Punto2D()
    P6 = Punto2D()

    P1.pideleAlUsuarioTuEstado()
    P2.pideleAlUsuarioTuEstado()

    P3 = P1+P2
    P4 = suma(P1, P2)
    P5 = P1-P2
    P6 = resta(P1, P2)
    m = calculaPendiente(P1, P2)
    d = calculaDistancia(P1, P2)
    
    print('P1',end='')
    P1.muestraTuEstado()
    print('P2',end='')
    P2.muestraTuEstado()
    print(f'm = {m}')
    print(f'd = {d}')
    print('P1+P2 = P3',end='')
    P3.muestraTuEstado()
    print('P1+P2 = P4',end='')
    P4.muestraTuEstado()
    print('P1-P2 = P5',end='')
    P5.muestraTuEstado()
    print('P1-P2 = P6',end='')
    P6.muestraTuEstado()
