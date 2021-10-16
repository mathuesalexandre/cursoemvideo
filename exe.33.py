a = int(input('Primeiro numero: '))
b = int(input('sugundo numero: '))
c = int(input('terceiro numero: '))
# Verificando o menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
# verificando o maior
maior = a
if b>a and b>c:
 maior  = b
if c>a and c>b:
    maior = c
print('o menor numero foi {}'.format(menor))
print('o maior numero foi {}'.format(maior))
