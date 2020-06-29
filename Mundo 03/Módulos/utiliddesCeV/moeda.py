def aumentar(num, pct, op=True):
    res = num + (num * (pct / 100))
    return res if op is not True else moeda(res)


def diminuir(num, pct, op=True):
    res = num - (num * (pct / 100))
    return res if op is not True else moeda(res)


def metade(num, op=True):
    res = num / 2
    return res if op is not True else moeda(res)


def dobro(num, op=True):
    res = num * 2
    return res if op is not True else moeda(res)


def moeda(num, moeda = 'R$'):
    return f'{moeda}{num}'.replace('.', ',')


def resumo(num, aum, dim):
    print('=-='*15)
    print('{:^45}'.format('RESUMO DO VALOR'))
    print('=-='*15)
    resultado = str(num).replace('.',',')
    print(f'Preço analisádo:               R${resultado}')
    print(f'Dobro do preço:                R${dobro(num, True)}')
    print(f'Metade do preço:               R${metade(num, True)}')
    print(f'{aum}% de aumento:                R${aumentar(num, aum)}')
    print(f'{dim}% de redução:                R${diminuir(num, dim)}')
    print('=-='*15)
    
    return '{:^45}'.format('>>>  FIM DO PROGRRAMA  <<<')