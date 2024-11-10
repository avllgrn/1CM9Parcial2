from os import system
from math import sqrt, pow

class Punto2D:

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
        #print(f'Punto2D construido')

    def __del__(self):
        #print(f'Punto2D destruido')
        pass

    def __str__(self):
        return f'({self.x}, {self.y})'

    def pideleAlUsuarioTuEstado(self):
        self.x = float(input('Dame mi x '))
        self.y = float(input('Dame mi y '))

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self,x,y):
        self.x = float(x)
        self.y = float(y)

    def guardaTuEstado(self, ArchivoSalida):
        ArchivoSalida.write(f'{self.x},{self.y}')

    def cargaTuEstado(self,ArchivoEntrada):
        datos = ArchivoEntrada.readline().split(',')
        self.x = float(datos[0])
        self.y = float(datos[1])

    def __add__(self, Derecho):
        if isinstance(Derecho, Punto2D):
            R = Punto2D()
            R.x = self.x + Derecho.x
            R.y = self.y + Derecho.y
            return R

    def __sub__(self, Derecho):
        if isinstance(Derecho, Punto2D):
            R = Punto2D()
            R.x = self.x - Derecho.x
            R.y = self.y - Derecho.y
            return R
    
def calculaPendiente(A, B):
    if type(A) == type(B) and isinstance(A, Punto2D):
        return (B.y - A.y) / (B.x - A.x)

def calculaDistancia(A, B):
    if type(A) == type(B) and isinstance(A, Punto2D):
        return sqrt(pow(B.x - A.x, 2) + pow(B.y - A.y, 2))

def suma(A, B):
    if type(A) == type(B) and isinstance(A, Punto2D):
        return A+B

def resta(A, B):
    if type(A) == type(B) and isinstance(A, Punto2D):
        return A-B


if __name__ == '__main__':
    system('cls')
    P = Punto2D()
    Q = Punto2D()
    S = Punto2D()
    R = Punto2D()

    print(f'P',end='')
    P.muestraTuEstado()
    print(f'Q',end='')
    Q.muestraTuEstado()
    print(f'P{P}')
    print(f'Q{Q}\n')

    print(f'P')
    P.pideleAlUsuarioTuEstado()
    print(f'Q')
    Q.pideleAlUsuarioTuEstado()

    d = calculaDistancia(P, Q)
    m = calculaPendiente(P, Q)
    S = suma(P, Q)
    R = resta(P, Q)

    print(f'P{P}')
    print(f'Q{Q}')
    print(f'd = {d}')
    print(f'm = {m}')
    print(f'S{S}')
    print(f'R{R}\n')
