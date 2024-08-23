# FAÇA UM PROGRAMA QUE CALCULE  A SOMA ENTRE TODOS OS NÚMEROS ÍMPARES
# QUE SÃO MÚLTIPLOS DE TRÊS E QUE SE ENCONTRAM NO INTERVALO DE 1 ATÉ 500.

# for c in range(1, 501, 2): # Contagem de 1 até 500 com passo 2 (ímpares)
#     if c % 3 == 0: # Se c for múltiplo de 3
#         print(c, end=' ') # Imprime o valor de c com um espaço no final da linha (end=' ')

for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c, end=' ')