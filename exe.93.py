jogador = dict()
partida = list()
jogador['Nome'] = str(input('Nome: '))
tot = int(input(f'Quantas partidas {jogador["Nome"]} Jogou? '))
for p in range(0, tot):
    partida.append(int(input(f'     Quantos gols na partida {p+1}?')))
jogador['gols'] = partida[:]
jogador['total'] = sum(jogador['gols'])
print('=-'*30)
print(jogador)
print('=-'*30)
for i, j in jogador.items():
    print(f'O campo {i} tem o valor {j}')
print('=-'*30)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["gols"])}')
for i, j in enumerate(jogador['gols']):
    print(f'     => Na partida {i}, fez {j} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
print('=-'*30)