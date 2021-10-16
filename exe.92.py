from datetime import datetime
dados = dict()
dados['nomes'] = str(input('Nome: '))
nasc = int(input('Ano de nacimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = int(input('Salario: '))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('=-'*30)
for i, d in dados.items():
    print(f'     - {d} tem o valor {i}')