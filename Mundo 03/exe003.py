contpar = 0
lista = []
for c in range(4):
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        contpar += 1
lista = tuple(lista)
print(f'O número 9 apareceu {lista.count(9)} vezes.')
if 3 in lista:
    print(f'O primeiro número 3 apareceu na posição {lista.index(3) + 1}.')
else:
    print('O número 3 não apareceu na lista.')
print(f'Você digitou {contpar} números pares.')