soma = 0
for c in range(6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
print('A soma de todos os número pares é {} {} {}'.format(('\033[34m'), soma, ('\033[m')))