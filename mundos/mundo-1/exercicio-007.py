"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Curso em Vídeo (https://cursoemvideo.com)

PT-BR:
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media.
"""

# Recebendo valores
nota_1 = float(input('Digite a primeira nota do aluno: '))
nota_2 = float(input('Digite a segunda nota do aluno: '))

# Calculando media
media = (nota_1 + nota_2) / 2

# Resultado
print('A media do aluno foi de: {:.1f}'.format(media))
