from datetime import date
atual= date.today().year
nascimento= int (input('qual a sua data de nascimento'))
idade = atual - nascimento
print('o atleta tem {} anos'.format(idade))
if idade<=9:
    print('o atleta é mirim')
elif idade<=14:
    print('o atleta é infantil')
elif idade <= 19:
    print('o atela é senior')
else:
    print('o atleta é master')
