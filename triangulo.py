r1=float(input('digite o valor da primeira reta:'))
r2=float(input('digite o valor da segunda reta:'))
r3=float(input('digite o valor da terceira reta:'))
if r1< r2 + r3 and r2< r1 + r3 and r3 <r1 + r2:
    print('os segmentos acima pode formar triangulo ',end='')
    if r1 == r2 == r3:
        print('Equilatero')
    elif r1!=r2!=r3!=r1:
        print('escaleno')
    else:
        print('isosceles')
else:
    print('nao pode formar um triangulo')