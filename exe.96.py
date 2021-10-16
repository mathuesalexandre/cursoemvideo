def area(largura, comprimento):
    a = largura*comprimento
    print(f'A área de terreno {l}x{c} é de {a}m²')
    print('=-' * 20)
#Programa principal
print('Controle de terrenos')
print('=-'*20)
l = int(input('Lagura (m):'))
c = int(input('Comprimento (m):'))
area(l, c)
