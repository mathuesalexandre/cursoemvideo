'''viagem = int(input('Qual a distancia da sua viagem? '))
curta = viagem * 0.50
longa = viagem * 0.45
if viagem <= 200:
    print('entao o preço vai ser R${}'.format(curta))
else :
    print('entao o preço vai ser R${}'.format(longa))'''


distancia = float(input('Qual a distancia da sua viagem? '))
print('você esta prestes a começar uma viagem de {}km'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia* 0.45
print('É o presço da sua passagem sera {}km'.format(preço))
