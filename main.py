import pygame
from sys import exit

pygame.init()

WIDTH, HEIGHT = 1024, 768
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

backgroundsound = pygame.mixer.Sound('assets/audio/bgm/Town2.ogg')

def main():
    running = True
    clock = pygame.time.Clock()
    backgroundsound.play()

    while running:
        clock.tick(FPS)
        WIN.fill('Yellow')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
        pygame.display.update()


if __name__ == "__main__":
    main()
