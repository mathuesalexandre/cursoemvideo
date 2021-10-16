total = mais = menor = cont = barato = 0
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('preço: R$'))
    cont += 1
    resp = ' '
    total += preço
    if preço > 1000:
        mais += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    while resp not in 'SN':
        resp = str(input('quer continuar [S/N]:')).strip().upper()[0]
    if resp == 'N':
        break

print(f'O total da compra foi {total}')
print(f'Temos {mais} produto custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} e ele custa R${menor}')
