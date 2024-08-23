# ESCREVA UM PROGRAMA PARA APROVAR O EMPRÉSTIMO BANCÁRIO PARA
# A COMPRA DE UMA CASA. O PROGRAMA VAI PERGUNTAR O VALOR DA CASA,
# O SALÁRIO DO COMPRADOR E EM QUANTOS ANOS ELE VAI PAGAR. CALCULE
# O VALOR DA PRESTAÇÃO MENSAL, SABENDO QUE ELA NÃO PODE EXCEDER
# 30% DO SALÁRIO OU ENTÃO O EMPRÉSTIMO SERÁ NEGADO.

valor_da_casa = float(input('Qual o valor da casa? R$ '))
salario_do_comprador = float(input('Qual o salário do comprador? R$ '))
anos_de_pagemento = int(input('Em quantos anos ele vai pagar? '))
disponibilidade = salario_do_comprador * 0.3
prestacao = valor_da_casa / (anos_de_pagemento * 12)

if prestacao <= disponibilidade:
    print('Empréstimo aprovado!')
    print(f'Para pagar uma casa de R$ {valor_da_casa:.2f} em {anos_de_pagemento} anos, a prestação será de R$ {prestacao:.2f}')
else:
    print('Empréstimo negado!')


