# MELHORE O JOGO DO DESAFIO 028 ONDE O COMPUTADOR VAI "PENSAR"
# EM UM NÚMERO ENTRE 0 E 10. SÓ QUE AGORA O JOGADOR VAI TENTAR
# ADIVINHAR ATÉ ACERTAR, MOSTRANDO NO FINAL QUANTOS PALPITES
# FORAM NECESSÁRIOS PARA VENCER.

import random
from time import sleep

numero_do_computador = random.randint(0, 10)

print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
sleep(2)
print('Pensando...')
sleep(1)
print('Pronto! Já pensei em um número. Tente adivinhar!')

number = int(input('Qual número eu pensei? '))

while number != numero_do_computador:
    if number < numero_do_computador:
        print('Mais... Tente novamente.')
    else:
        print('Menos... Tente novamente.')
    number = int(input('Qual número eu pensei? '))
print(f'Parabéns! Você acertou! O número que eu pensei foi {numero_do_computador}.')
