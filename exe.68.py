from random import randint
v = 0
while True:
    pessoa = int(input('diga um valor: '))
    computador = randint(0, 10)
    total = pessoa + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('par ou impar? [P/I] ')).strip().upper()[0]
    print(f'você jogou {pessoa} e o computador {computador}. total de {total}', end=' ')
    print('DEU PAR'if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('você PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('você PERDEU')
            break
    print('Vamos jogar novamente...')