frase = input('Digite seu nome completo: ')
print(frase.upper())
print(frase.lower())
frase = frase.split()
soletras = ''.join(frase)
print(len(soletras))