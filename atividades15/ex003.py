
# Crie um programa que leia dois números e mostre a soma entre eles.

# Correto

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1 + n2

print('A soma entre {} e {} é equivalente a {}!'.format(n1, n2, soma))

# Incorreto

n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')
s = n1 + n2

print('A soma entre', n1, 'e', n2, 'é igual a', s)

