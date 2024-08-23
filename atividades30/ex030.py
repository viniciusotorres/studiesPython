#CRIE UM PROGRAMA QUE LEIA UM NÚMERO  INTEIRO E MOSTRE NA TELA SE ELE É PAR OU ÍMPAR.

numero = int(input('Digite um número qualquer:  '))
if numero % 2 == 0:
    print('O número {} é par'.format(numero))
else:
    print('O número {} é ímpar'.format(numero))
