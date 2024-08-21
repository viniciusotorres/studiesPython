# Descrição: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

# algumaCoisa é um objeto que recebe um valor digitado pelo usuário
algumaCoisa = input('Digite algo: ')

print('Agora iremos verificar o que você digitou!')

# VERIFICA O TIPO DE DADO DIGITADO
print('O que você digitou é do tipo: ', type(algumaCoisa))
# VERIFICA SE O DADO DIGITADO É UM NÚMERO
print('O que você digitou é um número? ', algumaCoisa.isnumeric())
# VERIFICA SE O DADO DIGITADO É ALFABÉTICO
print('O que você digitou é alfabético? ', algumaCoisa.isalpha())
# VERIFICA SE O DADO DIGITADO É ALFANUMÉRICO
print('O que você digitou é alfanumérico? ', algumaCoisa.isalnum())
# VERIFICA SE O DADO DIGITADO ESTÁ EM LETRAS MINÚSCULAS
print('O que você digitou está em letras minúsculas? ', algumaCoisa.islower())
# VERIFICA SE O DADO DIGITADO ESTÁ EM LETRAS MAIÚSCULAS
print('O que você digitou está em letras maiúsculas? ', algumaCoisa.isupper())
# VERIFICA SE O DADO DIGITADO ESTÁ CAPITALIZADO
print('O que você digitou está capitalizado? ', algumaCoisa.istitle())
# VERIFICA SE O DADO DIGITADO É UM ESPAÇO
print('O que você digitou é um espaço? ', algumaCoisa.isspace())

