from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}

ranking = dict()

for i, j in jogo.items():
    print(f'{i} tirou {j} no dado')
    sleep(1)

print('=-'*30)
print(' == RANKING DOS JOGADORES ==')

ranking =sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, r in enumerate(ranking):
    print(f'{i+1} lugar: {r[0]} com {r[1]}.')