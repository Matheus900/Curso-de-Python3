frase = input('Digite seu nome completo: ')
print(len(frase[0]))
num = input('Digite um número entre  0 e 9999: ')
m = num[0]
c = num[1]
d = num[2]
u = num[3]
print("""Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}""".format(u, d, c, m))