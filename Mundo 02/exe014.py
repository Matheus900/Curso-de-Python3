preco = float(input('Qual o preço do produto? R$'))
forma_pagamento = int(input("""1) À vista(dinheiro/cheque)\n
2) À vista no cartão\n
3) Em até 2x no cartão\n
4) 3x ou mais no cartão\n
Opção: """))
if forma_pagamento == 1:
    preco -= preco * 0.1
    print('O valor total do produto será R${:.2f}'.format(preco))
elif forma_pagamento == 2:
    preco -= preco * 0.05
    print('O valor total do produto será R${:.2f}'.format(preco))
elif forma_pagamento == 3:
    print('O valor total do produto será R${:.2f}'.format(preco))
elif forma_pagamento == 4:
    preco += preco * 0.2
    print('O valor total do produto será R${:.2f}'.format(preco))