import moeda
p = float(input('Digite o preço: R$'))
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'diminuindo 13, temos {moeda.diminuir(p, 13)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'A metade de {p} é {moeda.metade(p)}')