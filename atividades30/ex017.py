import math

real = float(input('Digite um número real: '))
porcaoInteira = math.trunc(real)

print('A porção inteira de {} é igual a {}'.format(real, porcaoInteira))