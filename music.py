import pygame
from pygame import mixer

#initialisation de mixer
pygame.init()
pygame.mixer.init()

def musique_1():
        mixer.music.load('musique/background.mp3')
        mixer.music.play(-1)
def planete_0():
        mixer.music.load("planete0.mp3")
        mixer.music.play(-1)
def planete_1():
        mixer.music.load("planete1.mp3")
        mixer.music.play(-1)
def planete_2():
        mixer.music.load("planete2.mp3")
        mixer.music.play(-1)
def planete_3():
        mixer.music.load("planete3.mp3")
        mixer.music.play(-1)
def planete_4():
        mixer.music.load("planete4.mp3")
        mixer.music.play(-1)
def planete_5():
        mixer.music.load("planete5.mp3")
        mixer.music.play(-1)
def planete_6():
        mixer.music.load("planete6.mp3")
        mixer.music.play(-1)
def musique_8():
        mixer.music.load('musique/musique_menu.mp3')
        mixer.music.play(-1)