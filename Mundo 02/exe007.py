salario = float(input('Digite o seu salário: R$'))
if salario < 1250.00:
    print('Seu novo salário será R${}'.format(salario + salario * 0.15))
else:
    print('Seu novo salário será R${}'.format(salario + salario * 0.1))