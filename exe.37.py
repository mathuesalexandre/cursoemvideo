num = int(input('digite um numero inteiro: '))
print('''escolha umas da opções'
[1]converter em BINÁRIO
[2]conerter em OCTAL
[3]converte em HEXADECIMAL''')
opção = int(input('sua opção: '))
if opção == 1:
    print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para hecadecimal e igual a {}'.format(num, hex(num)[2:]))
