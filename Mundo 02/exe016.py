num = int(input('Digite um número inteiro: '))
print('''[ 1 ] BINÁRIO\n
[ 2 ] OCTAL\n
[ 3 ] HEXADECIMAL''')
op = int(input('Opção: '))
if op == 1:
    print('O número {} em BINÁRIO fica {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('O número {} em OCTAL fica {}'.format(num, oct(num)[2:]))
else:
    print('O úmero {} em HEXADECIMAL fica {}'.format(num, hex(num)[2:]))