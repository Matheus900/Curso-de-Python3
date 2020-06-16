for _ in range(5):
    maior = 0
    menor = 0
    peso = float(input('Digite o seu peso: '))
    if peso > maior:
        maior = peso
    if peso < maior:
        menor = peso
print('O maior peso registrado foi {}Kg e o menor peso registrado foi {}Kg'.format(maior, menor))