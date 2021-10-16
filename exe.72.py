#   Exercício Python 072 - Número por Extenso
#   Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#   Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
pos = -1
while pos < 0 or pos > 20:
    pos = int(input('Digite um numero de (0 á 20): '))
    if pos < 0 or pos > 20:
       print('TENTE OUTRA VEZ')
numero = (numeros[pos])
print(f'o numero que vc digitou foi {numero}')'''

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    cont = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= cont <= 20:
        break
    print('Tente novamente. ', end='')
print(f'O numero que vc digitou foi {numeros[cont]}')
