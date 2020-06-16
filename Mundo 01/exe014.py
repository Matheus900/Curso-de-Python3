salario = float(input('Qual é o salario do funcionário? R$'))
print('Um funcionário que ganhava {}, com o aumento de 15%, passa a receber R${:.2f}'.format(salario, (salario + salario * 0.15)))
