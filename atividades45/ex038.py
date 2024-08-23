# ESCREVA UM PROGRAMA QUE LEIA DOIS NÚMEROS INTEIROS E COMPARE-OS, MOSTRANDO NA TELA UMA MENSAGEM:
# - O PRIMEIRO VALOR É MAIOR
# - O SEGUNDO VALOR É MAIOR
# - NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O PRIMEIRO VALOR É MAIOR')
elif n2 > n1:
    print('O SEGUNDO VALOR É MAIOR')
else:
    print('NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS')