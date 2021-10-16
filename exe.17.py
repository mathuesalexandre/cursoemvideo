'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjascente: '))
hi = (co ** 2 +  ca ** 2 ) ** (1/2)
print ('A hipotenusa vai medir {:.2f}.'.format(hi))'''

import math
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimeto do cateto adjascente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
