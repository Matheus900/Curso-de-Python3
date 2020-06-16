ini = int(input('Qual o primeiro termo da sua PA? '))
raz = int(input('Qual a razão da sua PA? '))
dec = ini + 9 * raz
for i in range(ini, dec + raz, raz):
    print('{}'.format(i), end=' -> ')
print('CABÔ')