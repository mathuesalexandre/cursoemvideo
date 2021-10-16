n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] saír do programa''')
    opção = int(input('>>>>>>qual é a sua opção?'))
    if opção == 1 :
      soma = n1 + n2
      print('A soma  entre {} e {} é {}'.format(n1, n2, soma))
    elif opção == 2:
      produto = n1 * n2
      print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opção == 3:
      if n1 > n2:
          maíor = n1
      else:
          maíor = n2
      print('Entre {} e {} o maior numero é {}'.format(n1, n2, maíor))
    elif opção == 4:
       print('Informe o  numero novamente: ')
       n1 = int(input('Primeiro numero: '))
       n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('opção inválida. tente novamente')
print('Fim do programa! volte sempre! ')
