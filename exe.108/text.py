import moeda
p = float(input('Digite o preço: R$'))
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'diminuindo 13, temos {moeda.moeda(moeda.diminuir(p, 13))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
