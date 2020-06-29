from time import sleep
def main():
    contador(1, 10, 1)
    sleep(0.5)
    contador(10, 0, 2)
    sleep(0.5)
    print('Agora é a sua vez de personalizar a contagem!')
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    contador(inicio, fim, passo)


def contador(inicio, fim, passo):
    print('=-='*15)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    if inicio > fim:
        if passo < 0:
            passo *= -1
        for c in range(inicio, fim, -passo):
            print(c, end=' ')
            sleep(0.5)
    else:
        for c in range(inicio, fim, passo):
            print(c, end=' ')
            sleep(0.5)
    print('FIM!')
    print('=-='*15)

main()