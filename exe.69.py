tot18 = totM = tot20 = 0
while True:
    idade = int(input('idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('sexo: [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totM = 1
    if sexo == 'F' and idade <= 20:
        tot20 = 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('quer continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'sao no total {tot18} mulheres com mais de 18 anos')
print(f'O total de homems cadastrados foi de {totM}')
print(f'O total de mulheres com menos de 20 anos e {tot20}')
