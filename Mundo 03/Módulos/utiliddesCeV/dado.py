def leiadinheiro(msg):
    while True:
        n = input(msg).strip()
        n = n.replace(',', '.')
        try:
            float(n)

            return float(n)
        except:
            print('[ERROR] Digite um número inteiro!')
            