# CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE SETE PESSOAS.
# NO FINAL, MOSTRE QUANTAS PESSOAS AINDA NÃO ATINGIRAM A MAIORIDADE
# E QUANTAS JÁ SÃO MAIORES.
#

ano_atual = 2024  # Define o ano atual como 2024
maioridade = 18  # Define a idade de maioridade como 18 anos
menoridade = 0  # Inicializa o contador de pessoas menores de idade
maioridade_total = 0  # Inicializa o contador de pessoas maiores de idade

for i in range(1, 8):  # Loop que itera 7 vezes (para 7 pessoas)
    ano_nascimento = int(input(f'Digite o ano de nascimento da {i}ª: '))  # Solicita o ano de nascimento da pessoa
    idade = ano_atual - ano_nascimento  # Calcula a idade da pessoa
    if idade >= maioridade:  # Verifica se a pessoa é maior de idade
        maioridade_total += 1  # Incrementa o contador de maiores de idade
    else:  # Caso contrário
        menoridade += 1  # Incrementa o contador de menores de idade

print(f'{maioridade_total} pessoas são maiores de idade e {menoridade} são menores de idade.')  # Exibe o resultado final