# FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO COM SUA IDADE:
# - SE ELE AINDA VAI SE ALISTAR AO SERVIÇO MILITAR;
# - SE É A HORA DE SE ALISTAR;
# - SE JÁ PASSOU DO TEMPO DO ALISTAMENTO.
# SEU PROGRAMA TAMBÉM DEVERÁ MOSTRAR O TEMPO QUE FALTA OU QUE PASSOU DO PRAZO.

ano_de_nascimento = int(input('Digite o ano de nascimento: '))
idade = 2024 - ano_de_nascimento

if idade < 18:
    print(f'Você tem {idade} anos e ainda vai se alistar ao serviço militar.')
    print(f'Faltam {18 - idade} anos para você se alistar.')
elif idade == 18:
    print(f'Você tem {idade} anos e é hora de se alistar ao serviço militar.')
else:
    print(f'Você tem {idade} anos e já passou do tempo do alistamento.')
    print(f'Passaram-se {idade - 18} anos desde que você deveria ter se alistado.')