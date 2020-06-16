n = int(input('Digite um número\nPara mostrar o seu fatorial: '))
f = 1
c = n
print('Calculando....\n{}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
