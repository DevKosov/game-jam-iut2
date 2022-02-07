import pygame
from sys import exit
from pygame.locals import *

pygame.init()
pygame.display.set_caption('GAME JAM 2022')

WIDTH, HEIGHT = 1024, 768
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    running = True
    clock = pygame.time.Clock()

    pygame.mixer.music.load("assets/audio/bgm/Town1.ogg")
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(fade_ms=2000)

    while running:
        clock.tick(FPS)
        WIN.fill('Yellow')

        titleScreen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
        pygame.display.update()

def titleScreen():

    RED = (255, 0, 0)
    btnPlay = Rect(100,100,100,100)
    pygame.draw.rect(WIN,RED,btnPlay)


if __name__ == "__main__":
    main()
