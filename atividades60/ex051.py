# DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA
# PROGRESSÃO ARITMÉTICA. NO FINAL, MOSTRE OS 10 PRIMEIROS TERMOS
# DESTA PROGRESSÃO.
#

first_term = int(input("Digite o primeiro termo da PA: "))
reason = int(input("Digite a razão da PA: "))

for c in range(0, 10):
    print(first_term + c * reason, end=' ')
print('FIM')
