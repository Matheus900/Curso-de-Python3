alt = float(input('Qual a altura da sua parede? '))
larg = float(input('Qual a largura da sua parede? ')) 
tinta = (alt * larg) / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.3f}m²'.format(alt, larg, (alt*larg)))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))