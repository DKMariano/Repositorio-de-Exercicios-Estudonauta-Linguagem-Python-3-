# Desafio 021
# Faça um programa que abra e reproduza o audio de um arquivo mp3.
import pygame
pygame.init()
pygame.mixer.music.load('takinghobbit.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
