primeiro = int(input('Primeira termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for x in range(primeiro, décimo + razão, razão):
    print('{} '.format(x), end='')
print('ACABOU')