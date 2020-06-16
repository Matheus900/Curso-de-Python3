while True:
    print('=-='* 12)
    n = int(input(' Quer ver a tabuada de qual valor: '))
    print('=-='* 12)
    if n > 0:
        for c in range(11):
            print(f'{n} x {c} = {n*c}')
    else:
        print('FIM DO PROGRAMA')
        break
    