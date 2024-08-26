# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO QUALQUER E MOSTRE O SEU FATORIAL.

number = int(input('Digite um número para calcular o seu fatorial: '))
count = number
factorial = 1

print(f'Calculando {number}! = ', end='')
while count > 0:
    print(f'{count}', end='')
    print(' x ' if count > 1 else ' = ', end='')
    factorial *= count
    count -= 1
print(factorial)
