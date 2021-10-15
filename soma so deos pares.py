soma=0
contador=0
for c in range(1,100):
    num=int(input('digite o {} o valor'.format(c)))
    if num % 2 == 0:
        soma=soma+ num
        contador=contador+1
print('voce informou {} pares 1 e  a soma foi {}'.format(contador, soma))

