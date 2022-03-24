"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Curso em Vídeo (https://cursoemvideo.com)

PT-BR:
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
"""

# Recebendo valor
numero = int(input('Digite o numero: '))

# Declarando variaveis
antecessor = numero - 1
sucessor = numero + 1

# Resultado
print('Seu sucessor é: {}\nNumero digitado: {}\nSeu antecessor é {}'.format(sucessor , numero, antecessor))
