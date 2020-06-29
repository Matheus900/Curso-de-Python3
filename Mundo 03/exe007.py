lista = []
while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Número duplicado')
    op = input('Deseja continuar?[S/N] ').upper()
    if op == 'S':
        pass
    elif op == 'N':
        break
    else:
        print('Opção inválida.')
        op = input('Deseja continuar?[S/N] ').upper()
lista.sort()
print(f'Você digitou os valores {lista}')