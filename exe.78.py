valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
maior = max(valores)
menor = min(valores)
print(f'Você digitou os valores {valores}')
print(f'O maior valor foi {maior} nas posições ', end='')
for c, v in enumerate(valores):
    if v == maior:
        print(f'{c}...', end='')
print()
print(f'O menor valor foi {menor} nas posições ', end='')
for c, v in enumerate(valores):
    if v == menor:
        print(f'{c}...', end='')
print()