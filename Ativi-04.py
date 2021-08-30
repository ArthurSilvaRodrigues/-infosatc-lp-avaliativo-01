pt = float(input('Digite o valor total do premio: '))
pd = pt * 0.93
g1 = pd * 0.46
g2 = pd * 0.32
g3 = pd * 0.22
print('O valor do premio com imposto: {}'.format(pd) +
    '\nGanhador 01 ganhou: {:.2f} reais'.format(g1) +
    '\nGanhador 02 ganhou: {:.2f} reais'.format(g2) +
    '\nGanhador 03 ganhou: {:.2f} reais'.format(g3))