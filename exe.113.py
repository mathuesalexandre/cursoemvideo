import traceback
def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuario preferio não digitar esse número. \033[m')
            return 0
        else:
            return n
def LeiaFloat(msg):
    while not 'valor' in locals():
        try:
            valor = float(input(msg))
        except(TypeError, ValueError):
            print('\033[31mERRO: Por favor, Digite um numero Real valido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mUsuario Preferiu não Digitar o numero:\033[m')
            return 0
        else:
            return valor


inteiro = LeiaInt('Digite um numero: ')
real = LeiaFloat('Digite um numero Real: ')
print(f'O numero inteiro foi {inteiro}\nO numero Real foi {real}')
