soma = 0
cont = 0
for x in range(1, 7):
    num= int(input('digite o {} valor: '.format(x)))
    if num % 2 == 0:
        soma += num
        cont += 1
    print('Você informou {} números PARES e a soma {}'.format(cont, soma))