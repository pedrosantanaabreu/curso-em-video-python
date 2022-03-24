"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Curso em Vídeo (https://cursoemvideo.com)

PT-BR:
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo 
retângulo, calcule e mostre o comprimento da hipotenusa.
"""

#Importando modulo math
import math

#Recebendo valores:
cateto_oposto = float(input('Digite o cateto oposto: '))
cateto_adjacente = float(input('Digite o cateto adjacente: '))

#Declarando variaveis:
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

#Resultado:
print('A hipotenusa vai medir: {:.2f}'.format(math.hypot(cateto_oposto, cateto_adjacente)))
