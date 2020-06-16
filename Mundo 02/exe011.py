ano_pessoa = int(input('Digite o ano de seu nascimento: '))
if 2020 - ano_pessoa < 0:
    print('Idade inválida')
elif 2020 - ano_pessoa <= 9:
    print('Mirim')
elif 2020 - ano_pessoa <= 14:
    print('Infantil')
elif 2020 - ano_pessoa <= 19:
    print('Júnior')
elif 2020 - ano_pessoa == 20:
    print('Sênior')
else:
    print('Master')