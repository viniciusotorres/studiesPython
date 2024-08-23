# REFAÇA O DESAFIO 035 DOS TRIÂNGULOS, ACRESCENTANDO O RECURSO DE MOSTRAR QUE TIPO DE TRIÂNGULO SERÁ FORMADO:
# - EQUILÁTERO: TODOS OS LADOS IGUAIS
# - ISÓSCELES: DOIS LADOS IGUAIS
# - ESCALENO: TODOS OS LADOS DIFERENTES

print('Analisador de Triângulos')
print('-=' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

lados_diferentes = r1 != r2 != r3 != r1
lados_iguais = r1 == r2 == r3
dois_lados_iguais = r1 == r2 or r1 == r3 or r2 == r3

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if lados_iguais:
        print('EQUILÁTERO!')
    elif lados_diferentes:
        print('ESCALENO!')
    elif dois_lados_iguais:
        print('ISÓSCELES!')
