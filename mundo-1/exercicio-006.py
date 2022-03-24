"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Curso em Vídeo (https://cursoemvideo.com)

PT-BR:
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""

# Recebendo numero
numero = int(input('Digite um numero: '))

# Declarando variaveis
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1 / 2)

# Resultado
print('O numero digitado foi: {} \nO dobro é: {} \nO triplo é: {} \nSua raiz quadrada é: {:.2f}'.format(numero, dobro, triplo, raiz))
