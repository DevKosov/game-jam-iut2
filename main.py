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
RED = (255, 0, 0)
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
   'EEEEEEEEEEEEEEEEDSSaggggggggggggggggg]ppppp[bSSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSSagggggggggggggggggy/////ybSSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSSagggggggggggggggggg/////gbSSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSSagggggggggggggggggg/////gbSSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSSagggggggggggggggggt/////tbSSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSSagggggggggggPgggggipppppubSSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSSa]pp[ggggggggggggggggggggbSSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSSao//yggggggggggggggggggggbSSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSSao//gggggggggggggggggggggbSSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSSao//gggggggggggggggggggggbSSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSSao//tggggggggggggggggggggbSSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSSaippuggggggggggggggggggggbSSlEEEEEEEEEEEEEEEE',
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
        self.back_to_game = "null"
        self.tips = True
        self.timer_value = 0
        self.timer_init = 120 # 120s
        self.clock = pygame.time.Clock()

        self.xTopLefIsland = 0
        self.yTopLefIsland = 0
        self.nb_crabs_killed = 0 # pour romain

        self.bullet_sound = pygame.mixer.Sound(os.path.join('assets/audio/se', 'Gun1.ogg'))
        self.switch_weapon_sound = pygame.mixer.Sound(os.path.join('assets/audio/se', 'Switch2.ogg'))
        self.damaged_sound = pygame.mixer.Sound(os.path.join('assets/audio/se/Damage1.ogg'))

        pygame.mouse.set_visible(False)

        if self.fx_played==True:
            self.bullet_sound.set_volume(0.1)
            self.switch_weapon_sound.set_volume(0.08)
            spawn_sound.set_volume(0.1)
            click_sound.set_volume(0.1)
            self.damaged_sound.set_volume(0.05)

        else:
            self.bullet_sound.set_volume(0)
            self.switch_weapon_sound.set_volume(0)
            spawn_sound.set_volume(0)
            click_sound.set_volume(0)
            self.damaged_sound.set_volume(0)

        self.character_spritesheet = SpriteSheet(pygame.image.load(os.path.join('assets/img/characters', 'doux2.png')).convert_alpha())
        self.terrain_spritesheet = SpriteSheet(pygame.image.load(os.path.join('assets/img/tests', 'spritesBG_3par8_64x64.png')).convert_alpha())
        self.crab_spritesheet = SpriteSheet(pygame.image.load(os.path.join('assets/img/tests/Crab.png')).convert_alpha())
        self.night_effet = [
            pygame.image.load(os.path.join('assets/img/tests', 'overlayN.png')).convert_alpha(),
            pygame.image.load(os.path.join('assets/img/tests', 'overlayNormalRed.png')).convert_alpha(),
            pygame.image.load(os.path.join('assets/img/tests', 'overlayBeforeDeath.png')).convert_alpha()
        ] # lul


    def createTileMap(self):
        WIDTH, HEIGHT = 64, 64
        OFFSETX, OFFSETY = 23.5, 15
        self.xTopLefIsland = (0-OFFSETX)*WIDTH
        self.yTopLefIsland = (0-OFFSETY)*HEIGHT
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                # basic textures
                if column == 'E':
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'water', True)
                if column == 'S':
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'sand', False)
                if column == 'g':
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'grass', False)
                if column == '/':
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'dirt', False)
                if column == '.':
                    Block(self, (j-OFFSETX)*WIDTH, (i-OFFSETY)*HEIGHT, 'growingPotato', False)

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

                # Fences
                if column == ']':
                    Block(self, (j - OFFSETX) * WIDTH, (i - OFFSETY) * HEIGHT, 'topLeftFence', True)
                if column == '[':
                    Block(self, (j - OFFSETX) * WIDTH, (i - OFFSETY) * HEIGHT, 'topRightFence', True)
                if column == 'p':
                    Block(self, (j - OFFSETX) * WIDTH, (i - OFFSETY) * HEIGHT, 'topFence', True)
                if column == 'o':
                    Block(self, (j - OFFSETX) * WIDTH, (i - OFFSETY) * HEIGHT, 'sideFence', True)
                if column == 'i':
                    Block(self, (j - OFFSETX) * WIDTH, (i - OFFSETY) * HEIGHT, 'bottomLeftFence', True)
                if column == 'u':
                    Block(self, (j - OFFSETX) * WIDTH, (i - OFFSETY) * HEIGHT, 'bottomRightFence', True)
                if column == 'y':
                    Block(self, (j - OFFSETX) * WIDTH, (i - OFFSETY) * HEIGHT, 'topStopFence', True)
                if column == 't':
                    Block(self, (j - OFFSETX) * WIDTH, (i - OFFSETY) * HEIGHT, 'bottomStopFence', True)

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
        self.day_time = True
        self.farm_time = False
        self.night_time = False
        self.createTileMap()

    def events(self):
        #game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.player.switch_weapon(event)
                if event.button == pygame.BUTTON_LEFT:
                    self.player.attacks()
                if event.button == pygame.BUTTON_RIGHT:
                    spawn_sound.play()
                    Crab(self, self.player.x + (random.choice((-1,1))*random.randint(150,250)), self.player.y + (random.choice((-1,1))*random.randint(150,250)), 100,2)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                    self.menu = True
                elif event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                    self.playing = not self.playing
                    self.options = not self.options
                    self.back_to_game = "night"

    def events_day(self):
        #game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.day_time = False
                    self.farm_time = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
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
                    self.back_to_game = "day"

    def update_night(self):
        #game llop events
        self.all_sprites.update()
        #crabSpawn
        if (random.randint(0,60*3)) == 0:
            self.crab_spawn(100)

    def crab_spawn(self,hp):
        spawn_sound.play()
        # Crab(self, self.player.x + (random.choice((-1, 1)) * random.randint(150, 250)),self.player.y + (random.choice((-1, 1)) * random.randint(150, 250)), 100, 2)
        Crab(self,self.xTopLefIsland,self.yTopLefIsland,100,random.randint(1,5))
    def draw_night(self):
        #game loop draw
        font = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 25)
        self.timer = font.render("Time left:  "+str(self.timer_value)+"s", True, BLACK)
        self.timer_rect = self.timer.get_rect(x=900, y=20)

        self.crabs_killed = font.render("Crabs killed: "+str(self.nb_crabs_killed), True, BLACK)
        self.crabs_killed_rect = self.crabs_killed.get_rect(x=900, y=40)

        current_defense_label = font.render("Current defense", True, BLACK)
        current_defense_label_rect = current_defense_label.get_rect(x=860, y=650)

        if self.player.current_weapon=="gun":
            current_defense = font.render("Gun", True, BLACK)
        else:
            current_defense = font.render("Knife", True, BLACK)
        current_defense_rect = current_defense.get_rect(x=910, y=680)

        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        self.screen.blit(self.timer,self.timer_rect)
        self.screen.blit(self.crabs_killed,self.crabs_killed_rect)
        self.screen.blit(current_defense_label,current_defense_label_rect)
        self.screen.blit(current_defense,current_defense_rect)
        self.screen.blit(self.night_effet[0], (0,0))
        self.curseur()

        pygame.display.update()

    def draw_day(self):

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

        #game loop draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        self.curseur()

        pygame.display.update()

    def update_day(self):
        #game llop events
        self.all_sprites.update()
    
    def draw_farm(self):

        title = self.font.render("It's farmer time", True, WHITE)
        title_rect = title.get_rect(x=self.screen.get_width()/2-title.get_width()/2, y=100)

        font = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 25)
        subtitle = font.render("Improve your weapon damage", True, WHITE)
        subtitle_rect = subtitle.get_rect(x=self.screen.get_width()/2-subtitle.get_width()/2, y=150)

        font = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 40)
        label_nb_ress1 = font.render("Number of Potat : 10", True, WHITE) # à changer une fois les ressources crées
        label_nb_ress1_rect = subtitle.get_rect(x=self.screen.get_width()/3-label_nb_ress1.get_width()/2, y=230)
        label_nb_ress2 = font.render("Number of Corn : 7", True, WHITE) # à changer une fois les ressources crées
        label_nb_ress2_rect = subtitle.get_rect(x=350+self.screen.get_width()/3-label_nb_ress2.get_width()/2, y=230)

        res_btn1 = Button(80, 500, 120, 50, BLACK, BLUE, '10 Potat', 30)
        res_btn2 = Button(300, 500, 120, 50, BLACK, BLUE, '10 Corn', 30)
        res_btn3 = Button(520, 500, 120, 50, BLACK, BLUE, '10 Potat', 30)
        res_btn4 = Button(740, 500, 120, 50, BLACK, BLUE, '10 Corn', 30)

        buy_btn1 = Button(200, 500, 80, 50, BLACK, WHITE, 'Buy', 30)
        buy_btn2 = Button(420, 500, 80, 50, BLACK, WHITE, 'Buy', 30)
        buy_btn3 = Button(640, 500, 80, 50, BLACK, WHITE, 'Buy', 30)
        buy_btn4 = Button(860, 500, 80, 50, BLACK, WHITE, 'Buy', 30)


        self.screen.fill(BLACK)
        self.clock.tick(FPS)
        self.screen.blit(title,title_rect)
        self.screen.blit(subtitle,subtitle_rect)
        self.screen.blit(label_nb_ress1,label_nb_ress1_rect)
        self.screen.blit(label_nb_ress2,label_nb_ress2_rect)
        pygame.draw.rect(self.screen, RED, pygame.Rect(80, 300, 200, 200))
        self.screen.blit(res_btn1.image,res_btn1.rect)
        self.screen.blit(buy_btn1.image,buy_btn1.rect)
        pygame.draw.rect(self.screen, RED, pygame.Rect(300, 300, 200, 200))
        self.screen.blit(res_btn2.image,res_btn2.rect)
        self.screen.blit(buy_btn2.image,buy_btn2.rect)
        pygame.draw.rect(self.screen, RED, pygame.Rect(520, 300, 200, 200))
        self.screen.blit(res_btn3.image,res_btn3.rect)
        self.screen.blit(buy_btn3.image,buy_btn3.rect)
        pygame.draw.rect(self.screen, RED, pygame.Rect(740, 300, 200, 200))
        self.screen.blit(res_btn4.image,res_btn4.rect)
        self.screen.blit(buy_btn4.image,buy_btn4.rect)
        self.curseur()

        pygame.display.update()

    def events_farm(self):
        #game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.farm_time = False
                    self.night_time = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                    self.menu = True
                elif event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                    self.playing = not self.playing
                    self.options = not self.options
                    self.back_to_game = "farm"
                    if (self.playing):
                        self.main()

    def main(self):
        self.playing = True

        while self.playing:
            if self.back_to_game=="day" or self.day_time:
                self.draw_day()
                self.events_day()
            elif self.back_to_game=="farm" or self.farm_time:
                self.draw_farm()
                self.events_farm()
            elif self.back_to_game=="night" or self.night_time:
                self.draw_night()
                self.events()
                self.update_night()
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
                        self.bullet_sound.set_volume(0.1)
                        self.switch_weapon_sound.set_volume(0.08)
                        spawn_sound.set_volume(0.1)
                        click_sound.set_volume(0.1)
                        self.damaged_sound.set_volume(0.05)
                    else:
                        self.bullet_sound.set_volume(0)
                        self.switch_weapon_sound.set_volume(0)
                        spawn_sound.set_volume(0)
                        click_sound.set_volume(0)
                        self.damaged_sound.set_volume(0)

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
                    if self.back_to_game!="null":
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
        if g.music_played==True:
            pygame.mixer.music.load(os.path.join('assets/audio/bgm', 'Town1.ogg'))
            pygame.mixer.music.set_volume(0.05)
            pygame.mixer.music.play(fade_ms=2000)
        else:
            pygame.mixer.music.pause()
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
