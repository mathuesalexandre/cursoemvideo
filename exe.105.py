def notas(*n, sit=False):
    """""
    -> Função para analizar notas e situaçoes de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situacão
    :return: dicionario com varias informações sobre a situação da turma.
    """""
    r = dict()
    r['total'] = len(n)
    r['menor'] = min(n)
    r['maior'] = max(n)
    r['média'] = sum(n)/len(n)

    if sit:
        if r['média'] >= 7:
            r['situação'] = 'boa'
        elif r['média'] >= 5:
            r['situação'] = 'Razoavel'
        else:
            r['situação'] = 'Ruim!'

    return r

#programa principal
resp = notas(9.5, 9.5, 9.5, sit=True)
print(resp)
help(notas)