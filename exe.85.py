lista1 =[]
par = []
impar= []
for x in range(0, 8):
    numero = int(input(f'Digite o {x}o valor: '))
    if (numero%2) == 0:
        par.append(numero)
    else:
        impar.append(numero)
lista1.append(par[:])
lista1.append(impar[:])
print(f'os valores pares foram {lista1[0]}')
print(f'os valores impares foram {lista1[1]}')
