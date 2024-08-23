# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA OU NÃO COM O NOME "SANTO"

cidade = input('Digite o nome de uma cidade: ').strip()
print('A cidade começa com "Santo"? {}'.format('Santo' in cidade[:5].title()))