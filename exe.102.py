def fatoril(número, show=False):
    """
    -> Calcule o fatorial de um número.
    :param número: O nùmero a ser calculado.
    :param show: (opcional) mostrar ou  não a conta.
    :return: O valor do fatorial de um número n.
    """
    f = 1
    for c in range(número, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print('   x   ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

print(fatoril(5, show=True))
help(fatoril)