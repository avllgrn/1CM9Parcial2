from os import system
from math import pi

class Circulo:
    def __init__(self, radio=0.0) -> None:
        self._radio = radio
        self.verificaTuEstado()

    def __del__(self) -> None:
        pass 

    @property
    def radio(self):
        return self._radio
    
    @radio.setter
    def radio(self, radio):
        self._radio = radio
        self.verificaTuEstado()
    
    def __str__(self) -> str:
        cadena = f'Radio: {self._radio}\n'
        cadena += f'Diametro: {self.dameTuAtributoDiametro()}\n'
        cadena += f'Area: {self.dameTuAtributoArea()}\n'
        cadena += f'Perimetro: {self.dameTuAtributoPerimetro()}\n'
        return cadena

    def pideleAlUsuarioTuEstado(self):
        self._radio = float(input('Dame mi radio '))
        self.verificaTuEstado()

    def muestraTuEstado(self):
        print(self)

    def dameTuAtributoDiametro(self):
        return 2*self._radio

    def dameTuAtributoArea(self):
        return pi*self._radio**2

    def dameTuAtributoPerimetro(self):
        return 2*pi*self._radio
    
    def verificaTuEstado(self):
        if self._radio < 0:
            self._radio=0
    
           
if __name__ == '__main__':
    system('cls')

    print('Se intenta construir C1 con radio negativo:')
    C1 = Circulo(-1)
    print(f'C1\n{C1}')
    print()

    C2 = Circulo()
    print('Ingresa un radio negativo para C2')
    C2.pideleAlUsuarioTuEstado()
    print(f'C2\n{C2}')
    print()

    print('Se intenta C3.radio = -1')
    C3 = Circulo()
    C3.radio = -1
    print(f'C3\n{C3}')
    print()
