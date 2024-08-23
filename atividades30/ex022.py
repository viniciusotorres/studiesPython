# CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
# - O NOME COM TODAS AS LETRAS MAIÚSCULAS
# - O NOME COM TODAS AS LETRAS MINÚSCULAS
# - QUANTAS LETRAS AO TODO (SEM CONSIDERAR ESPAÇOS)
# - QUANTAS LETRAS TEM O PRIMEIRO NOME

nome = input('Digite seu nome completo: ' ).strip()
print("Seu nome é: {}".format(nome))
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
nomeTeste = (len(nome) - nome.count(' '))
print('Seu nome tem ao todo {} letras'.format(nomeTeste))
nomeDividido = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(nomeDividido[0])))