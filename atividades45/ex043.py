# DESENVOLVA UMA LÓGICA QUE LEIA O PESO E A ALTURA DE UMA PESSOA,
# CALCULE SEU IMC E MOSTRE SEU STATUS, DE ACORDO COM A TABELA ABAIXO:
# - ABAIXO DE 18.5: ABAIXO DO PESO
# - ENTRE 18.5 E 25: PESO IDEAL
# - 25 ATÉ 30: SOBREPESO
# - 30 ATÉ 40: OBESIDADE
# - ACIMA DE 40: OBESIDADE MÓRBIDA

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Seu IMC é {imc:.2f} e você está abaixo do peso.')
elif imc < 25:
    print(f'Seu IMC é {imc:.2f} e você está no peso ideal.')
elif imc < 30:
    print(f'Seu IMC é {imc:.2f} e você está com sobrepeso.')
elif imc < 40:
    print(f'Seu IMC é {imc:.2f} e você está com obesidade.')
else:
    print(f'Seu IMC é {imc:.2f} e você está com obesidade mórbida.')