from cmath import rect
import pygame
import Player
import os

from sys import exit
from pygame.locals import *

pygame.init()
pygame.display.set_caption('GAME JAM 2022')

WIDTH, HEIGHT = 1024, 768
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))

player = pygame.sprite.GroupSingle()
player.add(Player.Player())

CURSOR = pygame.transform.scale(pygame.image.load(os.path.join('assets/img/cursor', 'viewfinder.png')).convert_alpha(), (100, 100))
CURSOR_RECT = CURSOR.get_rect()

BACKGROUND = (173, 239, 255)

def main():
    running = True
    clock = pygame.time.Clock()

    pygame.mixer.music.load("assets/audio/bgm/Town1.ogg")
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(fade_ms=2000)

    pygame.mouse.set_visible(False)

    while running:
        clock.tick(FPS)

        # Title screen
        titleScreen()

        player.draw(screen)

        # Cursor
        mouse_pos = pygame.mouse.get_pos()
        CURSOR_RECT.center = mouse_pos
        screen.blit(CURSOR, CURSOR_RECT)

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                player.update()

        pygame.display.update()

def titleScreen():

    # background color of the window
    screen.fill(BACKGROUND)

    # font
    font = pygame.font.Font("assets/font/Pixeltype.ttf", 70)

    # Title
    font1 = pygame.font.Font("assets/font/Pixeltype.ttf", 70)
    TITLE = font1.render('Nom du jeu', 0, 'Black')
    TITLE_RECT = TITLE.get_rect(center=(WIDTH / 2, 100))
    screen.blit(TITLE, TITLE_RECT)

    # Button PLAY
    font2 = pygame.font.Font("assets/font/Pixeltype.ttf", 50)
    PLAY_BTN_LABEL = font1.render('PLAY', 0, 'Black')
    PLAY_BTN_RECT = PLAY_BTN_LABEL.get_rect(center=(WIDTH / 2, 300))
    PLAY_EVENT = screen.blit(PLAY_BTN_LABEL,PLAY_BTN_RECT)

    # Button OPTIONS
    OPT_BTN_LABEL = font1.render('OPTIONS', 0, 'Black')
    OPT_BTN_RECT = OPT_BTN_LABEL.get_rect(center=(WIDTH / 2, 400))
    screen.blit(OPT_BTN_LABEL,OPT_BTN_RECT)

    # Button CREDITS
    CRED_BTN_LABEL = font1.render('CREDITS', 0, 'Black')
    CRED_BTN_RECT = CRED_BTN_LABEL.get_rect(center=(WIDTH / 2, 500))
    screen.blit(CRED_BTN_LABEL,CRED_BTN_RECT)

    # Button EXIT
    EXIT_BTN_LABEL = font1.render('EXIT', 0, 'Black')
    EXIT_BTN_RECT = EXIT_BTN_LABEL.get_rect(center=(WIDTH / 2, 600))
    EXIT_EVENT = screen.blit(EXIT_BTN_LABEL,EXIT_BTN_RECT)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONUP and event.button==1 and EXIT_EVENT.collidepoint(event.pos):
            running = False
            exit()
        elif event.type == pygame.MOUSEBUTTONUP and event.button==1 and PLAY_EVENT.collidepoint(event.pos):
            print("PLAY CLICKED")


if __name__ == "__main__":
    main()