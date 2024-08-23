# ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO,
# CONSIDERANDO O SEU PREÇO NORMAL E CONDIÇÃO DE PAGAMENTO:
# - À VISTA DINHEIRO/CHEQUE: 10% DE DESCONTO
# - À VISTA NO CARTÃO: 5% DE DESCONTO
# - EM ATÉ 2X NO CARTÃO: PREÇO NORMAL
# - 3X OU MAIS NO CARTÃO: 20% DE JUROS

preco = float(input('Digite o preço do produto: R$ '))
print('''
[1] À vista dinheiro/cheque
[2] À vista no cartão
[3] Em até 2x no cartão
[4] 3x ou mais no cartão
''')
opcao = int(input('Digite a opção de pagamento: '))

if opcao ==1:
    desconto = preco * 0.10
    preco_final = preco - desconto
    print(f'O valor a ser pago é R$ {preco_final:.2f}')
elif opcao == 2:
    desconto = preco * 0.05
    preco_final = preco - desconto
    print(f'O valor a ser pago é R$ {preco_final:.2f}')
elif opcao == 3:
    preco_final = preco / 2
    print(f'O valor a ser pago em 2x é R$ {preco_final:.2f}')
elif opcao == 4:
    quantidade_parcelas = int(input('Digite a quantidade de parcelas: '))
    preco_final = preco / quantidade_parcelas
    juros = preco_final * 0.20
    preco_final += juros
    print(f'O valor a ser pago em {quantidade_parcelas}x é R$ {preco_final:.2f}')
else:
    print('Opção inválida!')
