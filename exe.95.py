time = list()
jogador = dict()
partida = list()

while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome: '))
    tot = int(input(f'Quantas partidas {jogador["Nome"]} Jogou? '))
    partida.clear()
    for p in range(0, tot):
        partida.append(int(input(f'     Quantos gols na partida {p+1}?')))
    jogador['gols'] = partida[:]
    jogador['total'] = sum(jogador['gols'])
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-'*30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('=-'*30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print()
print('=-'*30)

while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para sair] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
        print('=-'*30)