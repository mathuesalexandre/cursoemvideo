import moeda
p = float(input('Digite o preço: R$'))
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'diminuindo 13, temos {moeda.diminuir(p, 13, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
