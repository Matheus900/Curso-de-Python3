pri = int(input('Primeiro termo da PA? '))
raz = int(input('Qual a razão da PA? '))
termo = pri
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total: 
        print('{} -> '.format(termo), end='')
        termo += raz
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')