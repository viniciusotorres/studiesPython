# FAÇA UM PROGRAMA QUE LEIA TRêS NÚMEROS E MOSTRE QUAL É O MAIOR E QUAL É O MENOR.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número'))

if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
else:
    maior = n3

print(f'O maior número é {maior}')
print(f'O menor número é {n1 if n1 < n2 and n1 < n3 else n2 if n2 < n1 and n2 < n3 else n3}')
