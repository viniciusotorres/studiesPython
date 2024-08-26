# ESTRUTURA DE REPETIÇÃO WHILE

# Estrutura de repetição while (enquanto)
# O while é uma estrutura de repetição que executa um bloco de código enquanto a condição for verdadeira.
# Quando a condição for falsa, o bloco de código é interrompido.

# Sintaxe:
# while condição:
#     bloco de código

# Exemplo 1:
# Imprimir os números de 1 a 5.
# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# Exemplo 2:
# Imprimir os números de 1 a 10.
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# n = 1 # Inicialização da variável n.
# while n != 0: # Condição de parada.
#     n = int(input('Digite um número: ')) # Entrada de dados.
#     print(n) # Saída de dados.

# resposta = 'NÃO' # Inicialização da variável resposta. A resposta inicial é 'NÃO'.
# while resposta != 'SIM': # Condição de parada. Enquanto a resposta for diferente de 'SIM', o bloco de código será executado.
#     resposta = input('QUER CASAR COMIGO? (SIM/NÃO): ').upper() # Entrada de dados. A resposta é convertida para maiúsculo.
#
# print('FIM')

# Exemplo 3:

n = 1 # Inicialização da variável n.
par = impar = 0 # Inicialização das variáveis par e impar.
while n != 0:
    n = int(input('Digite um número: ')) # Entrada de dados.
    if n != 0:
        if n % 2 == 0: # Se o resto da divisão de n por 2 for igual a 0.
            par += 1 # Incrementa a variável par.
        else:
            impar += 1 # Incrementa a variável impar.

print('Quantidade de números pares:', par)
print('Quantidade de números ímpares:', impar)
print('FIM')