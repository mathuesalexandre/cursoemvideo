cont = 0
soma = 0
for x in range(1, 501, 2):
    if x % 3 == 0:
      cont = cont + 1
      soma = soma + x
print('A soma de todos os {}  valores solicitados foi {}'.format(cont, soma))