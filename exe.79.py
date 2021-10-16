lista = list()
while True:
    n = int(input('Digite um numero: '))
    if n not in lista:
        lista.append(n)
        print('número adicionado com sucesso')
    else:
        print('número repitido! Não sera adicionado.')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
lista.sort()
print(f'{lista}')
