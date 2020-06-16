from random import choice
print('O pc vai escolher um número entre 1 e 5. Tente adivinhar qual será.')
numero = 0
possibilidade = [1, 2, 3, 4, 5]
pc = choice(possibilidade)
palpite = 0
while numero != pc:
    if numero != 0: 
        print('Você fracassou.')
    numero = int(input('Escolha seu número: '))
    palpite += 1
print('Você venceu\nParabéns!!')
print('Foram necessários {} palpites para você ganhar.'.format(palpite))