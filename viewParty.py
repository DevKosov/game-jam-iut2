import pygame
from pygame.locals import *
from cmath import rect

class viewParty():
    def __init__(self):

        self.winWidth = 1024
        self.winHeight = 728
        self.font1 = pygame.font.Font("assets/font/Pixeltype.ttf", 70)
        self.font2 = pygame.font.Font("assets/font/Pixeltype.ttf", 30)
        self.background = [255,0,0]

    def draw(self,screen):
        screen.fill(self.background)