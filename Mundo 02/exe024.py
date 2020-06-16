num = int(input('Digite um número: '))
c = 0
for i in range(1, num+1):
    if num % i == 0:
        c += 1
if c ==  2:
    print('Número primo.')
else:
    print('Número não primo.')
