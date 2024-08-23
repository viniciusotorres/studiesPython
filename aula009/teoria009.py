# AULA SOBRE MANIPULAÇÃO DE STRING

# FATIAMENTO DE STRING
# Acessar um caractere de uma string
# Acessar um intervalo de caracteres de uma string
# Acessar um intervalo de caracteres de uma string com passo
# Acessar um intervalo de caracteres de uma string com passo negativo

# Exemplo 1
# Acessar um caractere de uma string
# frase = 'Curso em Vídeo Python'
# print(frase[3]) # s (posição 3)
# print(frase[3:13]) # so em Vídeo (posição 3 até 12)
# print(frase[3:13:2]) # se mV (posição 3 até 12 com passo 2)
# print(frase[:13]) # Curso em Víde (do início até a posição 12)
# print(frase[15:]) # Python
# print(frase[9::3]) # VePh (posição 9 até o final com passo 3)
#
# print(len(frase)) # 21 (tamanho da string)
# print(frase.count('o')) # 3 (quantidade de 'o' na string)
# print(frase.count('o', 0, 13)) # 1 (quantidade de 'o' na string do início até a posição 12)
# print(frase.find('deo')) # 11 (posição onde começa 'deo')
# print(frase.find('Android')) # -1 (não existe 'Android' na string)
#
# print('Curso' in frase) # True (existe 'Curso' na string)

# TRANSFORMAÇÃO DE STRING

# Exemplo 2
# Substituir uma palavra por outra
# frase = 'Curso em Vídeo Python'
# frase = '   Curso em Vídeo Python   '
# print(frase.replace('Python', 'Android')) # Curso em Vídeo Android (substitui 'Python' por 'Android')
# print(frase.upper()) # CURSO EM VÍDEO PYTHON (tudo maiúsculo)
# print(frase.lower()) # curso em vídeo python (tudo minúsculo)
# print(frase.capitalize()) # Curso em vídeo python (primeira letra maiúscula)
# print(frase.title()) # Curso Em Vídeo Python (primeira letra de cada palavra maiúscula)
# print(frase.strip()) # Curso em Vídeo Python (remove espaços desnecessários no início e no final)
# print(frase.rstrip()) # Curso em Vídeo Python (remove espaços desnecessários no final)
# print(frase.lstrip()) # Curso em Vídeo Python (remove espaços desnecessários no início)

# DIVISÃO DE STRING

# Exemplo 3
# Dividir uma string
# frase = 'Curso em Vídeo Python'
# print(frase.split()) # ['Curso', 'em', 'Vídeo', 'Python'] (divide a string por espaço e coloca em uma lista)
# dividido = frase.split()

# JUNTAR UMA STRING

# Exemplo 4
# Juntar uma string
# frase = 'Curso em Vídeo Python'
# print('-'.join(frase)) # C-u-r-s-o- -e-m- -V-í-d-e-o- -P-y-t-h-o-n (junta a string com '-')
# print('-'.join(dividido)) # Curso-em-Vídeo-Python (junta a lista com '-')

nome = 'Vinícius Tôrres'
# print(nome.replace('Tôrres', 'Henrique'))
# print(nome.upper())
# print(len(nome))
# print('-'.join(nome))
# print(nome.split())
# teste = nome.split()
# print(teste[0])
# print(teste[1])
# print(nome.upper().count('V'))
# print('Tôrres' in nome)
# print(nome.find('Tôrres'))
#
# print(nome.split())
# fraseNova = nome.split()
# print(fraseNova[0][3])













