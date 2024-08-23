# A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO
# DE UM ATLETA E MOSTRE SUA CATEGORIA, DE ACORDO COM A IDADE:
# - ATÉ 9 ANOS: MIRIM
# - ATÉ 14 ANOS: INFANTIL
# - ATÉ 19 ANOS: JUNIOR
# - ATÉ 25 ANOS: SÊNIOR
# - ACIMA: MASTER

ano_do_atleta = int(input('Digite o ano de nascimento do atleta: '))
idade_do_atleta = 2024 - ano_do_atleta

print('O atleta tem {} anos'.format(idade_do_atleta))

if idade_do_atleta < 9:
    print('O atleta é da categoria MIRIM')
elif idade_do_atleta <14:
    print('O atleta é da categoria INFANTIL')
elif idade_do_atleta < 19:
    print('O atleta é da categoria JUNIOR')
elif idade_do_atleta < 25:
    print('O atleta é da categoria SÊNIOR')
else:
    print('O atleta é da categoria MASTER')