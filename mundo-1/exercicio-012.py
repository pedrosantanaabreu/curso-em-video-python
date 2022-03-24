"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Curso em Vídeo (https://cursoemvideo.com)

PT-BR:
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

# Recebendo valores
preco = float(input('Digite o valor do produto: R$'))
desconto = 5

# Calculando valor final do produto
total =  preco - (preco * (desconto / 100))

# Exibindo resultado
print('O produto de valor {:.2f} reais, ficou por {:.2f} reais com o desconto de {}%'.format(preco, total, desconto))
