from cmath import rect
import pygame
import sprite
import os
import viewMenu
import viewOption
import viewParty
import viewCredits

from sys import exit
from pygame.locals import *

pygame.init()
pygame.display.set_caption('GAME JAM 2022')

WIDTH, HEIGHT = 1024, 768
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))

player = pygame.sprite.GroupSingle()
player.add(sprite.Player())


BACKGROUND = (173, 239, 255)
BACKGROUND2 = pygame.image.load('assets/img/tests/backgroundTest2.png')

def main():
    running = True
    clock = pygame.time.Clock()

    pygame.mixer.music.load("assets/audio/bgm/Town1.ogg")
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(fade_ms=2000)

    pygame.mouse.set_visible(False)

    MENU = 1
    PARTY = 0
    OPTIONS = 0
    CREDITS = 0

    while running:
        clock.tick(FPS)

        screen.fill(BACKGROUND)

        ################################################################################################################
        # VIEW
        ################################################################################################################

        if (MENU==1):
            menu = viewMenu.viewMenu()
            menu.draw(screen)
        
        elif (OPTIONS==1):
            option = viewOption.viewOption()
            option.draw(screen)
        
        elif (CREDITS==1):
            credit = viewCredits.viewCredits()
            credit.draw(screen)

        elif (PARTY==1):
            # party = viewParty.viewParty()
            # party.draw(screen)
            screen.blit(BACKGROUND2,(-1024,-1024))
            player.update()
            player.draw(screen)

        ################################################################################################################
        # EVENT LISTENER
        ################################################################################################################

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONUP and event.button==1 and menu.exit_event.collidepoint(event.pos):
                running = False
                exit()
            if event.type == pygame.KEYUP or event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                player.sprites().__getitem__(0).player_input(event)
            elif event.type == pygame.MOUSEBUTTONUP and event.button==1 and menu.play_event.collidepoint(event.pos):
                MENU=0
                CREDITS=0
                OPTIONS=0
                PARTY=1
            elif event.type == pygame.MOUSEBUTTONUP and event.button==1 and menu.opt_event.collidepoint(event.pos) and MENU==1:
                MENU=0
                PARTY=0
                CREDITS=0
                OPTIONS=1
            elif event.type == pygame.MOUSEBUTTONUP and event.button==1 :
                if menu.cred_event.collidepoint(event.pos) and MENU==1:
                    MENU=0
                    PARTY=0
                    OPTIONS=0
                    CREDITS=1
            elif event.type == pygame.MOUSEBUTTONUP and event.button==1:
                if  option.back_event.collidepoint(event.pos):
                    OPTIONS=0
                    PARTY=0
                    CREDITS=0
                    MENU=1
            elif event.type == pygame.MOUSEBUTTONUP and event.button==1:
                if credit.back_event_credit.collidepoint(event.pos):
                    CREDITS=0
                    OPTIONS=0
                    PARTY=0
                    MENU=1

        ################################################################################################################
        # CURSOR
        ################################################################################################################

        mouse_pos = pygame.mouse.get_pos()
        CURSOR = pygame.transform.scale(pygame.image.load(os.path.join('assets/img/cursor', 'viewfinder.png')).convert_alpha(), (100, 100))
        CURSOR_RECT = CURSOR.get_rect()
        CURSOR_RECT.center = mouse_pos
        screen.blit(CURSOR, CURSOR_RECT)

        pygame.display.update()

if __name__ == "__main__":
    main()
