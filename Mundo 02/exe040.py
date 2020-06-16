qtdH = 0
maior = 0
M20 = 0
while True:
    idade = int(input('Qual a sua idade? '))
    sexo = str(input('Qual o seu sexo?[M/F] ')).upper()
    if sexo in 'MF':
        op = str(input('Quer continuar?[S/N] ')).upper()
        if op == 'S':
            if idade > 18:
                maior += 1
            if sexo == 'M':
                qtdH += 1
            else:
                if idade < 20:
                    M20 += 1
        elif op == 'N':
            break
        else:
            print('[ERROR]')
    else:
        print('[ERROR]')
print(f'Há no grupo {maior} maior(es) de idade\n{qtdH} Homem(ns)\n{M20} Mulhere(s) com menos de 20 anos')