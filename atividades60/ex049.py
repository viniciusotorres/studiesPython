# REFAÇA O DESAFIO 009, MOSTRANDO A TABUADA DE UM NÚMERO QUE O USUÁRIO ESCOLHER,
# SÓ QUE AGORA UTILIZANDO UM LAÇO FOR.
#

number_choice = int(input('Digite um número para ver sua tabuada: '))

for c in range (0, 9+1):
    print(f'{number_choice} x {c} = {number_choice * c}')
