r1 = float(input('Primeira segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmetos aciama PODEM FORMAR triângulos!', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
            print('ESCALENO!')
    else:
        print('ISÓCELES')

else:
    print('Os segmentos acima NÃO PODEM FORMA triângulos')
