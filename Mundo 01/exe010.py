num = float(input('Digite uma distãncia em metros: '))
print('A medida de {:.1f}m corresponde a'.format(num))
print('{:.3f}km \n{:.2f}hm \n{:.1f}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format((num/1000), (num/100), (num/10), (num*10), (num*100), (num*1000)))