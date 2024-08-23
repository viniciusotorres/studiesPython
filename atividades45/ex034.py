#ESCREVA UM PROGRAMA QUE PERGUNTA  O SALÁRIO DE UM FUNCIONÁRIO E CALCULE O VALOR DO SEU AUMENTO.
# PARA SALÁRIOS SUPERIORES A R$1250,00, CALCULE UM AUMENTO DE 10%.
# PARA OS INFERIORES OU IGUAIS, O AUMENTO É DE 15%.

salario = float(input('Digite o salário do funcionário: '))
if salario >= 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

novoSalario = salario + aumento

print(f'O salário do funcionário era R${salario:.2f}')
print(f'O aumento foi de R${aumento:.2f}')
print(f'O novo salário é R${novoSalario:.2f}')