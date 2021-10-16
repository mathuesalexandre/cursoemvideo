palavras = ('aprender', 'programar', 'linguaguem', 'python',
            'curso', 'gratis', 'estuda', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futura')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos', end=' ')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')


