l1 = float(input('Primeiro lado: '))
l2 = float(input('Segundo lado: '))
l3 = float(input('Terceiro lado: '))
if l1 < l2 + l3 or l2 < l1 + l3 or l3 < l1 + l2:
    print('Esses valores admitem um triângulo.') 
    if l1 == l2 == l3:
        print('Trângulo equilátero.')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Triângulo isóceles.')
    else:
        print('Triângulo escaleno.')
else:
    print('Esses valores não admite um triângulo.')