print('-=-'*20)
print('Analisador de triângulos')
print('-=-'*20)
r1 = float(input('primeiro segmento: '))
r2 = float(input('segundo segmento: '))
r3 = float(input('terceiro segmento: '))
if r1 + r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os segmentos acima PODEM FORMA um triângulo!')
else:
    print('OS segmentos acima NÃO FORMÃO um triângulo!')