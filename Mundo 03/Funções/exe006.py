from datetime import datetime
def main():
    nasc = int(input('Digite o seu ano de nsacimento: '))
    print(f'Devido a sua idade seu voto será: {voto(nasc)}')
    

def voto(ano):
    agora = datetime.now().year
    idade = agora - ano
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


main()