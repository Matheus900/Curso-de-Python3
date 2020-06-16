n1 = int(input('Primeiro valor:  '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''
    [1] SOMAR\n
    [2] MULTIPLICAR\n
    [3] MAIOR\n
    [4] NOVOS NÚMEROS\n
    [5] SAIR DO PROGRAMA''')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, (n1 + n2)))
    elif opcao == 2:
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, (n1 * n2)))
    elif opcao == 3:
        if n1 > n2:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, n1))
        else:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, n2))
    elif opcao == 4:
        print('Informe os números novamente.')
        n1 = int(input('Primeiro valor:  '))
        n2 = int(input('Segundo valor: '))
    else:
        print('Opção inválida, tente novamente.')
    print('=-='*10)
print('Fim do programa.')
print('Volte sempre!!!')