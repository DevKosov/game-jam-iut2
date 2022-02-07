import pygame
from sys import exit

pygame.init()

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
        pygame.display.update()



if __name__ == "__main__":
    main()
