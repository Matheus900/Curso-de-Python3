def main():
    num = int(input('Qual número deseja ver o fatorial? '))
    show = str(input('Deseja ver o processo de fatorial?[S/N] ')).upper()
    print(fatorial(num, show))

def fatorial(num=1,mostrar='N'):
    f = 1
    n = num
    for c in range(num, 0, -1):
        f *= c
    if mostrar == 'S':            
        for _ in range(num, 0, -1):
            if n > 1:
                print(n, end=' x ' )
            else:
                print(n, end=' = ')
            n -= 1
    return f

main()