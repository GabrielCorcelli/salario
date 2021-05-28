num=int(input('digite um numero inteiro'))
print('''escolha umas das bases de conversao
[1] Binario
[2] Octal
[3] Hexadecimal''')
opção= int(input('sua opção'))
if opção == 1:
    print('o valor {} transformado em  binario, fica  {}'.format (num, bin(num)[2:]))
elif opção== 2:
    print('o valor{} transformado em octal fica {}'.format(num, oct(num)[2:]))
elif opção==3:
    print('o valor {} em transformado em Hexadecimal fica {}'.format(num,hex(num)[2:]))

