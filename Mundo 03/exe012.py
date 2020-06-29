galera = list()
dados = list()
totp = 0
mai = men = 0
while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Digite seu peso: ')))
    if len(galera) == 0:
        mai = men = dados[1]
    else:
        if dados[1] < mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    galera.append(dados[:])
    dados.clear()
    totp += 1
    op = str(input('Quer continuar:[S/N] ')).upper()
    if op in 'SN':
        if op == 'N':
            break
    else:
        print('Opção inválida!')
        op = str(input('Quer continuar:[S/N] ')).upper()
print(f'Ao todo foram cadastradas {totp} pessoas')
print(f'O maior peso registrado foi: {mai}Kg. Peso de: ', end='')
for p in galera:
    if p[1] == mai:
        print(f'[{p[0]}] ', end=' ')
print()
print(f'O menor peso registrado foi: {men}Kg. Peso de: ',end='')
for p in galera:
    if p[1] == men:
        print(f'[{p[0]}] ', end=' ')
print()