def maior(* núm):
    cont = maior = 0
    print('\nAnalisando os valores passados...')
    for valor in núm:
        print(f'{valor} ', end='', flush=True)
        if cont == 0:
                maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')

#programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(0)


