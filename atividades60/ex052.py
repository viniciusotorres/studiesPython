# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E DIGA SE ELE É OU NÃO UM NÚMERO PRIMO.

number = int(input("Digite um número inteiro: "))
count = 0

for c in range(1, number + 1):
    if number % c == 0:
        count += 1

if count == 2:
    print(f"{number} é um número primo.")
else:
    print(f"{number} não é um número primo.")