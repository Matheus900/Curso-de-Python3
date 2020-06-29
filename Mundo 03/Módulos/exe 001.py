from utiliddesCeV import moeda, dado

p = dado.leiadinheiro('Digite o preço: R$')
res = str(p).replace('.', ',')
print(f'A metade de {res} é {moeda.metade(p)}')
print(f'O dobro de {res} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(p, 13)}')
#print(moeda.resumo(p, 80, 35))