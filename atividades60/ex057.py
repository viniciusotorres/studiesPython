#  FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA,
#  MAS SÓ ACEITE OS VALORES 'M' OU 'F'. CASO ESTEJA ERRADO,
#  PEÇA A DIGITAÇÃO NOVAMENTE ATÉ TER UM VALOR CORRETO.

# sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]

sexo = input('Informe seu sexo [M/F]: ').strip() # strip() remove espaços em branco
while sexo != 'F' and sexo != 'M': # enquanto o sexo for diferente de F e M
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0] # strip() remove espaços em branco

print(f'Sexo {sexo} registrado com sucesso.') # se o sexo for F ou M, imprime a mensagem

