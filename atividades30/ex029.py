# ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO.
# SE ELE ULTRAPASSAR 80KM/H, MOSTRE UMA MENSAGEM DIZENDO
# QUE ELE FOI MULTADO. A MULTA VAI CUSTAR R$7,00 POR CADA KM
# ACIMA DO LIMITE.

velocidade = float(input('Digite a velocidade do carro em km:  '))

if velocidade >= 80:
    print('Carro multado por ter ultrapassado o limite de velocidade! Velocidade atingida: {} '.format(velocidade))
else:
    print('Sem multa!')

valor_da_multa = velocidade * 0.7

print(f'A multa ficou no valor total de: R${valor_da_multa:2f} Cobramos por cada Km, R$7,00')
