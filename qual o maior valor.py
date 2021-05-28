n1 = int (input('digite um numero inteiro'))
n2= int(input('digite outro numero'))
if n1>n2:
    print('o numero {} é maior'.format(n1))
elif n2>n1:
    print('o maior numero é o {}'.format(n2))
else:
    print('os dois numeros tem a mesmo valor')
