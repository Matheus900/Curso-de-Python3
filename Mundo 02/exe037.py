n = soma = cont = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:    
        soma += n
        cont += 1
    else:
        break
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))