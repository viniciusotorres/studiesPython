# DESENVOLVA UM PROGRAMA QUE LEIA O NOME, IDADE E SEXO DE 4 PESSOAS. NO FINAL DO PROGRAMA, MOSTRE:
# - A MÉDIA DE IDADE DO GRUPO
# - QUAL É O NOME DO HOMEM MAIS VELHO
# - QUANTAS MULHERES TÊM MENOS DE 20 ANOS
#

media_idade = 0  # Inicializa a variável media_idade com 0
nome_homem_velho = ''  # Inicializa a variável nome_homem_velho com uma string vazia
idade_homem_velho = 0  # Inicializa a variável idade_homem_velho com 0
mulheres_menos_20 = 0  # Inicializa a variável mulheres_menos_20 com 0

for p in range(1, 5):  # Loop que itera 4 vezes (para 4 pessoas)
    nome = str(input(f'Digite o nome da {p}ª pessoa: '))  # Solicita o nome da pessoa e converte a entrada para uma string
    idade = int(input(f'Digite a idade da {p}ª pessoa: '))  # Solicita a idade da pessoa e converte a entrada para um número inteiro
    sexo = str(input(f'Digite o sexo da {p}ª pessoa [M/F]: ')).strip().upper()  # Solicita o sexo da pessoa, remove espaços em branco e converte para maiúsculas

    if p == 1:  # Se for a primeira pessoa
        media_idade = idade  # Define media_idade como a idade da primeira pessoa
        if sexo == 'M':  # Se o sexo for masculino
            nome_homem_velho = nome  # Define nome_homem_velho como o nome da primeira pessoa
            idade_homem_velho = idade  # Define idade_homem_velho como a idade da primeira pessoa
        if sexo == 'F' and idade < 20:  # Se o sexo for feminino e a idade for menor que 20
            mulheres_menos_20 += 1  # Incrementa o contador de mulheres com menos de 20 anos
    else:  # Para as demais pessoas
        media_idade += idade  # Adiciona a idade da pessoa à media_idade
        if sexo == 'M' and idade > idade_homem_velho:  # Se o sexo for masculino e a idade for maior que a idade_homem_velho
            nome_homem_velho = nome  # Atualiza nome_homem_velho com o nome da pessoa
            idade_homem_velho = idade  # Atualiza idade_homem_velho com a idade da pessoa
        if sexo == 'F' and idade < 20:  # Se o sexo for feminino e a idade for menor que 20
            mulheres_menos_20 += 1  # Incrementa o contador de mulheres com menos de 20 anos

media_idade /= 4  # Calcula a média de idade dividindo a soma das idades por 4

print(f'A média de idade do grupo é {media_idade:.1f} anos.')  # Exibe a média de idade do grupo
print(f'O homem mais velho é {nome_homem_velho} com {idade_homem_velho} anos.')  # Exibe o nome e a idade do homem mais velho
print(f'{mulheres_menos_20} mulheres têm menos de 20 anos.')  # Exibe o número de mulheres com menos de 20 anos