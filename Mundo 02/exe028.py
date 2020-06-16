maior = 0
media = 0
soma = 0
mulher = 0
for i in range(4):
    nome = input('Qual é o seu nome? ')
    idade = int(input('Qual é a sua idade? '))
    sexo = input('Qual é o seu sexo?(M/F) ')
    soma += idade
    media = soma / 4
    if sexo == 'M':
        if idade > maior:
            maior = idade
            nome_maior = nome
    else:
        if idade < 20:
            mulher += 1
print('A media de idade do grupo é de {:.2f} anos'.format(media))
print('O homem mais velho é o {}'.format(nome_maior))
print('No grupo há {} mulheres com menos de 20 anos'.format(mulher))

