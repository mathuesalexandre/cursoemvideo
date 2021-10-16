ficha = []
while True:
    name = str(input('Nome:'))
    nota1 = float(input('nota 1 :'))
    nota2 = float(input('nota 2 :'))
    media = (nota1 + nota2) / 2
    ficha.append([name, [nota1, nota2], media])
    cont = str(input('Quer continuar? [S/N]'))
    print('=-'*30)
    if cont in "Nn":
        break
print('-'*30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')

for i, a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")

while True:
    print('-'*30)
    opc = int(input("mostrar notas de qual aluno? (999 para interromper):"))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')