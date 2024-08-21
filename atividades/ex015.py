kmPercorridos = float(input('Quantos km foram percorridos? '))
diasAlugados = int(input('Por quantos dias o carro foi alugado? '))

preco = (diasAlugados * 60) + (kmPercorridos * 0.15)

print(f'O total a pagar é de R${preco:.2f}')
