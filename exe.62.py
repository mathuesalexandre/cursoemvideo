print('Gerador de PA')
print('=-' * 20)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão de PA: '))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} - '.format(termo), end='')
        termo += razão
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você que mostrar a mais ?'))
print('Progressão finalizada com {} termos mostrados.'.format(total))
