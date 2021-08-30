autura = float(input('Digite a autura da parede: '))
comprimento = float(input('Digite o comprimento da parede: '))
m = autura * comprimento
l = m / 3
lata = l / 3.6
pt = m * lata
print('A sua parede de {:.2f} m² precisa de {:.0f} latas de tintas e isso custara {:.2f} reais'.format(m,lata,pt))