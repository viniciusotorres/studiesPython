# CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA MÉDIA,
# MOSTRANDO UMA MENSAGEM NO FINAL, DE ACORDO COM A MÉDIA ATINGIDA:

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media > 5.0:
    print('O aluno foi aprovado!')
elif media > 8.0:
    print('O aluno foi aprovado com distinção!')
elif media < 5.0:
    print('O aluno foi reprovado!')
elif media == 5.0:
    print('O aluno está de recuperação!')
else:
    print('Digite um valor válido!')

print(f'A média do aluno foi: {media:.2f}')
