num= int(input('digite um numero'))
tot= 0
for c in range (1,num +1):
    if num%c==0:
        print('\033[34m',end=' ')
        tot+=1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c),end=' ')
print('o numero {} foi divisivel {} vezes'.format(num,tot))
if tot==2:
    print('e por  isso ele é primo')
else:
    print('e por isso ele não é primo')25