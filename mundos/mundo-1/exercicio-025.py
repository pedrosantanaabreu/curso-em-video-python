"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Curso em Vídeo (https://cursoemvideo.com)

PT-BR:
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""

# Recebendo valor
nome = str(input('Digite seu nome: ')).strip()

# Variaveis
dividir = nome.upper().split()

# Retorna valor boleano
resultado = bool('SILVA' in dividir)

# Resultado
print('Você tem Silva no nome? {}'.format(resultado))
