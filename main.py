import pygame
import Player

from sys import exit
from pygame.locals import *

pygame.init()
pygame.display.set_caption('GAME JAM 2022')

WIDTH, HEIGHT = 1024, 768
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
        pygame.display.update()

def titleScreen():

    # background color of the window
    WIN.fill('Yellow')

    # font
    font = pygame.font.Font("assets/font/Pixeltype.ttf", 70)

    # title
    TITLE = font.render('Nom du jeu', 0, 'Black')
    TITLE_RECT = TITLE.get_rect(center=(WIDTH / 2, 50))
    WIN.blit(TITLE, TITLE_RECT)

    # button play


if __name__ == "__main__":
    main()
