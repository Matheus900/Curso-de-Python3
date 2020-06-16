vel = float(input('Qual a velocidade do seu carro(em Km/h)? '))
if vel > 80:
    multa = (vel - 80) * 7
    print('Você foi multado em R${:.2f}'.format(multa))
else:
    print('Sem multa.')