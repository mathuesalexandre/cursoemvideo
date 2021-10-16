sálario = float(input('Qual o sálario do funcionario? R$'))
if sálario <= 1250:
    novo = sálario + (sálario * 15  / 100)
else:
    novo = sálario + (sálario * 10 / 100)
print('Quem ganhava {:.2f} agora ganha {:.2f}'.format(sálario, novo))