cont = 0
for _ in range(7):
    ano = int(input('Ano de nascimento: '))
    if 2020 - ano >= 21:
        cont += 1
print('{} pessoas dessa família já atingiram a maioridade. E {} ainda são menores.'.format(cont, (7- cont)))
