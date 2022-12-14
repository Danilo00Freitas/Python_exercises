matriz = [[0,0,0],[0,0,0],[0,0,0]]
temp = []
soma_par = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Defina um valor para ({l}, {c}) '))

print('-='*30)

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end=' ')
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
    print()

print('-='*30)

print(f'A soma dos números pares é: {soma_par}')
print(f'A soma da tarceira coluna é {matriz[0][2]+matriz[1][2]+matriz[2][2]}')
matriz[1].sort()
print(f'O maior valor da segunda linha é {matriz[1][2]}')
