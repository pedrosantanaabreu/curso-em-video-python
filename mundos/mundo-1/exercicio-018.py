"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Curso em Vídeo (https://cursoemvideo.com)

PT-BR:
Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.
"""

# Importando math
import math

# Recebendo informações
angulo = float(input('Digite o angulo: '))

# Converter para radianos
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

# Resultado
print('Seno: {:.2f}, Cosseno: {:.2f}, Tangente: {:.2f}'.format(seno, cosseno, tangente))
