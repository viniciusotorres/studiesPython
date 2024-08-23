# ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER
# E PEÇA PARA O USUÁRIO ESCOLHER QUAL SERÁ A BASE DE CONVERSÃO:

number = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: ')
print('[1] converter para BINÁRIO')
print('[2] converter para OCTAL')
print('[3] converter para HEXADECIMAL')
option = int(input('Sua opção: '))

if option == 1:
    print(f'{number} convertido para BINÁRIO é igual a {bin(number)[2:]}')
elif option == 2:
    print(f'{number} convertido para OCTAL é igual a {oct(number)[2:]}')
elif option == 3:
    print(f'{number} convertido para HEXADECIMAL é igual a {hex(number)[2:]}')
else:
    print('Opção inválida, tente novamente!')