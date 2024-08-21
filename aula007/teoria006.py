# OPERAÇÕES ARITMÉTICAS
# O QUE SÃO OPERAÇÕES ARITMÉTICAS?
# São operações matemáticas que podem ser realizadas com números.

# SOMA (+)
# SUBTRAÇÃO (-)
# MULTIPLICAÇÃO (*)
# DIVISÃO (/)
# DIVISÃO INTEIRA (//)
# POTENCIAÇÃO (**)
# RESTO DA DIVISÃO (%)

# == Serve para comparar valores
# = Serve para atribuir valores

# ORDENS DE PRECEDÊNCIA
# 1. ()
# 2. **
# 3. * / // %
# 4. + -

# Exemplo de uso de operações aritméticas

# n1 = 5
# n2 = 3
# n3 = 2

# operacao = n1 + n2 * n3
# resultado = 11

# print('O resultado da operação {} + {} * {} é equivalente a {}!'.format(n1, n2, n3, operacao))
#
# n4 = 3
# n5 = 4
#
# operacao = n2 * n1 + n5 ** n3
#
# print('O resultado da operação {} * {} + {} ** {} é equivalente a {}!'.format(n2, n1, n5, n3, operacao))
#
# operacao = n2 * (n1 + n5) ** n3
#
# print('O resultado da operação {} * ({} + {}) ** {} é equivalente a {}!'.format(n2, n1, n5, n3, operacao))
#
# # NO PYTHON NÃO EXISTE LIMITAÇÃO DE MEMÓRIA PARA ARMAZENAMENTO DE NÚMEROS
# # O PYTHON É CAPAZ DE ARMAZENAR QUALQUER NÚMERO, INDEPENDENTE DO TAMANHO

# nome = input('Digite seu nome: ')
# # CENTRALIZANDO O TEXTO
# print('É um prazer te conhecer, {:^20}!'.format(nome))
# # ALINHANDO O TEXTO PARA A ESQUERDA
# print('É um prazer te conhecer, {:>20}!'.format(nome))
# # ALINHANDO O TEXTO PARA A DIREITA
# print('É um prazer te conhecer, {:<20}!'.format(nome))
# # PREENCHENDO OS ESPAÇOS VAZIOS COM O CARACTERE #
# print('É um prazer te conhecer, {:#^20}!'.format(nome))

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
r = n1 % n2

print('A soma entre {} e {} é igual a {}!'.format(n1 , n2, s), end=' >> ')
print(' A multiplicação entre {} e {} é igual a {}!'.format(n1, n2, m), end=' >> ')
print(' A divisão entre {} e {} é igual a {:.2f}!'.format(n1, n2, d), end=' >> ')
print(' A divisão inteira ente {} e {} é igual {}!'.format(n1, n2, di), end=' >> ')
print (' A potenciação de {} elevado a {} é igual a {}!'.format(n1, n2, e), end=' >> ')
print('O resto da divisão entre {} e {} é igual a {}!'.format(n1, n2, r))


