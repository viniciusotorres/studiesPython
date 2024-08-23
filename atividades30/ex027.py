# FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, MOSTRANDO EM SEGUIDA O PRIMEIRO E O ÚLTIMO NOME SEPARADAMENTE.
# Ex: Ana Maria de Souza
# primeiro = Ana
# último = Souza

nome = input('Digite seu nome completo: ').strip()
nomeDividido = nome.split()
print('Primeiro nome: {}'.format(nomeDividido[0]))  # 0 é o primeiro elemento da lista
print('Último nome: {}'.format(nomeDividido[-1]))   # -1 é o último elemento da lista