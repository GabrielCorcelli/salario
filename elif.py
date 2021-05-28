casa = float(input('Qual o valor da casa?:'))
salario = float(input('qual seu salario'))
anos= int(input('em quantos anos vc quer pagar?:'))
prestacao=casa/(anos*12)
minimo= salario * 30/100
print('para pagar uma casa de {} em {} anos '.format(casa,anos))
print('voce tera que pagar {:.2f} por mes'.format(prestacao))
print('o minimo de dinheiro para pagar a prestacao é {:.2f}'.format(prestacao))
if prestacao<= minimo:
    print('o emprestimo pode ser concedido')
else:
    print('o voce nao pode comprar essa casa pois voce é pobre')