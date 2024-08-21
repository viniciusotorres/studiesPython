# TIPOS PRIMITIVOS E SAÍDA DE DADOS

# TIPOS PRIMITIVOS BÁSICOS

# -> int: números inteiros  (positivos, negativos e zero)
# -> float: números reais   (ponto flutuante)
# -> bool: valores lógicos (True ou False)
# -> str: cadeias de caracteres ('')

# n1 = input('Digite um número: ')
#
# print(type(n1))

# A função input() sempre retorna uma string

# n1 = int(input('Digite um número: '))
# print(type(n1))

# A função input() deve ser tipada para o tipo desejado


# n1 = input('Digite um número: ')
# n2 = input('Digite outro número: ')
# s = n1 + n2
#
# print('A soma entre', n1, 'e', n2, 'é igual a', s)

# Aqui está concatenando as strings



# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite outro número: '))
# s = n1 + n2
#
# print('A soma entre {} e {} é igual {}!'.format(n1, n2, s))

# {} → espaços reservados para os valores das variáveis
# .format() -> função que formata a saída de dados
# Aqui estará somando os valores das variáveis

# Exemplo de saída de dados

# print('A soma vale', s)
# print('A soma entre', n1, 'e', n2, 'é igual a', s)
# print('A soma entre {} e {} é igual {}!'.format(n1, n2, s))
# print('A soma entre {0} e {1} é igual {2}!'.format(n1, n2, s))
# print('A soma entre {2} e {0} é igual {1}!'.format(n1, n2, s))
# print('A soma entre {0} e {0} é igual {0}!'.format(n1, n2, s))
# print('A soma entre {n1} e {n2} é igual {s}!'.format(n1, n2, s))
# print('A soma entre {n1} e {n2} é igual {s}!'.format(n1=n1, n2=n2, s=s))

# n = float(input('Digite um valor: '))
# print(n)
# print(type(n))

# Aqui está convertendo o valor digitado para float

# n = bool(input('Digite um valor: '))
# print(n)
# print(type(n))

# Aqui está convertendo o valor digitado para bool
# Se for digitado algum valor, será True
# Se for digitado nenhum valor, será False

# n = input('Digite algo: ')
# print(n.isupper())
# print(n.isnumeric())
# print(n.isalpha())
# print(n.isalnum())
# print(n.islower())


# isnumeric() → verifica se o valor digitado é numérico
# isalpha() → verifica se o valor digitado é alfabético
# isalnum() → verifica se o valor digitado é alfanumérico
# isupper() → verifica se o valor digitado está em maiúsculo
# islower() → verifica se o valor digitado está em minúsculo





