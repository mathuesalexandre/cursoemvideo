def ficha(jog='<desconhecido>', gols=0):
    print(f'O jogador {jog} fez {gols} no campeonato')

#programa principal
n = str(input('Nome do jogador:'))
g = str(input('Numero de gols'))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)