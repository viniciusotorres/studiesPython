valor = float(input('Digite o valor em reais: '))
desconto = valor * 0.07
valor_com_desconto = valor - desconto
print(f'O valor com desconto de 7% é R${valor_com_desconto:.2f}')