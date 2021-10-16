L = float(input('lagura da parede: '))
A = float(input('altura da parede: '))
area = L*A
tinta = area / 2
print('Sua parede tem a dimenção de {}x{} é sua area e de {}m².'.format(L, A, area))
print('Para pintar essa parede, você presisará de {}l  de tinta.'.format(tinta))
