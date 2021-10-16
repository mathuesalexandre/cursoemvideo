lista = []

while True:
    n = lista.append(int(input('digite um número: ')))
    resp = str(input('Quer contiuar? [S/N] '))
    if resp in 'Nn':
        break
print('=-'*30)
print(f'Vocé digitou {len(lista)} elementos')
lista.reverse()
print(f'Os valores em ordem decressente são {lista}')
#if lista.count(5) > 0:
#    print('O valor 5 faz parte da lista')
#else:
#   print('O valor 5 não foi encontrado na lista')

#Tbm pode ser:

#if 5 in lista:
 #   print('O valor 5 faz parte da lista')
#else:
#    print('O valor 5 não foi encontrado na lista')