lista = []
cont = 0
while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
    else:
        print('Número já digitado!')
    cont += 1
    op = input('Quer continuar?[S/N] ').upper()
    if op in 'SN':
        if op == 'N':
            break
    else:
        print('Opção inválida.')
        op = input('Quer continuar?[S/N] ').upper()
print(f'Você digitou {cont} números.')
lista.sort(reverse=True)
print(f'Você digitou os números: {lista}')
if 5 in lista:
    print('O número 5 foi digitado e está na lista.')
else:
    print('O número 5 não foi digitado nenhuma vez. Por isso não está na lista.')