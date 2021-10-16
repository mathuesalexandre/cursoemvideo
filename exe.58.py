from random import randint
computador = randint(0, 10)
print('Sou seu  computador... Acabei de pensar em número entre 0 é 10.')
print('-=' * 35 )
print('será que vc consegue adivinhar qual foi?')
print('-=' * 35 )
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu papite?'))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez .')
        elif jogador > computador:
            print ('Menos... tente mais uma vez.')
print('Acertou com {} tentativas. parabéns!'.format(palpites))
