nota1=int(input('digite sua primeira nota'))
nota2=int(input('digite sua segunda nota'))
media= (nota1+nota2)/2
if media>=9:
    print('parabens voce passou de etapa')
elif media>=9:
    print('voce nao passou dessa etapa porem voce ainda tem outra chance')
elif media==8:
    print('deu 8')
else:
    print('voce foi eliminado do campeonato')