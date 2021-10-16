pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['name'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, Digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, Digite apenas S ou F.')
    if resp == 'N':
        break
print('=-'*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
print('=-'*30)
media = soma / len(galera)
print(f'B) A media de idade é {media} Anos.')
print('=-'*30)
print('C) As mulheres cadastradas foram', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["name"]} ', end='')
print()
print('=-'*30)
print('D) Listagem de pessoas  que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('      ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('=-'*30)
