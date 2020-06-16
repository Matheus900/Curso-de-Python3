sexo = str(input('Digite o seu sexo: [M/F] ')).strip().upper() [0]
while sexo not in 'MF':
    sexo = str(input('Dado inválido. Por favor, informe seu sexo: ')).strip().upper() [0]
print('Sexo {} cadastrado com sucesso'.format(sexo))
