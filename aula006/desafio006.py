
# Desafio 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite outro número: '))
# soma = n1 + n2
#
# print('A soma entre {} e {} é equivalente a {}!'.format(n1, n2, soma))

someThing = input('Digite Algo: ')
print('Agora iremos verificar o que você digitou!')
print('O que você digitou é do tipo: ', type(someThing))
print('O que você digitou é um número? ', someThing.isnumeric())
print('O que você digitou é alfabético? ', someThing.isalpha())
print('O que vocÊ digitou é alfanumérico? ', someThing.isalnum())
print('O que você digitou está em letras minúsculas? ', someThing.islower())
print('O que você digitou está em letras maiúsculas? ', someThing.isupper())