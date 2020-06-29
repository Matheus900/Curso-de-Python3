def notas(*notas, sit=False):
    """
    -> Função para analisar notas e situaçõesde vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: retorna um dicionário com várias informações sobre a turma.
    """
    notas = list(notas)
    tot = 0
    res = dict()
    for _ in notas:
        tot += 1
    res['total'] = tot
    res['maior'] = max(notas)
    res['menor'] = min(notas)
    res['media'] = (sum(notas) / tot)
    if sit == True:
        if res['media'] < 6:
            res['situaçao'] = 'RUIM'
        elif 6 <= res['media'] < 7:
            res['situacao'] = 'RAZOÁVEL'
        else:
            res['situacao'] = 'BOA'
        return res
    else:
        return res

print(notas(3.5, 7.6, 4, 5, sit=True))
#help(notas)