def main():
    larg = float(input('LARGURA (m): '))
    comp = float(input('COMPRIMENTO (m): '))
    print(area(larg, comp))


def area(larg, comp):
    area = larg * comp
    return f'A área do seu terreno, que tem mede {larg}x{comp}, é {area}m²'


main()