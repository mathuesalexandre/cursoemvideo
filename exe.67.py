while True:
    n = int(input('Quer ver a tabuada de qual valor?'))
    if n <= 0:
        break
    for x in range(1, 11):
        soma = n * x
        print(f'{n} x {x} = {soma}')
print('tabuada finalizada...')