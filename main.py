#from cmath import rect
import random
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
   'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEGTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTREEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSS1cccccccccccccccccccccccc2SSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSSaggggggggggggggggggggggggbSSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSSaggggggggggggggggggggggggbSSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSSaggggggggggggggggggggggggbSSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSSaggggggggggggggggggggggggbSSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSSaggggggggggggggggggggggggbSSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSSagggggggggggPggggggggggggbSSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSSaggggggggggggggggggggggggbSSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSSaggggggggggggggggggggggggbSSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSSaggggggggggggggggggggggggbSSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSSaggggggggggggggggggggggggbSSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSSaggggggggggggggggggggggggbSSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSSaggggggggggggggggggggggggbSSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSS3xxxxxxxxxxxxxxxxxxxxxxxx4SSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEVBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBXEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
]

bullet_sound = pygame.mixer.Sound(os.path.join('assets/audio/se', 'Gun1.ogg'))
test_sound = pygame.mixer.Sound('assets/audio/se/Applause2.ogg')
spawn_sound = pygame.mixer.Sound(os.path.join('assets/audio/se/Up1.ogg'))
click_sound = pygame.mixer.Sound(os.path.join('assets/audio/se/Decision5.ogg'))

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
        self.music_played = True
        self.fx_played = True
        self.gameplay_ZQSD = False
        self.back_to_game = False
        self.tips = True
        self.timer_value = 0
        self.timer_init = 120 # 120s
        self.clock = pygame.time.Clock()

        pygame.mouse.set_visible(False)

        if self.fx_played==True:
            test_sound.set_volume(0.1)
            bullet_sound.set_volume(0.1)
            spawn_sound.set_volume(0.1)
            click_sound.set_volume(0.1)
        else:
            test_sound.set_volume(0)
            bullet_sound.set_volume(0)
            spawn_sound.set_volume(0)
            click_sound.set_volume(0)

        self.character_spritesheet = SpriteSheet(pygame.image.load(os.path.join('assets/img/characters', 'doux.png')).convert_alpha())
        self.terrain_spritesheet = SpriteSheet(pygame.image.load(os.path.join('assets/img/tests', 'spritesBG_3par8_64x64.png')).convert_alpha())
        self.crab_spritesheet = SpriteSheet(pygame.image.load(os.path.join('assets/img/tests/Crab.png')).convert_alpha())
        self.night_effet = [
            pygame.image.load(os.path.join('assets/img/tests', 'overlayN.png')).convert_alpha(),
            pygame.image.load(os.path.join('assets/img/tests', 'overlayNormalRed.png')).convert_alpha(),
            pygame.image.load(os.path.join('assets/img/tests', 'overlayBeforeDeath.png')).convert_alpha()
        ]


    def createTileMap(self):
        WIDTH, HEIGHT = 64, 64
        OFFSETX, OFFSETY = 23.5, 15
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):

                # basic textures
                if column == 'E':
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'water', True)
                if column == 'S':
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'sand', False)
                if column == 'g':
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'grass', False)

                #map border textures
                if column == 'T':
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'topWater', True)
                if column == 'G':
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'topLeftWaterBord', True)
                if column == 'R':
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'topRightWaterBord', True)
                if column == 'B':
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'bottomWaterBord', True)
                if column == 'V':
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'bottomLeftSand', True)
                if column == 'X':
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'bottomRightSand', True)
                if column == 'l':
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'rightWaterBord', True)
                if column == 'D':
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'leftWaterBord', True)

                #Sand + Grass Transition
                if column == '1':
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'topLeftSandGrassT', False)
                if column == '2':
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'topRightSandGrassT', False)
                if column == 'c':
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'topSandGrassT', False)
                if column == 'a':
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'leftSandGrassT', False)
                if column == 'b':
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'rightSandGrassT', False)
                if column == '4':
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'bottomRightSandGrassT', False)
                if column == '3':
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'bottomleftSandGrassT', False)
                if column == 'x':
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'bottomSandGrassT', False)


                #Player pog
                if column == 'P':
                    self.player = Player(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT,self.gameplay_ZQSD)
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'grass', False)
        self.screen.blit(pygame.image.load(os.path.join('assets/img/tests', 'spritesBG_3par8_64x64.png')).convert_alpha(), (0,0))
    def new(self):
        #a new game starts
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks_collid = pygame.sprite.LayeredUpdates()
        self.blocks_no_collid = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.bullets = pygame.sprite.LayeredUpdates()

        # self.night_effect = pygame.Surface((1024, 768))
        
        # self.night_effect.set_alpha(115)
        # self.night_effect.fill((30,0,0))

        self.createTileMap()

    def events(self):
        #game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    bullet_sound.play()
                    x, y = pygame.mouse.get_pos()
                    Bullet(self, self.player.rect.centerx, self.player.rect.centery, x, y, 5)
                if event.button == pygame.BUTTON_RIGHT:
                    spawn_sound.play()
                    Crab(self, self.player.x + (random.choice((-1,1))*random.randint(150,250)), self.player.y + (random.choice((-1,1))*random.randint(150,250)), 100,2)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    test_sound.play()
                elif event.key == pygame.K_ESCAPE:
                    self.playing = False
                    self.menu = True
                elif event.key == pygame.K_i:
                    self.tips = not self.tips
                    if self.tips:
                        self.tips1.set_alpha(150)
                        self.tips2.set_alpha(150)
                        self.tips3.set_alpha(150)
                    else:
                        self.tips1.set_alpha(0)
                        self.tips2.set_alpha(0)
                        self.tips3.set_alpha(0)
                elif event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                    self.playing = not self.playing
                    self.options = not self.options
                    self.back_to_game = True

    def update(self):
        #game llop events
        self.all_sprites.update()

    def draw(self):
        #game loop draw
        font = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 25)
        self.timer = font.render("Time left:  "+str(self.timer_value)+"s", True, BLACK)
        self.timer_rect = self.timer.get_rect(x=900, y=20)

        font = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 25)
        if self.tips:
            self.tips1 = font.render("Press 'esc' to quit party", True, BLACK)
            self.tips1.set_alpha(150)
            self.tips1_rect = self.tips1.get_rect(x=self.screen.get_width()/2-self.tips1.get_width()/2, y=100)

            self.tips2 = font.render("Press 'ctrl' to open options", True, BLACK)
            self.tips2.set_alpha(150)
            self.tips2_rect = self.tips2.get_rect(x=self.screen.get_width()/2-self.tips2.get_width()/2, y=130)

            self.tips3 = font.render("Press 'i' to toggle tips", True, BLACK)
            self.tips3.set_alpha(150)
            self.tips3_rect = self.tips3.get_rect(x=self.screen.get_width()/2-self.tips3.get_width()/2, y=160)

        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        self.screen.blit(self.tips1,self.tips1_rect)
        self.screen.blit(self.tips2,self.tips2_rect)
        self.screen.blit(self.tips3,self.tips3_rect)
        self.screen.blit(self.timer,self.timer_rect)
        
        self.screen.blit(self.night_effet[0], (0,0))
        self.curseur()
        
        pygame.display.update()

    def main(self):
        self.playing = True



        if self.music_played==True:
            pygame.mixer.music.load(os.path.join('assets/audio/bgm', 'Town3.ogg'))
            pygame.mixer.music.set_volume(0.05)
            pygame.mixer.music.play(fade_ms=2000)
        else:
            pygame.mixer.music.pause()

        while self.playing:
            self.draw()    
            self.events() 
            self.update()
            self.timer_value=int(self.timer_init-(pygame.time.get_ticks())/1000)
        pygame.display.update()

    def game_over(self):
        pass

    def curseur(self):
        mouse_pos = pygame.mouse.get_pos()
        CURSOR = pygame.transform.scale(pygame.image.load(os.path.join('assets/img/cursor', 'viewfinder.png')).convert_alpha(), (100, 100))
        CURSOR_RECT = CURSOR.get_rect()
        CURSOR_RECT.center = mouse_pos
        self.screen.blit(CURSOR, CURSOR_RECT)

    def intro_screen(self):
        click_sound.play()
        self.menu = True

        if self.music_played==True:
            pygame.mixer.music.load(os.path.join('assets/audio/bgm', 'Town1.ogg'))
            pygame.mixer.music.set_volume(0.05)
            pygame.mixer.music.play(fade_ms=2000)
        else:
            pygame.mixer.music.pause()

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
        click_sound.play()

        title = self.font.render('Options', True, BLACK)
        title_rect = title.get_rect(x=self.screen.get_width()/2-title.get_width()/2, y=100)

        font1 = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 50)
        font2 = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 30)

        sound_options = font1.render('Sound options', True, BLACK)
        sound_options_rect = sound_options.get_rect(x=self.screen.get_width()/3-title.get_width()/2, y=200)

        if self.music_played==True:
            music_on_off = Button(700, 240, 60, 30, WHITE, BLACK, 'On', 30)
        else:
            music_on_off = Button(700, 240, 60, 30, BLACK, WHITE, 'Off', 30)

        if self.fx_played==True:
            fx_on_off = Button(700, 270, 60, 30, WHITE, BLACK, 'On', 30)
        else:
            fx_on_off = Button(700, 270, 60, 30, BLACK, WHITE, 'Off', 30)

        music_sound = font2.render('Music theme sound', True, BLACK)
        music_sound_rect = music_sound.get_rect(x=self.screen.get_width()/3-title.get_width()/2, y=250)

        fx_sound = font2.render('FX sound', True, BLACK)
        fx_sound_rect = music_sound.get_rect(x=self.screen.get_width()/3-title.get_width()/2, y=280)

        gameplay = font1.render('Gameplay', True, BLACK)
        gameplay_rect = gameplay.get_rect(x=self.screen.get_width()/3-title.get_width()/2, y=320)

        top = font2.render('Top', True, BLACK)
        top_rect = top.get_rect(x=self.screen.get_width()/3-title.get_width()/2, y=370)

        bottom = font2.render('Bottom', True, BLACK)
        bottom_rect = bottom.get_rect(x=self.screen.get_width()/3-title.get_width()/2, y=400)

        left = font2.render('Left', True, BLACK)
        left_rect = left.get_rect(x=self.screen.get_width()/3-title.get_width()/2, y=430)

        right = font2.render('Right', True, BLACK)
        right_rect = right.get_rect(x=self.screen.get_width()/3-title.get_width()/2, y=460)

        if self.gameplay_ZQSD==True:
            top_btn1 = Button(700, 370, 60, 30, WHITE, BLACK, 'Z', 30)
            bottom_btn1 = Button(700, 400, 60, 30, WHITE, BLACK, 'S', 30)
            left_btn1 = Button(700, 430, 60, 30, WHITE, BLACK, 'Q', 30)
            right_btn1 = Button(700, 460, 60, 30, WHITE, BLACK, "D", 30)
            top_btn2 = Button(590, 370, 110, 30, BLACK, WHITE, 'Arr. Top', 30)
            bottom_btn2 = Button(590, 400, 110, 30, BLACK, WHITE, 'Arr. Bottom', 30)
            left_btn2 = Button(590, 430, 110, 30, BLACK, WHITE, 'Arr. Left', 30)
            right_btn2 = Button(590, 460, 110, 30, BLACK, WHITE, "Arr. Right", 30)
        else:
            top_btn1 = Button(700, 370, 60, 30, BLACK, WHITE, 'Z', 30)
            bottom_btn1 = Button(700, 400, 60, 30, BLACK, WHITE, 'S', 30)
            left_btn1 = Button(700, 430, 60, 30, BLACK, WHITE, 'Q', 30)
            right_btn1 = Button(700, 460, 60, 30, BLACK, WHITE, "D", 30)
            top_btn2 = Button(590, 370, 110, 30, WHITE, BLACK, 'Arr. Top', 30)
            bottom_btn2 = Button(590, 400, 110, 30, WHITE, BLACK, 'Arr. Bottom', 30)
            left_btn2 = Button(590, 430, 110, 30, WHITE, BLACK, 'Arr. Left', 30)
            right_btn2 = Button(590, 460, 110, 30, WHITE, BLACK, "Arr. Right", 30)

        if self.back_to_game:
            back_button = Button((self.screen.get_width()/2)-100, 650, 200, 50, WHITE, BLACK, 'Back to game', 30)
        else:
            back_button = Button((self.screen.get_width()/2)-100, 650, 200, 50, WHITE, BLACK, 'Back to menu', 30)

        while self.options:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.options = False
                    self.running = False
                    exit()
                if event.type == pygame.MOUSEBUTTONUP and music_on_off.rect.collidepoint(pygame.mouse.get_pos()):
                    click_sound.play()
                    self.music_played= not self.music_played
                    if self.music_played:
                        pygame.mixer.music.unpause()
                    else:
                        pygame.mixer.music.pause()
                    self.options_screen()
                elif event.type == pygame.MOUSEBUTTONUP and fx_on_off.rect.collidepoint(pygame.mouse.get_pos()):
                    click_sound.play()
                    self.fx_played= not self.fx_played
                    if self.fx_played:
                        test_sound.set_volume(0.1)
                        bullet_sound.set_volume(0.1)
                        spawn_sound.set_volume(0.1)
                        click_sound.set_volume(0.1)
                    else:
                        test_sound.set_volume(0)
                        bullet_sound.set_volume(0)
                        spawn_sound.set_volume(0)
                        click_sound.set_volume(0)
                    self.options_screen()
                elif event.type == pygame.MOUSEBUTTONUP and (top_btn1.rect.collidepoint(pygame.mouse.get_pos())or
                                                             bottom_btn1.rect.collidepoint(pygame.mouse.get_pos())or
                                                             left_btn1.rect.collidepoint(pygame.mouse.get_pos())or
                                                             right_btn1.rect.collidepoint(pygame.mouse.get_pos())):
                    self.gameplay_ZQSD = True
                    self.options_screen()
                elif event.type == pygame.MOUSEBUTTONUP and (top_btn2.rect.collidepoint(pygame.mouse.get_pos())or
                                                             bottom_btn2.rect.collidepoint(pygame.mouse.get_pos())or
                                                             left_btn2.rect.collidepoint(pygame.mouse.get_pos())or
                                                             right_btn2.rect.collidepoint(pygame.mouse.get_pos())):
                    self.gameplay_ZQSD = False
                    self.options_screen()
                elif event.type == pygame.MOUSEBUTTONUP and back_button.rect.collidepoint(pygame.mouse.get_pos()) or (event.type == pygame.KEYDOWN and (event.key==K_RCTRL or event.key==K_LCTRL)):
                    if self.back_to_game:
                        self.options = False
                        self.playing = True
                    else:
                        self.options = False
                        self.menu = True

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            self.screen.fill(BLUE)
            self.screen.blit(title, title_rect)
            self.screen.blit(sound_options, sound_options_rect)
            self.screen.blit(music_sound, music_sound_rect)
            self.screen.blit(fx_sound, fx_sound_rect)
            self.screen.blit(gameplay, gameplay_rect)
            self.screen.blit(top, top_rect)
            self.screen.blit(bottom, bottom_rect)
            self.screen.blit(left, left_rect)
            self.screen.blit(right, right_rect)
            self.screen.blit(music_on_off.image, music_on_off.rect)
            self.screen.blit(fx_on_off.image, fx_on_off.rect)
            self.screen.blit(back_button.image, back_button.rect)
            self.screen.blit(top_btn1.image, top_btn1.rect)
            self.screen.blit(bottom_btn1.image, bottom_btn1.rect)
            self.screen.blit(left_btn1.image, left_btn1.rect)
            self.screen.blit(right_btn1.image, right_btn1.rect)
            self.screen.blit(top_btn2.image, top_btn2.rect)
            self.screen.blit(bottom_btn2.image, bottom_btn2.rect)
            self.screen.blit(left_btn2.image, left_btn2.rect)
            self.screen.blit(right_btn2.image, right_btn2.rect)
            self.clock.tick(FPS)
            self.curseur()
            pygame.display.update()


    def credits_screen(self):
        click_sound.play()
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
