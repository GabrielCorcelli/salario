preco = float(input('\033[31mQual o preço do produto?\033[m R$ '))
print('\033[1m-=-' * 20)
print('[1] - Dinheiro/cheque: 10% de desconto.')
print('[2] - Á vista no cartão: 5% de desconto.')
print('[3] - Em até 2x vezes no cartão: Preço normal.')
print('[4] - 3x ou mais no cartão: 20% de juros ')
print('\033[1m-=-\033[m' * 20)
pagamento = float(input('\033[31mDigite o número da opção de pagamento: \033[m'))
if pagamento == 1:
    print('''Sua compra será paga á vista com 10% de desconto  
    O total da sua compra será R${:.2f}'''.format(preco * 0.9))
elif pagamento == 2:
    print('Sua compra será paga á vista com desconto de 5%')
    print('O total da compra será R${:.2f}'.format(preco * 0.95))
ar a sua compra em 2x?')
    deseja = int(input(elif pagamento == 3:
    print('Deseja parcel'''-=-==-=-=-=-=-=-=-=-=-=-=-=-=-
    [1] - SIM 
    [2] - NÃO
-=--=-=-=-=-=-=-=-=-=-=-=-=-='''))
    if deseja == 1:
        print('Sua compra será parcelada em 2x SEM JUROS')
        print('O valor das parcelas será de R${:.2f}'.format(preco/2))
    elif deseja == 2:
        print('Sua compra será paga á vista SEM JUROS')
        print('O valor a ser pago será de R${:.2f}'.format(preco))
    else:
        print('Digite uma opção disponivel!')
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas,(preco * 1.2)/parcelas))
    print('O valor a ser pago é de R${:.2f}'.format(preco * 1.2))