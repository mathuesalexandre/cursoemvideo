# (A) quantas vezes aparecu o valor 9
# (B) Em que posicão foi digitado o numero 3
# (C) Quais foram os valores pares
aa = 0
n = (int(input('Digite um numero: ')),
     int(input('Digite um numero: ')),
     int(input('Digite um numero: ')),
     int(input('Digite um numero: ')))
print(f'A quantida de vezes que vc digitou 9 foi {n.count(9)} vezes')
if n.count(3) > 0:
    print(f'Na {n.index(3) + 1}º posição foi encontrado o numero 3')
else:
    print(f'Não foi encontrado o numero 3')
print('O valores pares digitados foram ', end='')
for x in n:
    if x % 2 == 0:
        print(x, end=' ')
