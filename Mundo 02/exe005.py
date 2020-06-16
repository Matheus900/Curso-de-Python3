km = float(input('Digite a distãncia da sua viagem: '))
if km > 200:
    valor = ((km - 200) * 0.45) + 200 * 0.5
    print('O valor da sua passagem é R${:.2f}'.format(valor))
else:
    valor = km * 0.5
    print('O valor da sua passagem é R${:.2f}'.format(valor))