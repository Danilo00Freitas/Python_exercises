s = c = 0
while True:
    n = int(input('Insira um número '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Foram inseridos {c} valores e a some é {s}')