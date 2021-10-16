def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return 'NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        return 'OPCIONAL'
    else:
        return 'OBRIGATORIO'


print(voto(2004))
