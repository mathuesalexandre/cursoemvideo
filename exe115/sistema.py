from exe115.lib.interface import *
from time import sleep
from exe115.lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExistente(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['ver pessoas cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de lista o conteudo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma pessoa
        nome = str(input('nome: '))
        idade = LeiaInt('idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do programa
        print('Saindo do sistema... Até logo!')
        break
    else:
        # Digitou  uma opção errada no menu
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1.5)
