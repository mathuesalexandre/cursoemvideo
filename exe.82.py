lista1 = []
while True:
    lista1.append(int(input('Digite um nùmero: ')))
    resp = str(input('quer continuar [S/N] '))
    if resp in 'Nn':
        break
lista2 = []
lista3 = []
for x in lista1:
    if x % 2 == 0:
        lista2.append(x)
    else:
        lista3.append(x)
print(f'A lista completa é {lista1}')
print(f'A lista de pares é {lista2}')
print(f'A lista de ímpares é {lista3}')