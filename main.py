#from cmath import rect
import this
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
tilemap = [
'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEGTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTREEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEDSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSlEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEDSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSlEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEDSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSlEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEDSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSlEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEDSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSlEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEDSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSlEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEDSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSPSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSlEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEDSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSlEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEDSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSlEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEDSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSlEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEDSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSlEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEDSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSlEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEVBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBXEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE']



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
        self.menu = True
        self.playing = False
        self.options = False
        self.credits = False
        self.font = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 70)

        pygame.mouse.set_visible(False)

        pygame.mixer.music.load(os.path.join('assets/audio/bgm', 'Town1.ogg'))
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play(fade_ms=2000)

        self.character_spritesheet = SpriteSheet(pygame.image.load(os.path.join('assets/img/characters', 'doux.png')).convert_alpha())
        self.terrain_spritesheet = SpriteSheet(pygame.image.load(os.path.join('assets/img/tests', 'spritesBG_3par8_64x64.png')).convert_alpha())

    def createTileMap(self):
        WIDTH, HEIGHT = 64, 64
        OFFSETX, OFFSETY = 39, 13
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                if column == 'E':
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'water')
                if column == 'S':
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'sand')
                if column == 'T':
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'topWater')
                if column == 'G':
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'topLeftWaterBord')
                if column == 'R':
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'topRightWaterBord')
                if column == 'B':
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'bottomWaterBord')
                if column == 'V':
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'bottomLeftSand')
                if column == 'X':
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'bottomRightSand')
                if column == 'l':
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'rightWaterBord')
                if column == 'D':
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'leftWaterBord')
                if column == 'P':
                    Player(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT)
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'sand')
        self.screen.blit(pygame.image.load(os.path.join('assets/img/tests', 'spritesBG_3par8_64x64.png')).convert_alpha(), (0,0))
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
        self.menu = True

        title = self.font.render('Pog Champs Game', True, BLACK)
        title_rect = title.get_rect(x=self.screen.get_width()/2-title.get_width()/2, y=100)

        play_button = Button((self.screen.get_width()/2)-100, 250, 200, 50, WHITE, BLACK, 'Play', 40)
        option_button = Button((self.screen.get_width()/2)-100, 350, 200, 50, WHITE, BLACK, 'Options', 40)
        credits_button = Button((self.screen.get_width()/2)-100, 450, 200, 50, WHITE, BLACK, 'Credits', 40)
        exit_button = Button((self.screen.get_width()/2)-100, 550, 200, 50, WHITE, BLACK, 'Exit', 40)

        while self.menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu = False
                    self.running = False
                    exit()
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                self.menu = False
                self.playing = True
            elif option_button.is_pressed(mouse_pos,mouse_pressed):
                self.menu = False
                self.options = True
            elif credits_button.is_pressed(mouse_pos,mouse_pressed):
                self.menu = False
                self.credits = True
            elif exit_button.is_pressed(mouse_pos,mouse_pressed):
                exit()
            self.screen.fill(BLUE)
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.screen.blit(option_button.image, option_button.rect)
            self.screen.blit(credits_button.image, credits_button.rect)
            self.screen.blit(exit_button.image, exit_button.rect)
            self.clock.tick(FPS)
            self.curseur()
            pygame.display.update()

    def options_screen(self):
        self.options = True

        title = self.font.render('Options', True, BLACK)
        title_rect = title.get_rect(x=self.screen.get_width()/2-title.get_width()/2, y=100)
        back_button = Button((self.screen.get_width()/2)-100, 650, 200, 50, WHITE, BLACK, 'Back to menu', 30)

        while self.options:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.options = False
                    self.running = False
                    exit()
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            if back_button.is_pressed(mouse_pos,mouse_pressed):
                self.options = False
                self.menu = True

            self.screen.fill(BLUE)
            self.screen.blit(title, title_rect)
            self.screen.blit(back_button.image, back_button.rect)

            self.clock.tick(FPS)
            self.curseur()
            pygame.display.update()
    
    def credits_screen(self):
        self.credits = True

        title = self.font.render('Credits', True, BLACK)
        title_rect = title.get_rect(x=self.screen.get_width()/2-title.get_width()/2, y=100)

        back_button = Button((self.screen.get_width()/2)-100, 650, 200, 50, WHITE, BLACK, 'Back to menu', 30)

        while self.credits:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.credits = False
                    self.running = False
                    exit()
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            if back_button.is_pressed(mouse_pos,mouse_pressed):
                self.credits = False
                self.menu = True

            self.screen.fill(BLUE)
            self.screen.blit(title, title_rect)
            self.screen.blit(back_button.image, back_button.rect)

            self.clock.tick(FPS)
            self.curseur()
            pygame.display.update()


g = Game()
while g.running==True:

    if g.menu==True:
        g.intro_screen()
    elif g.options==True:
        g.options_screen()
    elif g.credits==True:
        g.credits_screen()
    elif g.playing==True:
        g.new()
        g.main()
        g.game_over()

pygame.quit()
sys.exit()