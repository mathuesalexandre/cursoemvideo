'''times = ('CORINTHIANS',
'CRUZEIRO',	'FLAMENGO',	'GRÊMIO',
'INTERNACIONAL',	'PALMEIRAS',	'SANTOS',
'SÃO PAULO',	'SPORT', 'VITÓRIA', 'BOTAFOGO',	'CEARÁ', )
list = print(f'Lista de times do Brasileirão: {times}')
o5 = times[0], times[1], times[2], times[3], times[4], times[5]
print (f'Os cinco primeiro times são: {o5}')
i4 = times[-1], times[-2], times[-3], times[-4]
print(f'os 4 ultimos times são : {i4}')
print(.(times))'''

time = ('Corinthias', 'Palmeiras', 'Santos', 'Grêmio',
        'Cruzeiro', 'Flamengo','Vasco', 'Chapecoense',
        'Atlético', 'Botafogo', 'Atletico-PR','Bahia',
        'São paulo', 'Fluminense','Sport Recife',
        'EC Vitória', 'coritiba', 'Avaí', 'Ponte Preta',
        'Atlético-GO')
print('-='*15)
print(f'Lista de times do Brasileirão: {time}')
print('-='*15)
print(f'Os 5 primeiros são {time[0:5]}')
print('-='*15)
print(f'Os 4 ultimos são {time[-4:]}')
print('-='*15)
print(f'Times em ordem Alfabetica: {sorted(time)}')
print('-='*15)
print(f'O chapecoense está na {time.index("Chapecoense")} Posição')