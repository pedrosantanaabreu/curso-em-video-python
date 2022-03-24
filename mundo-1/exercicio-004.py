"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Curso em Vídeo (https://cursoemvideo.com)

PT-BR:
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações 
possíveis sobre ela
"""

frase = input('Digite algo: ')
print('É alfanumerico?', frase.isalnum())
print('É numerico?', frase.isnumeric())
print('É alfabético?', frase.isalpha())
print('É maiusculas?', frase.isupper())
print('É minusculas?', frase.islower())
print('So tem espaços?', frase.isspace())
print('Está captalizada (maiúsculo e minusculo)', frase.istitle())
