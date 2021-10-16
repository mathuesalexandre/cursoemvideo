#Faça um programa que leia  nome e media de um aluno.
#guardando também a situação em dicionario.
#No final, mostre o conteudo da estrutura na tela
Aluno = {}
Aluno['nome'] = input('Nome:')
Aluno['media'] = float(input('media:'))

if Aluno['media'] >= 7:
    Aluno['situação'] = 'Aprovado'
elif 5 <= Aluno['media'] < 7:
    Aluno['situação'] = 'Recuperação'
else:
    Aluno['situação'] = 'Reprovado'

print('=-'*30)
for k, v in Aluno.items():
    print(f'  _ {k} é igual a {v}')

