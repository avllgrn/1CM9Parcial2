from os import system

if __name__ == '__main__':
    system('cls')

    a = float(input('Dame a '))
    b = float(input('Dame b '))
    c = float(input('Dame c '))
    d = float(input('Dame d '))

    realSuma = a+c
    imagSuma = b+d
    realRest = a-c
    imagRest = b-d
    realMult = a*c - b*d
    imagMult = a*d + b*c
    realDivi = (a*c + b*d) / (c**2 + d**2)
    imagDivi = (b*c - a*d) / (c**2 + d**2)
    

    print(f'C1 = {a} + {b}i')
    print(f'C2 = {c} + {d}i')
    print(f'CS = {realSuma} + {imagSuma}i')
    print(f'CR = {realRest} + {imagRest}i')
    print(f'CM = {realMult} + {imagMult}i')
    print(f'CD = {realDivi} + {imagDivi}i')
    