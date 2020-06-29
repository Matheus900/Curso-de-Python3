aluno = dict()
aluno['Nome'] = str(input('Nome do aluno: '))
aluno['Média'] = float(input('Média do aluno: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'APROVADO'
else:
    aluno['Situação'] = 'REPROVADO'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
