"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Curso em Vídeo (https://cursoemvideo.com)

PT-BR:
Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada 
"""

# Recebendo informações
numero = int(input('Digite um numero: '))

# Iniciando loop de 0 atá 10
variavel_loop = 0
while variavel_loop < 11:
    print('{} x {:2} = {}'.format(numero, variavel_loop, (numero * variavel_loop)))
    variavel_loop += 1
