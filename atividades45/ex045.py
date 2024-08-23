# CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR JOGAR JOKENPÔ COM VOCÊ.

from random import choice
from time import sleep

print('VAMOS JOGAR JOKENPÔ!')
print('Escolha uma opção:')
print('[1] Pedra')
print('[2] Papel')
print('[3] Tesoura')

sua_opcao = int(input('Digite a sua opção: '))

opcoes = ['Pedra', 'Papel', 'Tesoura']

opcao_computador = choice(opcoes)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(3)

print(f'Você escolheu {opcoes[sua_opcao - 1]}')
print(f'O computador escolheu {opcao_computador}')

if sua_opcao == 1:
    if opcao_computador == 'Pedra':
        print('Empate!')
    elif opcao_computador == 'Papel':
        print('Você perdeu!')
    elif opcao_computador == 'Tesoura':
        print('Você ganhou!')

if sua_opcao == 2:
    if opcao_computador == 'Pedra':
        print('Você ganhou!')
    elif opcao_computador == 'Papel':
        print('Empate!')
    elif opcao_computador == 'Tesoura':
        print('Você perdeu!')

if sua_opcao == 3:
    if opcao_computador == 'Pedra':
        print('Você perdeu!')
    elif opcao_computador == 'Papel':
        print('Você ganhou!')
    elif opcao_computador == 'Tesoura':
        print('Empate!')

if sua_opcao < 1 or sua_opcao > 3:
    print('Opção inválida!')

print('FIM DE JOGO!')