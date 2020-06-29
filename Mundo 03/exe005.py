lista = ('Açai','Ideia','Maçaneta','Loiro','Casa',
'Lua','Terra','Viagem','Motocicleta','Computador','Celular')
for palavra in lista:
    print(f'\nNa palavra {palavra} temos ', end='')
    palavra = palavra.lower()
    for letter in palavra:
        if letter in 'aeiou':
            print(letter, end=' ')        