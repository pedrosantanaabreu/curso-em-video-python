"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Curso em Vídeo (https://cursoemvideo.com)

PT-BR:
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
"""

# Recebendo valor
cidade = str(input('Digite o nome da sua cidade: ')).strip().upper()

# Declarando variavel
resultado = bool(cidade[:5] == 'SANTO')

# Resultado
print('A cidade começa com o nome Santo? {}'.format(bool(resultado)))
