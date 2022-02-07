from cmath import rect
import pygame
import Player

from sys import exit
from pygame.locals import *

pygame.init()
pygame.display.set_caption('GAME JAM 2022')

WIDTH, HEIGHT = 1024, 768
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))

player = pygame.sprite.GroupSingle()
player.add(Player.Player())

def main():
    running = True
    clock = pygame.time.Clock()

    pygame.mixer.music.load("assets/audio/bgm/Town1.ogg")
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(fade_ms=2000)

    while running:
        clock.tick(FPS)

        # Title screen
        titleScreen()
        player.draw(screen)
        player.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
        pygame.display.update()

def titleScreen():

    # background color of the window
    screen.fill('Yellow')

    # title
    font1 = pygame.font.Font("assets/font/Pixeltype.ttf", 70)
    TITLE = font1.render('Nom du jeu', 0, 'Black')
    TITLE_RECT = TITLE.get_rect(center=(WIDTH / 2, 100))
    WIN.blit(TITLE, TITLE_RECT)

    # button
    font2 = pygame.font.Font("assets/font/Pixeltype.ttf", 50)
    PLAY_BTN_LABEL = font1.render('PLAY', 0, 'Black')
    PLAY_BTN_RECT = PLAY_BTN_LABEL.get_rect(center=(WIDTH / 2, 300))
    WIN.blit(PLAY_BTN_LABEL,PLAY_BTN_RECT)

    CRED_BTN_LABEL = font1.render('CREDITS', 0, 'Black')
    CRED_BTN_RECT = CRED_BTN_LABEL.get_rect(center=(WIDTH / 2, 400))
    WIN.blit(CRED_BTN_LABEL,CRED_BTN_RECT)

    EXIT_BTN_LABEL = font1.render('EXIT', 0, 'Black')
    EXIT_BTN_RECT = EXIT_BTN_LABEL.get_rect(center=(WIDTH / 2, 500))
    WIN.blit(EXIT_BTN_LABEL,EXIT_BTN_RECT)

if __name__ == "__main__":
    main()
