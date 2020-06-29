def main():
    n = leiaint('Digite um número: ')
    print(f'Você digitou o número {n}.')


def leiaint(msg):
    while True:
        n = input(msg).strip()
        if n.isdigit():
            break
        else:
            print('[ERROR] Digite um número inteiro!')
    return n


main()