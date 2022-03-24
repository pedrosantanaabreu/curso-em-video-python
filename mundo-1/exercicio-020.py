"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Curso em Vídeo (https://cursoemvideo.com)

PT-BR:
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. 
Faça um porgrama que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

#Importando random
import random

#Recebendo valores:
aluno_1 = input('Primeiro aluno: ')
aluno_2 = input('Segundo aluno: ')
aluno_3 = input('Terceiro aluno: ')
aluno_4 = input('Quarto aluno: ')

#Transformando em lista:
lista = [aluno_1, aluno_2, aluno_3, aluno_4]

#Sorteando uma sequencia aleatoria:
random.shuffle(lista)

#Resultado:
print('A ordem de apresentação sera: ')
print(lista)
