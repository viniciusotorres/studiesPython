# DESENVOLVA UM PROGRAMA QUE LEIA SEIS NÚMEROS INTEIROS E MOSTRE
# A SOMA APENAS DAQUELES QUE FOREM PARES. SE O VALOR DIGITADO FOR
# ÍMPAR, DESCONSIDERE-O.

sum = 0

for c in range(1, 7):
    number = int(input(f"Digite o {c}º número: "))
    if number % 2 == 0:
        sum += number

print(f"A soma dos números pares é {sum}")