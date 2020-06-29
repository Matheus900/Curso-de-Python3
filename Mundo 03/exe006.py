lista = []
for _ in range(5):
    lista.append(int(input('Digite um número: ')))
copia = lista[:]
print(f'Você digitou os números: ', end='')
for c in lista:
    print(c, end=' ')
lista.sort()
#print(f'Você digitou os números: {lista}')
print(f'\nO maior número digitado foi {lista[4]} e está na posição {copia.index(lista[4]) + 1}')
print(f'O menor número digitedo foi {lista[0]} e está na posição {copia.index(lista[0]) + 1}')