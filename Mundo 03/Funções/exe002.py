def main():
    msg = str(input('Digite a mensagem: '))
    escreva(msg)

def escreva(msg):
    num = len(msg) + 4
    print('~'*num)
    print(f'  {msg}')
    print('~'*num)


main()