def main():
    um = input('n1')
    dois = input('n2')
    tres = input('n3')
    res = teste(um, dois, tres)
    print(f'A soma deu: {res}')


def teste(n1 = 0, n2 = 0, n3 = 0):
    s = n1 + n2 + n3
    return s
print(teste(9))