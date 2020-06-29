from random import randrange
lista = []
soma = 0
while True:
    num = randrange(10)
    if num not in lista:
        soma += num
        lista.append(num)
    if len(lista) == 5:
        break
print('Números gerados:',lista)
lista.sort()
lista = tuple(lista)
print('Menor número gerado:',lista[0])
print('Maior número gerado:',lista[4])
print('A soma de todos os valores gerados é:',soma)
print('A média dos números gerados é:',soma / 5)
#print(type(lista))