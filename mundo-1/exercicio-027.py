"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Curso em Vídeo (https://cursoemvideo.com)

PT-BR:
Faça um programa que leia o nome completo de uma pessoa, 
mostrando em seguida o primeiro e o último nome separadamente.
"""

# Recebendo valores
nome = input('Digite seu nome: ')

# Variaveis
primeiro_nome = nome.split()[0]
ultimo_nome = nome.split()[-1]

# Resultado
print('Seu primeiro nome é: {}\nSeu segundo nome é: {}'.format(primeiro_nome, ultimo_nome))
