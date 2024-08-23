# ESCREVE UM PROGRAMA QUE FAÇA O COMPUTADOR "PENSAR" EM UM
# NÚMERO INTEIRO ENTRE 0 E 5 E PEÇA PARA O USUÁRIO TENTAR DESCOBRIR QUAL FOI O
# NÚMERO ESCOLHIDO PELO COMPUTADOR. O PROGRAMA DEVERÁ ESCREVER NA TELA SE O
# USUÁRIO VENCEU OU PERDEU.

import random

numero = random.randint(0, 5)
print('Pensando em um número...')

numeroEscolhido = int(input('Advinhe um número entre 0 e 5:  '))

if numero == numeroEscolhido:
    print('Parabéns, você acertou o número!')
else:
    print(f'Você errou! O número escolhido foi {numero}')