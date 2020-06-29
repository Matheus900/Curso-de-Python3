num_ex = ('Zero','Um','Dois','Três','Quatro','Cinco',
          'Seis','Sete','Oito','Nove','Dez','Onze',
          'Doze','Treze','Quatorze','Quinze','Dezesseis',
          'Dezessete','Dezoito','Dezenove','Vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'O número {num} por extenso é: {num_ex[num]}')
        break
    else:
        print('[ERROR] Número inválido!!!')
        num = int(input('Digite um número entre 0 e 20: '))