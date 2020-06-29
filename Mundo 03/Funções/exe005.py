from random import choice
def main():
    numeros = [1,23,4,5,12,41,14,274,78,2,24,6,90]
    sorteia(numeros)


def sorteia(lista):
    sorteados = []
    while True:
        num = choice(lista)
        if num not in sorteados:
            sorteados.append(num)
        if len(sorteados) == 5:
            break
    print('=-='*25)
    print('Dos numeros:', end=' ')
    for num in lista:
        print(num, end=' ')
    print()
    print('=-='*25)
    print(f'Foram sorteados os números: {sorteados}')
    print('=-='*25)
    somapar(sorteados)


def somapar(sorteados):
    soma = 0
    print(f'Entre os numeros sorteados os numeros pares foram: ', end=' ')
    for num in sorteados:
        if num % 2 == 0:
            soma += num
            print(num, end=' ')
    print()
    print('=-='*25)
    print(f'Somando esses números pares temos {soma}')
    print('=-='*25)


main()