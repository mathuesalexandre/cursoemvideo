nota1 = float(input('primeira nota: '))
nota2 = float(input('segundo nota: '))
media = nota1 + nota2 / 2
print('tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
if 7 > media >= 5:
    print('O Aluno ésta em RECUPERAÇÃO.')
elif media < 5 :
    print('O aluno esta REPROVADO.')
elif media > 7:
    print('O aluno foi APROVADO.')