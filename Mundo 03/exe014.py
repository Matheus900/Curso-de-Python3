matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input('Digite um número: '))
print('=-='*7)

for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()