lista = []
listap = []
listai = []
while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
        print('Número adicionado com sucesso!')
    else:
        print('Número já adicionado.')
    if num % 2 == 0:
        if num not in listap:
            listap.append(num)
    else:
        if num not in listai:
            listai.append(num)
    op = input('Quer continuar?[S/N] ').upper()
    if op in 'SN':
        if op == 'N':
            break
    else:
        print('Opção inválida.')
        op = input('Quer continuar?[S/N] ').upper()

print(f'Você digitou os números: {lista}')
print(f'Os números pares que você digitou foram: {listap}')
print(f'Os números ímpares que você digitou foram: {listai}')