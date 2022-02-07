import pygame
from pygame.locals import *
from cmath import rect

class viewMenu():
    def __init__(self):

        self.winWidth = 1024
        self.winHeight = 728
        self.font1 = pygame.font.Font("assets/font/Pixeltype.ttf", 70)
        self.font2 = pygame.font.Font("assets/font/Pixeltype.ttf", 50)

    def draw(self,screen):

        TITLE = self.font1.render('Nom du jeu', 0, 'Black')
        TITLE_RECT = TITLE.get_rect(center=(self.winWidth / 2, 100))
        screen.blit(TITLE, TITLE_RECT)

        PLAY_BTN_LABEL = self.font2.render('PLAY', 0, 'Black')
        PLAY_BTN_RECT = PLAY_BTN_LABEL.get_rect(center=(self.winWidth / 2, 300))
        self.play_event = screen.blit(PLAY_BTN_LABEL,PLAY_BTN_RECT)

        OPT_BTN_LABEL = self.font2.render('OPTIONS', 0, 'Black')
        OPT_BTN_RECT = OPT_BTN_LABEL.get_rect(center=(self.winWidth / 2, 400))
        self.opt_event = screen.blit(OPT_BTN_LABEL,OPT_BTN_RECT)

        CRED_BTN_LABEL = self.font2.render('CREDITS', 0, 'Black')
        CRED_BTN_RECT = CRED_BTN_LABEL.get_rect(center=(self.winWidth / 2, 500))
        self.cred_event = screen.blit(CRED_BTN_LABEL,CRED_BTN_RECT)

        EXIT_BTN_LABEL = self.font2.render('EXIT', 0, 'Black')
        EXIT_BTN_RECT = EXIT_BTN_LABEL.get_rect(center=(self.winWidth / 2, 600))
        self.exit_event = screen.blit(EXIT_BTN_LABEL,EXIT_BTN_RECT)

