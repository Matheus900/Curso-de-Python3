lista = ('Relógio', 120.00,
'Camiseta',100.00,
'Short',60.00,
'Mochila',150.00,
'Tênis',120.00)
for c in range(len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<30}', end='')
        if c+1 <= len(lista):
            print(f'R$ {lista[c+1]:>5}')