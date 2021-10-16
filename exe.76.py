"""print('-'*45)
print('              LISTA DE PREÇOS             ')
print('-'*45)

lista = ('Lápis', 1.75,
         'Borracha', 2.00,
         'Caderno', 15.90,
         'Estojo', 25.00,
         'Transferidor', 4.20,
         'compassao', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'livro', 34.90)

print(lista[0], end='')
print('.........................R$', lista[1])
print(lista[2], end='')
print('.........................R$', lista[3])
print(lista[4], end='')
print('.........................R$', lista[5])
print(lista[6], end='')
print('.........................R$', lista[7])
print(lista[8], end='')
print('.........................R$', lista[9])
print(lista[10], end='')
print('.........................R$', lista[11])
print(lista[12], end='')
print('.........................R$', lista[13])
print(lista[14], end='')
print('.........................R$', lista[15])
print(lista[16], end='')
print('.........................R$', lista[17])
print('-'*45)"""

lista = ('Lápis', 1.75,
         'Borracha', 2.00,
         'Caderno', 15.90,
         'Estojo', 25.00,
         'Transferidor', 4.20,
         'compassao', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'livro', 34.90)
print('-'*40)
print(f'{"           LISTAGEM DE PREÇOS"}')
print('-'*40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('-'*40)