sexo = str(input('INFORME SEU SEXO: [M/F]')).strip().upper()[0]
while sexo not in 'M F':
    sexo = str(input('Dados invalidos, digite outra vez: ')).strip().upper()[0]
print('sexo {} registraddo com sucesso'.format(sexo))