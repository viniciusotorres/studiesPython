# CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU NA TELA:
# [ 1 ] SOMAR
# [ 2 ] MULTIPLICAR
# [ 3 ] MAIOR
# [ 4 ] NOVOS NÚMEROS
# [ 5 ] SAIR DO PROGRAMA
# SEU PROGRAMA DEVERÁ REALIZAR A OPERAÇÃO SOLICITADA EM CADA CASO.

primerio_valor = int(input('Digite o primeiro valor: '))
segundo_valor = int(input('Digite o segundo valor: '))
print('[1] SOMAR')
print('[2] MULTIPLICAR')
print('[3] MAIOR')
print('[4] NOVOS NÚMEROS')
print('[5] SAIR DO PROGRAMA')
opcao = int(input('Escolha uma opção: '))


while opcao != 5:
    if opcao == 1:
        print('A soma dos números é: {}'.format(primerio_valor + segundo_valor))
    elif opcao == 2:
        print('A multiplicação dos números é {}'.format(primerio_valor * segundo_valor))
    elif opcao == 3:
        if primerio_valor > segundo_valor:
            print('O maior número é: {}'.format(primerio_valor))
        else:
            print('O maior número é: {}'.format(segundo_valor))
    elif opcao == 4:
        primerio_valor = int(input('Digite o primeiro valor: '))
        segundo_valor = int(input('Digite o segundo valor: '))
    else:
        print('Opção inválida. Tente novamente.')
    opcao = int(input('Escolha uma opção: '))

