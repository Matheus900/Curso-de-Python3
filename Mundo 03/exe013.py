geral = list()
par = list()
impar = list()
for _ in range(7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    par.sort()
    impar.sort()
geral.append(impar)
geral.append(par)
print(f'Os valores pares digitados foram: {geral[1]}')
print(f'Os valores ímpares digitados foram: {geral[0]}')
