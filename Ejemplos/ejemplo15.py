from os import system

class Fraccion:

    def __init__(self, numerador=0.0, denominador=0.0):
        self.numerador = int(numerador)
        self.denominador = int(denominador)
        #print(f"Fraccion construido")

    def __del__(self):
        #print(f"Fraccion destruido")
        pass

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def pideleAlUsuarioTuEstado(self):
        self.numerador = int(input("Dame mi numerador "))
        self.denominador = int(input("Dame mi denominador "))

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self,numerador,denominador):
        self.numerador = int(numerador)
        self.denominador = int(denominador)

    def guardaTuEstado(self, ArchivoSalida):
        ArchivoSalida.write(f'{self.numerador},{self.denominador}')

    def cargaTuEstado(self,ArchivoEntrada):
        datos = ArchivoEntrada.readline().split(',')
        self.numerador = int(datos[0])
        self.denominador = int(datos[1])

    def __add__(self, Derecho):
        if isinstance(Derecho, Fraccion):
            R = Fraccion()
            R.numerador = self.numerador*Derecho.denominador + Derecho.numerador*self.denominador
            R.denominador = self.denominador*Derecho.denominador
            return R

    def __sub__(self, Derecho):
        if isinstance(Derecho, Fraccion):
            R = Fraccion()
            R.numerador = self.numerador*Derecho.denominador - Derecho.numerador*self.denominador
            R.denominador = self.denominador*Derecho.denominador
            return R
    
    def __mul__(self, Derecho):
        if isinstance(Derecho, Fraccion):
            R = Fraccion()
            R.numerador = self.numerador * Derecho.numerador
            R.denominador = self.denominador * Derecho.denominador
            return R

    def __truediv__(self, Derecho):
        if isinstance(Derecho, Fraccion):
            R = Fraccion()
            R.numerador = self.numerador * Derecho.denominador
            R.denominador = self.denominador * Derecho.numerador
            return R
    
def suma(A, B):
    R = Fraccion()
    R.numerador = A.numerador*B.denominador + B.numerador*A.denominador
    R.denominador = A.denominador*B.denominador
    return R

def resta(A, B):
    R = Fraccion()
    R.numerador = A.numerador*B.denominador - B.numerador*A.denominador
    R.denominador = A.denominador*B.denominador
    return R

def multiplica(A, B):
    R = Fraccion()
    R.numerador = A.numerador * B.numerador
    R.denominador = A.denominador * B.denominador
    return R

def divide(A, B):
    R = Fraccion()
    R.numerador = A.numerador * B.denominador
    R.denominador = A.denominador * B.numerador
    return R

if __name__ == '__main__':
    system('cls')

    F1 = Fraccion()
    F2 = Fraccion()
    F3 = Fraccion()
    F4 = Fraccion()
    F5 = Fraccion()
    F6 = Fraccion()

    F1.pideleAlUsuarioTuEstado()
    F2.pideleAlUsuarioTuEstado()

    F3.numerador = F1.numerador*F2.denominador + F2.numerador*F1.denominador
    F3.denominador = F1.denominador*F2.denominador
    F4.numerador = F1.numerador*F2.denominador - F2.numerador*F1.denominador
    F4.denominador = F1.denominador*F2.denominador
    F5.numerador = F1.numerador * F2.numerador
    F5.denominador = F1.denominador * F2.denominador
    F6.numerador = F1.numerador * F2.denominador
    F6.denominador = F1.denominador * F2.numerador

    print(f'F1 = ',end='')
    F1.muestraTuEstado()
    print(f'F2 = ', end='')
    F2.muestraTuEstado()
    print(f'F3 = ', end='')
    F3.muestraTuEstado()
    print(f'F4 = ', end='')
    F4.muestraTuEstado()
    print(f'F5 = ', end='')
    F5.muestraTuEstado()
    print(f'F6 = ', end='')
    F6.muestraTuEstado()
