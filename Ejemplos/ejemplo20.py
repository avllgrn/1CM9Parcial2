from os import system

class Rectangulo:
    def __init__(self, base=0.0, altura=0.0):
        self._base = float(base)
        self._altura = float(altura)
        self.verificaTuEstado()

    def __del__(self):
        pass

    def __str__(self):
        cadena = f'Base: {self._base}\n'
        cadena += f'Altura: {self._altura}\n'
        cadena += f'Área: {self.dameTuAtributoArea()}\n'
        cadena += f'Perimetro: {self.dameTuAtributoPerimetro()}\n'
        return cadena
    
    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        self._base = base
        self.verificaTuEstado()

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        self._altura = altura
        self.verificaTuEstado()

    def pideleAlUsuarioTuEstado(self):
        self._base = float(input('Dame mi base '))
        self._altura = float(input('Dame mi altura '))
        self.verificaTuEstado()

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, base, altura):
        self._base = float(base)
        self._altura = float(altura)
        self.verificaTuEstado()

    def dameTuAtributoArea(self):
        return self._base*self._altura

    def dameTuAtributoPerimetro(self):
        return 2*self._base + 2*self._altura
    
    def verificaTuEstado(self):
        if self._base<=0 or self._altura<=0:
            self._base=0
            self._altura=0

if __name__ == '__main__':
    system('cls')

    print('Se intenta construir R1 con base<0 y altura<0:')
    R1 = Rectangulo(-2, -3)
    print(f'R1\n{R1}')
    print()

    print('Se intenta R1.modificaTuEstado(-2, -3)')
    R1.modificaTuEstado(-2, -3)
    print(f'R1\n{R1}')
    print()

    print('Se intenta R1.base = -2 y R1.altura = -3')
    R1.base = -2
    R1.altura = -3
    print(f'R1\n{R1}')
    print()

    print('Ingresa base<0 y altura<0 para R1')
    R1.pideleAlUsuarioTuEstado()
    print(f'R1\n{R1}')
    print('\n\n')
    system('pause')
    system('cls')



    print('Se intenta construir R2 con base<0 y altura>0:')
    R2 = Rectangulo(-2, 3)
    print(f'R2\n{R2}')
    print()

    print('Se intenta R2.modificaTuEstado(-2, 3)')
    R2.modificaTuEstado(-2, 3)
    print(f'R2\n{R2}')
    print()

    print('Se intenta R2.base = -2 y R2.altura = 3')
    R2.base = -2
    R2.altura = 3
    print(f'R2\n{R2}')
    print()

    print('Ingresa base<0 y altura>0 para R2')
    R2.pideleAlUsuarioTuEstado()
    print(f'R2\n{R2}')
    print('\n\n')
    system('pause')
    system('cls')



    print('Se intenta construir R3 con base>0 y altura<0:')
    R3 = Rectangulo(2, -3)
    print(f'R3\n{R3}')
    print()

    print('Se intenta R3.modificaTuEstado(2, -3)')
    R3.modificaTuEstado(2, -3)
    print(f'R3\n{R3}')
    print()

    print('Se intenta R3.base = 2 y R3.altura = -3')
    R3.base = 2
    R3.altura = -3
    print(f'R3\n{R3}')
    print()

    print('Ingresa base>0 y altura<0 para R3')
    R3.pideleAlUsuarioTuEstado()
    print(f'R3\n{R3}')
    print('\n\n')
    system('pause')
    system('cls')



    print('Se intenta construir R4 con base=0 y altura>0:')
    R4 = Rectangulo(0, 3)
    print(f'R4\n{R4}')
    print()

    print('Se intenta R4.modificaTuEstado(0, 3)')
    R4.modificaTuEstado(0, 3)
    print(f'R4\n{R4}')
    print()

    print('Se intenta R4.base = 0 y R4.altura = 3')
    R4.base = 0
    R4.altura = 3
    print(f'R4\n{R4}')
    print()

    print('Ingresa base=0 y altura>0 para R4')
    R4.pideleAlUsuarioTuEstado()
    print(f'R4\n{R4}')
    print('\n\n')
    system('pause')
    system('cls')



    print('Se intenta construir R5 con base>0 y altura=0:')
    R5 = Rectangulo(2, 0)
    print(f'R5\n{R5}')
    print()

    print('Se intenta R5.modificaTuEstado(2, 0)')
    R5.modificaTuEstado(2, 0)
    print(f'R5\n{R5}')
    print()

    print('Se intenta R5.base = 2 y R5.altura = 0')
    R5.base = 2
    R5.altura = 0
    print(f'R5\n{R5}')
    print()

    print('Ingresa base>0 y altura=0 para R5')
    R5.pideleAlUsuarioTuEstado()
    print(f'R5\n{R5}')
    print('\n\n')
    system('pause')
    system('cls')



    print('Se construye R6 con base>0 y altura>0:')
    R6 = Rectangulo(2, 3)
    print(f'R6\n{R6}')
    print()

    print('Se intenta R6.modificaTuEstado(4, 5)')
    R6.modificaTuEstado(4, 5)
    print(f'R6\n{R6}')
    print()

    print('Se intenta R6.base = 6 y R6.altura = 7')
    R6.base = 6
    R6.altura = 7
    print(f'R6\n{R6}')
    print()

    print('Ingresa base>0 y altura>0 para R6')
    R6.pideleAlUsuarioTuEstado()
    print(f'R6\n{R6}')
    print('\n\n')
