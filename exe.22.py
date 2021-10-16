nome = str(input('Digite seu nome: '))
print('Analidando seu nome...')
print('Seu nome em maiúscula é {}'.format(nome.upper()))
print('Seu nome em minúscula é {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome)))
separa = nome.split()
print('seu primeiro nome é {} é ele tem {} letras'.format(separa[0], len(separa[0])))

