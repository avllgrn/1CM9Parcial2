from os import system

class Monomio:
    def __init__(self, coeficiente=0.0, exponente=0) -> None:
        self.coeficiente = coeficiente
        self.exponente = exponente
        #print('Monomio construido...')

    def __del__(self):
        #print('Monomio destruido...')
        pass

    def __str__(self) -> str:
        return f'{self.coeficiente}x^{self.exponente}'

    def pideleAlUsuarioTuEstado(self):
        self.coeficiente = int(input('Dame mi coeficiente '))
        self.exponente = float(input('Dame mi exponente '))

    def muestraTuEstado(self):
        print(self)

    def __add__(self, Derecho):
        M = None
        if self.exponente == Derecho.exponente:
            M = Monomio()
            M.coeficiente = self.coeficiente + Derecho.coeficiente
            M.exponente = self.exponente
        return M

    def __sub__(self, Derecho):
        M = None
        if self.exponente == Derecho.exponente:
            M = Monomio()
            M.coeficiente = self.coeficiente - Derecho.coeficiente
            M.exponente = self.exponente
        return M

    def __mul__(self, Derecho):
        M = Monomio()
        M.coeficiente = self.coeficiente*Derecho.coeficiente
        M.exponente = self.exponente+Derecho.exponente
        return M

    def __truediv__(self, Derecho):
        M = Monomio()
        M.coeficiente = self.coeficiente/Derecho.coeficiente
        M.exponente = self.exponente-Derecho.exponente
        return M

def suma(self, Derecho):
    M = None
    if self.exponente == Derecho.exponente:
        M = Monomio()
        M.coeficiente = self.coeficiente + Derecho.coeficiente
        M.exponente = self.exponente
    return M

def resta(self, Derecho):
    M = None
    if self.exponente == Derecho.exponente:
        M = Monomio()
        M.coeficiente = self.coeficiente - Derecho.coeficiente
        M.exponente = self.exponente
    return M

def multiplica(self, Derecho):
    M = Monomio()
    M.coeficiente = self.coeficiente*Derecho.coeficiente
    M.exponente = self.exponente+Derecho.exponente
    return M

def divide(self, Derecho):
    M = Monomio()
    M.coeficiente = self.coeficiente/Derecho.coeficiente
    M.exponente = self.exponente-Derecho.exponente
    return M

if __name__ == '__main__':
    system('cls')

    M1 = Monomio()
    M2 = Monomio()
    M2 = Monomio()
    M3 = Monomio()
    M4 = Monomio()
    M5 = Monomio()
    M6 = Monomio()

    print('M1')
    M1.pideleAlUsuarioTuEstado()
    print('M2')
    M2.pideleAlUsuarioTuEstado()

    if M1.exponente == M2.exponente:
        M3.coeficiente = M1.coeficiente + M2.coeficiente
        M3.exponente = M1.exponente
    else:
        M3.coeficiente = None
        M3.exponente = None

    if M1.exponente == M2.exponente:
        M4.coeficiente = M1.coeficiente - M2.coeficiente
        M4.exponente = M1.exponente
    else:
        M4.coeficiente = None
        M4.exponente = None

    M5.coeficiente = M1.coeficiente*M2.coeficiente
    M5.exponente = M1.exponente+M2.exponente

    M6.coeficiente = M1.coeficiente/M2.coeficiente
    M6.exponente = M1.exponente-M2.exponente

    print(f'M1 = ',end='')
    M1.muestraTuEstado()
    print(f'M2 = ', end='')
    M2.muestraTuEstado()
    print(f'M3 = ', end='')
    M3.muestraTuEstado()
    print(f'M4 = ', end='')
    M4.muestraTuEstado()
    print(f'M5 = ', end='')
    M5.muestraTuEstado()
    print(f'M6 = ', end='')
    M6.muestraTuEstado()
