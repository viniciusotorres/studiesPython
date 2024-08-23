#DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTÂNCIA DE
# UMA VIAGEM EM KM. CALCULE O PREÇO DA PASSAGEM,
# COBRANDO R$0,50 POR KM PARA VIAGENS DE ATÉ 200KM E R$0,45
# PARA VIAGENS MAIS LONGAS.

distanciaViagem = float(input('Qual a distância da viagem em KM? '))
precoPassagem = distanciaViagem * 0.50 if distanciaViagem <= 200 else distanciaViagem * 0.45

print(f'O preço da passagem é R${precoPassagem:.2f}')