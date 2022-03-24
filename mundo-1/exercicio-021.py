"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Curso em Vídeo (https://cursoemvideo.com)

PT-BR:
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
"""

#Importando pygame #pip install pygame
import pygame

#Iniciando pygame:
pygame.init()

#Selecionando audio:
pygame.mixer.music.load('exercicio-021uepa.mp3')

#Iniciando o audio:
pygame.mixer.music.play()

#Fim do programa:
input()
