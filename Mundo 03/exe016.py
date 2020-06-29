geral = list()
dados = list()
while True:
    dados.append(str(input('Nome:  ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    geral.append(dados[:])
    dados.clear()
    op = str(input('Quer adicionar mais um aluno?[S/N] ')).upper()
    if op in 'SN':
        if op == 'N':
            break
    else:
        print('Opção inválida!')
        op = str(input('Quer adicionar mais um aluno?[S/N] ')).upper()
print('{:^69}'.format('Boletim Geral'))
print('=-='*26)
for pos, element in enumerate(geral):
    media = (element[1] + element[2]) / 2
    print(f'| Nº {pos} | Nome: {element[0]:<15} | Nota 1: {element[1]:<5} | Nota 2: {element[2]:<5}| Média: {media:<5} |')
    print('=-='*26)
while True:
    aluno = str(input('Quer ver a o boletim de algúm aluno individualmente?[S/N] ')).upper()
    if aluno in 'SN':
        if aluno == 'S':
            num = int(input('De qual aluno você quer ver o boletim? '))
            mediai = (geral[num][1] + geral[num][2]) / 2
            print(f'Boletim do aluno de número: {num}')
            print(f'| Nº {num} | Nome: {geral[num][0]:<15} | Nota 1: {geral[num][1]:<5} | Nota 2: {geral[num][2]:<5}| Média: {mediai:<5} |')
        else:
            print('Fim do Programa!')
            break
    else:
        print('[ERROR] Opção inválida!')
        aluno = str(input('Quer ver a o boletim dos aulonos individualmente?[S/N] ')).upper()