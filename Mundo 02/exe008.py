v_casa = float(input('Digite o valor da casa: R$'))
qtd_anos = int(input('Emquantos anos você irá pagar a casa? '))
salario = float(input('Quanto é o seu slário atual? R$'))
qtd_parcelas = qtd_anos * 12
prestacao = v_casa / qtd_parcelas
if prestacao > salario * 0.3:
    print('O empréstimo foi NEGADO devido a falta de saldo.')
else:
    print('Empréstimo APROVADO.')