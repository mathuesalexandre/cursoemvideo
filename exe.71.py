print('-'*30)
print('{:^30}' .format(' BANCO '))
print('-'*30)
valor = int(input('Qual valor você quer sacar? R$'))
cont50 = cont20 = cont10 = cont1 = 0
while True:
    while valor - 50 >= 0:
        valor -= 50
        cont50 += 1
    while valor - 20 >= 0:
        valor -= 20
        cont20 += 1
    while valor - 10 >= 0:
        valor -= 10
        cont10 += 1
    while valor - 1 >= 0:
        valor -= 1
        cont1 +=1

    if valor == 0:
        break
if cont50 != 0:
    print(f'total de {cont50} de R$50')
if cont20 != 0:
    print(f'Total de {cont20} de R$20')
if cont10 != 0:
    print(f'Total de {cont10} de R$10')
if cont1 != 0:
    print(f'Total de {cont1} de R$1')
