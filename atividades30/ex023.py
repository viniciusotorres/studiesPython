# FALA UM PROGRAMA QUE LEIA  UM NÚMERO DE 0 A 9999 E MOSTRE NA TELA CADA UM DOS DÍGITOS SEPARADOS
# Ex: Digite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

num = int(input('Digite um número de 0 a 9999: '))
newNum = str(num)
print('Unidade: {}'.format(newNum[3]))
print('Dezena: {}'.format(newNum[2]))
print('Centena: {}'.format(newNum[1]))
print('Milhar: {}'.format(newNum[0]))