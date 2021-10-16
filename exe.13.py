salário = float(input('Qual é o salario do funcionario? R$'))
novo = salário + (salário * 15/100)
print('Um funcionario que ganhava {}, com 15% de aumento, passa a receber {}'.format(salário, novo))