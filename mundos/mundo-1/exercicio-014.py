"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Curso em Vídeo (https://cursoemvideo.com)

PT-BR:
Escreva um programa que converta uma temperatura digitada em C para F.
"""

# Recebendo valores
celsius = float(input('Digite a temperatura em celsius: '))

# Convertendo
fahrenheit = (celsius * 9/5) + 32

# Resultado
print('{:.1f} graus celsius equivalem a {:.1f} graus fahrenheit'.format(celsius, fahrenheit))
