dias = int(input('Quantos dias alugados: '))
kms = float(input('Quaantos quilometros rodados: '))
valor_total = dias * 60 + kms * 0.15
print('O total a pagar é de R${:.2f}'.format(valor_total))
