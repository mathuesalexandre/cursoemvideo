num = int(input('Digite um número: '))
tot = 0
for x in range(1, num+1):
    if num % x == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(x), end='')
print('O número {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('É por isso ele É PRIMO')
else:
    print('É por isso ele NÃO É PRIMO')
