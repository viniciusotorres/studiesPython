# FAÇA UM PROGRAMA QUE MOSTRE NA TELA UMA CONTAGEM REGRESSIVA
# PARA O ESTOURO DE FOGOS DE ARTIFÍCIO, INDO DE 10 ATÉ 0, COM UMA
# PAUSA DE 1 SEGUNDO ENTRE ELES.

from time import sleep # Importa a função sleep da biblioteca time

for c in range(10, -1, -1): # Contagem regressiva de 10 até 0 com passo -1 (decremento)
    print(c) # Imprime o valor de c
    sleep(1) # Pausa de 1 segundo
print('FELIZ ANO NOVO!') # Imprime a mensagem de feliz ano novo

