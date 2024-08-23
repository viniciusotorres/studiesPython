# FAÇA UM PROGRAMA QUE LEIA O PESO DE 5 PESSOAS. NO FINAL, MOSTRE QUAL FOI O MAIOR E O MENOR PESO LIDOS.

maior_peso = 0  # Inicializa a variável maior_peso com 0
menor_peso = 0  # Inicializa a variável menor_peso com 0

for p in range(1, 6):  # Loop que itera 5 vezes (para 5 pessoas)
    peso = float(input(f'Digite o peso da {p}ª pessoa: '))  # Solicita o peso da pessoa e converte a entrada para um número de ponto flutuante
    if p == 1:  # Se for a primeira pessoa
        maior_peso = peso  # Define o maior_peso como o peso da primeira pessoa
        menor_peso = peso  # Define o menor_peso como o peso da primeira pessoa
    else:  # Para as demais pessoas
        if peso > maior_peso:  # Verifica se o peso atual é maior que o maior_peso registrado
            maior_peso = peso  # Atualiza o maior_peso
        if peso < menor_peso:  # Verifica se o peso atual é menor que o menor_peso registrado
            menor_peso = peso  # Atualiza o menor_peso

print(f'O maior peso lido foi {maior_peso}Kg e o menor peso lido foi {menor_peso}Kg.')  # Exibe o maior e o menor peso lidos