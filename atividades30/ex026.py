# FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:
# - QUANTAS VEZES APARECE A LETRA "A"
# - EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ
# - EM QUE POSIÇÃO ELA APARECE A ÚLTIMA VEZ

frase = input("Digite uma frase: ").strip().lower()
print("Quantidade: {}".format(frase.count('a')))
print('Primeira posição: {}'.format(frase.find('a')+1))
print('Última posição: {}'.format(frase.rfind('a')+1))