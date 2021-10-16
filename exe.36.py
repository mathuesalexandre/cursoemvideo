casa = float(input('valor da casa: R$ '))
salario = float(input('Salario do comprador: R$'))
anos = int(input(' Quantos anos de financiamento?'))
prestação = casa / (anos * 12)
minimo = salario * 30 / 10
print('para pagar uma casa de {:.2f} em {} anos '.format(casa, anos), end='')
print('A prestação sera {:.2f} '.format(prestação))
if prestação <= minimo:
    print('emprestimo concedido')
else:
    print('emprestimo NEGADO')