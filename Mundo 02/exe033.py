pri = int(input('Primeiro termo da PA? '))
raz = int(input('Qual a razão da PA? '))
termo = pri
cont = 1
while cont <= 10: 
    print('{} -> '.format(termo), end='')
    termo += raz
    cont += 1
print('FIM')