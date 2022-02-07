import pygame
from pygame.locals import *
from cmath import rect

class viewCredits():
    def __init__(self):

        self.winWidth = 1024
        self.winHeight = 728
        self.font1 = pygame.font.Font("assets/font/Pixeltype.ttf", 70)
        self.font2 = pygame.font.Font("assets/font/Pixeltype.ttf", 30)

    def draw(self,screen):

        # Title
        TITLE = self.font1.render('CREDITS', 0, 'Black')
        TITLE_RECT = TITLE.get_rect(center=(self.winWidth / 2, 100))
        screen.blit(TITLE, TITLE_RECT)
        
        # Back to menu
        BACK = self.font2.render('BACK TO MENU', 0, 'Black')
        BACK_RECT = BACK.get_rect(center=(self.winWidth / 12, 30))
        self.back_event_credit = screen.blit(BACK, BACK_RECT)