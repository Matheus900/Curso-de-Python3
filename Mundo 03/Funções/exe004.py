def main():
    contador(1,5,2,6,4,9)
    contador(5,7,11,3,78)
    contador(14,4,5,16,76,88,9)
    contador()


def contador(* valores):
    if len(valores) > 0:
        print('=-='*15)
        print('Analisando os valores informados...')
        print('Os números', end=' ')
        for n in valores:
            print(n, end=' ')
        print(f'Foram informados {len(valores)} valores ao todo.')
        print(f'O maior valor informado foi {max(valores)}')
        print('=-='*15)
    else:
        print('=-='*15)
        print('Analisando os valores informados...')
        print('Foram informados 0 valores ao todo.')
        print('O maior valor informado foi 0.')
        print('=-='*15)


main()