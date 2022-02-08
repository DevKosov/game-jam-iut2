#from cmath import rect
import pygame, os
from sprite import *
import sys

from sys import exit
from pygame.locals import *

pygame.init()
pygame.display.set_caption('GAME JAM 2022')

WIDTH, HEIGHT = 1024, 768
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (150, 252, 255)
tilemap = ['.....',
            '.....',
            '..P..',
            '.....',
            '.....']



##################################Sound###########################################
bullet_sound = pygame.mixer.Sound(os.path.join('assets/audio/se', 'Gun1.ogg'))
test_sound = pygame.mixer.Sound('assets/audio/se/Applause2.ogg')
test_sound.set_volume(0.1)
bullet_sound.set_volume(0.1)
##################################################################################

    

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 32)

        

        pygame.mouse.set_visible(False)

        pygame.mixer.music.load(os.path.join('assets/audio/bgm', 'Town1.ogg'))
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play(fade_ms=2000)

        self.character_spritesheet = SpriteSheet(pygame.image.load(os.path.join('assets/img/characters', 'doux.png')).convert_alpha())
        self.terrain_spritesheet = SpriteSheet(pygame.transform.scale(pygame.image.load(os.path.join('assets/img/tilesets', 'ground.png')).convert_alpha(), (12, 12)))

    def createTileMap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                if column == '.':
                    Block(self, j*32, i*32)
                if column == 'P':
                    Player(self, i*32, j*32)
    def new(self):
        #a new game starts
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.balles = pygame.sprite.LayeredUpdates()

        self.createTileMap()

        

    def events(self):
        #game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                bullet_sound.play()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    test_sound.play()

    def update(self):
        #game llop events
        self.all_sprites.update()

    def draw(self):
        #game loop draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        self.curseur()
        pygame.display.update()

    def main(self):
        #game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False

    def game_over(self):
        pass

    def curseur(self):
        mouse_pos = pygame.mouse.get_pos()
        CURSOR = pygame.transform.scale(pygame.image.load(os.path.join('assets/img/cursor', 'viewfinder.png')).convert_alpha(), (100, 100))
        CURSOR_RECT = CURSOR.get_rect()
        CURSOR_RECT.center = mouse_pos
        self.screen.blit(CURSOR, CURSOR_RECT)

    def intro_screen(self):
        intro = True

        title = self.font.render('Nom Jeu', True, BLACK)
        title_rect = title.get_rect(x=10, y=10)

        play_button = Button(10, 50, 100, 50, WHITE, BLACK, 'Play', 32)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False
                    exit()
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False
            self.screen.fill(BLUE)
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.clock.tick(FPS)
            self.curseur()
            pygame.display.update()


g = Game()
g.intro_screen()
g.new()
g.main()
g.game_over()

pygame.quit()
sys.exit()




    

#     MENU = 1
#     PARTY = 0
#     OPTIONS = 0
#     CREDITS = 0

#     while running:
#         clock.tick(FPS)

#         screen.fill(BACKGROUND)

#         ################################################################################################################
#         # VIEW
#         ################################################################################################################

#         if (MENU==1):
#             menu = viewMenu.viewMenu()
#             menu.draw(screen)
        
#         elif (OPTIONS==1):
#             option = viewOption.viewOption()
#             option.draw(screen)
        
#         elif (CREDITS==1):
#             credit = viewCredits.viewCredits()
#             credit.draw(screen)

#         elif (PARTY==1):
#             # party = viewParty.viewParty()
#             # party.draw(screen)
#             screen.blit(BACKGROUND2,(-1024,-1024))
#             player.update()
#             player.draw(screen)

#         ################################################################################################################
#         # EVENT LISTENER
#         ################################################################################################################

#         for event in pygame.event.get():
#             if PARTY:
#                 player.sprites().__getitem__(0).player_input(event)
#             if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONUP and event.button==1 and menu.exit_event.collidepoint(event.pos):
#                 running = False
#                 exit()
#             elif event.type == pygame.MOUSEBUTTONUP and event.button==1 and menu.play_event.collidepoint(event.pos):
#                 MENU=0
#                 CREDITS=0
#                 OPTIONS=0
#                 PARTY=1
#             elif event.type == pygame.MOUSEBUTTONUP and event.button==1 and menu.opt_event.collidepoint(event.pos) and MENU==1:
#                 MENU=0
#                 PARTY=0
#                 CREDITS=0
#                 OPTIONS=1
#             elif event.type == pygame.MOUSEBUTTONUP and event.button==1 :
#                 if menu.cred_event.collidepoint(event.pos) and MENU==1:
#                     MENU=0
#                     PARTY=0
#                     OPTIONS=0
#                     CREDITS=1
#             elif event.type == pygame.MOUSEBUTTONUP and event.button==1:
#                 if  option.back_event.collidepoint(event.pos):
#                     OPTIONS=0
#                     PARTY=0
#                     CREDITS=0
#                     MENU=1
#             elif event.type == pygame.MOUSEBUTTONUP and event.button==1:
#                 if credit.back_event_credit.collidepoint(event.pos):
#                     CREDITS=0
#                     OPTIONS=0
#                     PARTY=0
#                     MENU=1
