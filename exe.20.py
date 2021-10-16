from random import shuffle
n1 = str(input('primero aluno: '))
n2 = str(input('segundo aluno: '))
n3 = str(input('terceira aluno: '))
n4 = str(input('quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem da a prensentação será')
print(lista)
