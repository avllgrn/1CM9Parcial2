import os

class Complejo:
    def __init__(self, real=0.0, imaginario=0.0) -> None:
        self.real = real
        self.imaginario = imaginario
        #print('Complejo construido...')

    def __del__(self):
        #print('Complejo destruido...')
        pass

    def __str__(self) -> str:
        if self.imaginario < 0:
            cadena = f'{self.real}{self.imaginario}i'
        else:
            cadena = f'{self.real}+{self.imaginario}i'
        return cadena

    def muestraTuEstado(self):
        print(self)

    def pideleAlUsuarioTuEstado(self):
        self.real = float(input('Dame mi real '))
        self.imaginario = float(input('Dame mi imaginario '))

    def __add__(self, Derecho):
        CR = Complejo()
        CR.real = self.real + Derecho.real
        CR.imaginario = self.imaginario + Derecho.imaginario
        return CR

    def __sub__(self, Derecho):
        CR = Complejo()
        CR.real = self.real - Derecho.real
        CR.imaginario = self.imaginario - Derecho.imaginario
        return CR

    def __mul__(self, Derecho):
        CR = Complejo()
        CR.real = self.real*Derecho.real - self.imaginario*Derecho.imaginario
        CR.imaginario = self.real*Derecho.imaginario + Derecho.real*self.imaginario
        return CR

    def __truediv__(self, Derecho):
        CR = Complejo()
        CR.real = (self.real*Derecho.real + self.imaginario*Derecho.imaginario) / (Derecho.real**2 + Derecho.imaginario**2)
        CR.imaginario = (Derecho.real*self.imaginario - self.real*Derecho.imaginario) / (Derecho.real**2 + Derecho.imaginario**2)
        return CR

def suma(C1, C2):
    R = Complejo()
    R.real = C1.real + C2.real
    R.imaginario = C1.imaginario + C2.imaginario
    return R

def resta(C1, C2):
    R = Complejo()
    R.real = C1.real - C2.real
    R.imaginario = C1.imaginario - C2.imaginario
    return R

def multiplica(C1, C2):
    R = Complejo()
    R.real = C1.real*C2.real - C1.imaginario*C2.imaginario
    R.imaginario = C1.real*C2.imaginario + C2.real*C1.imaginario
    return R

def divide(C1, C2):
    R = Complejo()
    R.real = (C1.real*C2.real + C1.imaginario*C2.imaginario) / (C2.real**2 + C2.imaginario**2)
    R.imaginario = (C2.real*C1.imaginario - C1.real*C2.imaginario) / (C2.real**2 + C2.imaginario**2)
    return R


if __name__ == '__main__':
    os.system('cls')

    C1 = Complejo()
    C2 = Complejo()
    C3 = Complejo()
    C4 = Complejo()
    C5 = Complejo()
    C6 = Complejo()

    C1.pideleAlUsuarioTuEstado()
    C2.pideleAlUsuarioTuEstado()

    C3.real = C1.real + C2.real
    C3.imaginario = C1.imaginario + C2.imaginario
    C4.real = C1.real - C2.real
    C4.imaginario = C1.imaginario - C2.imaginario
    C5.real = C1.real*C2.real - C1.imaginario*C2.imaginario
    C5.imaginario = C1.real*C2.imaginario + C1.imaginario*C2.real
    C6.real = (C1.real*C2.real + C1.imaginario*C2.imaginario) / (C2.real**2 + C2.imaginario**2)
    C6.imaginario = (C2.real*C1.imaginario - C1.real*C2.imaginario) / (C2.real**2 + C2.imaginario**2)

    print(f'C1 = ',end='')
    C1.muestraTuEstado()
    print(f'C2 = ', end='')
    C2.muestraTuEstado()
    print(f'C3 = ', end='')
    C3.muestraTuEstado()
    print(f'C4 = ', end='')
    C4.muestraTuEstado()
    print(f'C5 = ', end='')
    C5.muestraTuEstado()
    print(f'C6 = ', end='')
    C6.muestraTuEstado()
