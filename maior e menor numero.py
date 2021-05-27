n1=float(input('digite um numero'))
n2=float(input('digite um numero'))
n3=float(input('digite um numero'))
if n1<n2 and n1<n3:
    menor=n1
    print('o menor numero é {}'.format(n1))
if n2<n1 and n2<n3:
    menor=n2
    print('digite o menor numero é '.format(n2))
if n3<n2 and n3<n1:
    menor= n3
    print('digite o menor numero é{}'.format(n3))

maior = n1
if n2>n1 and n2>n3:
    maior=n2
if n3>n1 and n3>n2:
    maior=n3
    print('o maior numero é {}'.format(maior))

print('adad')
