times = ('Palmeiras','Internacional','Fluminense','Corinthians','Flamengo','Atlético-PR',
'Atlético-MG','Fortaleza','São Paulo','América-MG','Botafogo',
    'Santos','Goiás','Bragantino','Coritiba','Cuiabá','Ceará SC',
    'Atlético-GO','Avaí','Juventude')

print(f'Os 5 primeiros colocados são {times[0:5]}')

print(f'Os 4 últimos colocados são {times[16:21]}')

print(f'Os times em ordem alfabética: {sorted(times)}')

x = str(input('Informe qual time deseja procurar? '))
print(f'O time {x} está na posição {times.index(x) + 1}')