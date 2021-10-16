lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        lista[l][c] = int(input('Digite um numero: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[l][c]}]', end='')
    print()
