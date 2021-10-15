print('{:=^40}'.format('Lojas TombaTomba'))
preço= float(input('preço da sua compra: R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção= int(input('qual a sua opção?'))
if opção ==1:
    total = preço - (preço*10/100)
elif opção== 2:
    total= preço - (preço*5/100)
elif opção==3:
    total= preço
    parcela= total/2
    print('sua compra sera parcelada em 2x de {:.2f}'.format(parcela))
elif opção==4:
    total=preço+(preço*20/100)
    totparc= int(input('quantas parcelas?'))
    parcela = total/totparc
    print('sua compra sera parcelada em {}x de R${:.2f} com juros'.format(totparc,parcela))
print('sua compra de {:.2f} vai custar R${:.2f} no final'.format(preço, total))

