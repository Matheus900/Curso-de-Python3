total = 0
maisBarato = 0
maisCaro = 0
mil = 0
while True:
    nome = str(input('Qual o nome do produto: '))
    preco = float(input('Qual o preco do produto: '))
    opcao = str(input('Quer continuar? ')).upper()
    total += preco
    if preco >= maisCaro:
        maisCaro = preco
    else:
        maisBarato = preco
        real = nome
    if preco > 1000:
        mil += 1
    if opcao == 'N':
        print('Fim')
        break
print(f'O total gasto em produtos foi R${total}')
print(f'O produto mais barato foi o {real}')
print(f'Você comprou {mil} producos que custaram mais de R$1000.00')