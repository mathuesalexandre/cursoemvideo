from datetime import date
atual = date.today().year
nascimento = int(input('Digite sua data de nacimento:'))
idade = atual- nascimento
print('O Atleta tem {} Anos.'.format(idade))
if idade <= 9:
    print('CLASSIFICAÇÃO: Mirim.')
elif idade <= 14:
    print('CLASSIFICAÇÃO: Infantil.')
elif idade <= 19:
    print('CLASSIFICAÇÃO: Junior.')
elif idade <= 24:
    print('CLASSIFICAÇÃO: Senior.')
elif idade >= 24:
    print('CLASSIFICAÇÃO: Master')