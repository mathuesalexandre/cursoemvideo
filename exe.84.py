temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = min = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < min:
            min = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('quer continuar? [S/N] '))
    if resp in 'Nn':
        break

print(f'Ao todo, você cadastrou{len(princ)} pessoas')
print(f'O maior peso foi de {mai}kg.peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]}', end='')
print()
print(f'o menor peso foi de {min}kg. peso de ', end='')
for p in princ:
    if p[1] == min:
        print(f'{p[0]}', end='')
print()
