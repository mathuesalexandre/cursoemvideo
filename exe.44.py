print('{:=^40}'.format(' LOJAS GUANABARA '))
preço = float(input('Preço das compras: R$'))
print('''Formas de pagamento
[1] á vista dinheiro/Pagamento
[2] á vista no cartão
[3] 2x no cartão 
[4] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
    print('sua compra de {} agora custa {} no final'.format(preço, total))

elif opção == 2:
    total = preço - (preço *5 / 100)
    print(' Sua compra de R${:.2f} vai custar {:.2f} no final'.format(preço, total))
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em: 2x de {:.2f}'.format(parcela))
    print('Sua compra de {:.2f} agora custa {:.2f} no final'.format(total, total))
elif opção == 4:
    total = preço + (preço * 20 / 100 )
    totaldeparcela = int(input('Qual total de parcelas?'))
    parcela = total / totaldeparcela
    print('sua compra sera parcelada em {}x de R${}'.format(totaldeparcela, parcela))
    print('sua compra de {} vai custa {} no final'.format(preço, total))
else:
    total = 0
    print('OPÇÃO INVALIDA DE PAGAMETO !!!')
