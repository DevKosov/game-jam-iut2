# from cmath import rect
import random
import this
import pygame, os
from sprite import *
from config import *
import sys

from sys import exit
from pygame.locals import *

pygame.init()
pygame.display.set_caption('GAME JAM 2022')


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
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.menu = True
        self.playing = False
        self.options = False
        self.credits = False
        self.font = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 70)
        self.music_played = True
        self.fx_played = True
        self.gameplay_ZQSD = True
        self.back_to_game = False
        self.tips = True
        self.timer_value = 0
        self.timer_init = 120  # 120s
        self.clock = pygame.time.Clock()
        self.nb_crabs_killed = 0

        self.xTopLefIsland = 0
        self.yTopLefIsland = 0
        self.hpCrab = HP_CRAB

        self.bullet_sound = pygame.mixer.Sound(os.path.join('assets/audio/se', 'Gun1.ogg'))
        self.switch_weapon_sound = pygame.mixer.Sound(os.path.join('assets/audio/se', 'Switch2.ogg'))
        self.damaged_sound = pygame.mixer.Sound(os.path.join('assets/audio/se/Damage1.ogg'))

        pygame.mouse.set_visible(False)

        if self.fx_played == True:
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

        self.character_spritesheet = SpriteSheet(
            pygame.image.load(os.path.join('assets/img/characters', 'doux2.png')).convert_alpha())
        self.terrain_spritesheet = SpriteSheet(
            pygame.image.load(os.path.join('assets/img/tests', 'spritesBG_3par8_64x64.png')).convert_alpha())
        self.crab_spritesheet = SpriteSheet(
            pygame.image.load(os.path.join('assets/img/tests/Crab.png')).convert_alpha())
        self.night_effet = [
            pygame.image.load(os.path.join('assets/img/tests', 'overlayN.png')).convert_alpha(),
            pygame.image.load(os.path.join('assets/img/tests', 'overlayNormalRed.png')).convert_alpha(),
            pygame.image.load(os.path.join('assets/img/tests', 'overlayBeforeDeath.png')).convert_alpha()
        ]  # lul

    def createTileMap(self):
        
        self.xTopLefIsland = (17 - OFFSETX) * TILE_WIDTH
        self.yTopLefIsland = (12 - OFFSETY) * TILE_HEIGHT
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                # basic textures
                if column == 'E':
                    Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'water', True, False)
                if column == 'S':
                    Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'sand', False, False)
                if column == 'g':
                    Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'grass', False, False)
                if column == '/':
                    Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'dirt', False, False)

                # map border textures
                if column == 'T':
                    Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'topWater', True, False)
                if column == 'G':
                    Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'topLeftWaterBord', True, False)
                if column == 'R':
                    Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'topRightWaterBord', True, False)
                if column == 'B':
                    Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'bottomWaterBord', True, False)
                if column == 'V':
                    Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'bottomLeftSand', True, False)
                if column == 'X':
                    Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'bottomRightSand', True, False)
                if column == 'l':
                    Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'rightWaterBord', True, False)
                if column == 'D':
                    Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'leftWaterBord', True, False)

                # Sand + Grass Transition
                if column == '1':
                    Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'topLeftSandGrassT', False, False)
                if column == '2':
                    Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'topRightSandGrassT', False, False)
                if column == 'c':
                    Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'topSandGrassT', False, False)
                if column == 'a':
                    Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'leftSandGrassT', False, False)
                if column == 'b':
                    Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'rightSandGrassT', False, False)
                if column == '4':
                    Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'bottomRightSandGrassT', False, False)
                if column == '3':
                    Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'bottomleftSandGrassT', False, False)
                if column == 'x':
                    Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'bottomSandGrassT', False, False)

                # Fences
                if column == ']':
                    Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'topLeftFence', True, False)
                if column == '[':
                    Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'topRightFence', True, False)
                if column == 'p':
                    Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'topFence', True, False)
                if column == 'o':
                    Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'sideFence', True, False)
                if column == 'i':
                    Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'bottomLeftFence', True, False)
                if column == 'u':
                    Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'bottomRightFence', True, False)
                if column == 'y':
                    Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'topStopFence', True, False)
                if column == 't':
                    Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'bottomStopFence', True, False)

                #potato
                if column == ':':
                    Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'dirt', False, False)
                    Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'firstStagePotato', True, True)
                # Player pog
                if column == 'P':
                    self.player = Player(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, self.gameplay_ZQSD)
                    Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'grass', False, False)

        self.screen.blit(
            pygame.image.load(os.path.join('assets/img/tests', 'spritesBG_3par8_64x64.png')).convert_alpha(), (0, 0))

    def new(self):
        # a new game starts
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks_no_collid_not_farm = pygame.sprite.LayeredUpdates()
        self.blocks_no_collid_farm = pygame.sprite.LayeredUpdates()
        self.blocks_collid = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.bullets = pygame.sprite.LayeredUpdates()

        # self.night_effect = pygame.Surface((1024, 768))

        # self.night_effect.set_alpha(115)
        # self.night_effect.fill((30,0,0))
        self.day_time = True
        self.farm_time = False
        self.night_time = False
        self.createTileMap()

    def events_night(self):
        # game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                exit()
            if event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    self.player.sprint(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.player.switch_weapon(event)
                if event.button == pygame.BUTTON_LEFT:
                    self.player.attacks()
                if event.button == pygame.BUTTON_RIGHT:
                    self.crab_spawn(self.hpCrab)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_r:
                    self.player.reloading()
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
                    self.back_to_game = True

    def events_day(self):
        # game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.day_time = False
                    self.farm_time = True
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    for block in self.blocks_no_collid_farm:
                        if pygame.sprite.collide_mask(self.player, block):
                            block.kill()
                            self.player.potat_counter += 1
            if event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    self.player.sprint(event)
    def update_night(self):
        # game llop events
        self.all_sprites.update()
        # crabSpawn
        if (random.randint(0, TIME_SPAWN_CRAB)) == 0:
            self.crab_spawn(self.hpCrab)

    def crab_spawn(self, hp):
        spawn_sound.play()
        # Crab(self, self.player.x + (random.choice((-1, 1)) * random.randint(150, 250)),self.player.y + (random.choice((-1, 1)) * random.randint(150, 250)), 100, 2)
        position = random.randint(1,5)
        if position == 1: # Corner Top Left
            Crab(self, self.xTopLefIsland, self.yTopLefIsland, self.hpCrab, random.randint(CRAB_VITESSE_MIN, CRAB_VITESSE_MAX))
        elif position == 2: # Corner Top Right
            Crab(self, self.xTopLefIsland + ISLANDWIDTH, self.yTopLefIsland, self.hpCrab, random.randint(CRAB_VITESSE_MIN, CRAB_VITESSE_MAX))
        elif position == 3: # Corner Bottom Left
            Crab(self, self.xTopLefIsland, self.yTopLefIsland + ISLANDHEIGHT, self.hpCrab, random.randint(CRAB_VITESSE_MIN, CRAB_VITESSE_MAX))
        elif position == 4: # Corner Bottom Right
            Crab(self, self.xTopLefIsland + ISLANDWIDTH, self.yTopLefIsland + ISLANDHEIGHT, self.hpCrab, random.randint(CRAB_VITESSE_MIN, CRAB_VITESSE_MAX))
        elif position == 5: # Tous en même temps
            Crab(self, self.xTopLefIsland, self.yTopLefIsland, self.hpCrab, random.randint(CRAB_VITESSE_MIN, CRAB_VITESSE_MAX))
            Crab(self, self.xTopLefIsland + ISLANDWIDTH, self.yTopLefIsland, self.hpCrab, random.randint(CRAB_VITESSE_MIN, CRAB_VITESSE_MAX))
            Crab(self, self.xTopLefIsland, self.yTopLefIsland + ISLANDHEIGHT, self.hpCrab, random.randint(CRAB_VITESSE_MIN, CRAB_VITESSE_MAX))
            Crab(self, self.xTopLefIsland + ISLANDWIDTH, self.yTopLefIsland + ISLANDHEIGHT, self.hpCrab, random.randint(CRAB_VITESSE_MIN, CRAB_VITESSE_MAX))

    def draw(self):
        #game loop draw
        font = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 25)
        self.timer = font.render("Time left:  "+str(self.timer_value)+"s", True, BLACK)
        self.timer_rect = self.timer.get_rect(x=900, y=20)

        self.crabs_killed = font.render("Crabs killed: "+str(self.nb_crabs_killed), True, BLACK)
        self.crabs_killed_rect = self.crabs_killed.get_rect(x=900, y=40)

        current_defense_label = font.render("Current defense", True, BLACK)
        current_defense_label_rect = current_defense_label.get_rect(x=860, y=650)

        if self.player.current_weapon=="gun":
            font = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 90)
            current_ammo = font.render(str(self.player.gun_ammo), True, BLACK)
            current_ammo_label_rect = current_ammo.get_rect(x=30, y=30)
            font = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 30)
            max_ammo = font.render("/"+str(self.player.gun_max_ammo), True, BLACK)
            max_ammo_label_rect = current_ammo.get_rect(x=80, y=55)
        else:
            knife_img1 = pygame.image.load("assets/img/tests/knife.png")
            knife_img2 = pygame.transform.rotate(knife_img1,45)

        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        self.screen.blit(self.timer,self.timer_rect)
        self.screen.blit(self.crabs_killed,self.crabs_killed_rect)
        self.screen.blit(current_defense_label,current_defense_label_rect)
        if self.player.current_weapon=="gun":
            self.screen.blit(current_ammo,current_ammo_label_rect)
            self.screen.blit(max_ammo,max_ammo_label_rect)
        else:
            self.screen.blit(knife_img2, (900,680))
        if (self.player.player_health == 3):
            self.screen.blit(self.night_effet[0], (0,0))
        elif (self.player.player_health == 2):
            self.screen.blit(self.night_effet[1], (0,0))
        else:
            self.screen.blit(self.night_effet[2], (0,0))

        self.curseur()
        pygame.display.update()

    def draw_day(self):

        # game loop draw
        font = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 35)
        self.timer = font.render("Time left:  " + str(self.timer_value) + "s", True, BLACK)
        self.timer_rect = self.timer.get_rect(x=20, y=20)

        font = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 35)
        label_nb_ress1 = font.render(str(self.player.potat_counter), True, BLACK)
        label_nb_ress1_rect = label_nb_ress1.get_rect(x=940, y=30)

        label_nb_ress2 = font.render(str(self.player.corn_counter), True, BLACK) 
        label_nb_ress2_rect = label_nb_ress1.get_rect(x=940,y=90)

        potato_img1 = pygame.image.load("assets/img/tests/potato.png")
        potato_img2 = pygame.transform.scale(potato_img1, (40,40))

        corn_img1 = pygame.image.load("assets/img/tests/corna.png")
        corn_img2 = pygame.transform.scale(corn_img1, (40,40))

        font = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 25)
        if self.tips:
            self.tips1 = font.render("Press 'esc' to quit party", True, BLACK)
            self.tips1.set_alpha(150)
            self.tips1_rect = self.tips1.get_rect(x=self.screen.get_width() / 2 - self.tips1.get_width() / 2, y=100)

            self.tips2 = font.render("Press 'ctrl' to open options", True, BLACK)
            self.tips2.set_alpha(150)
            self.tips2_rect = self.tips2.get_rect(x=self.screen.get_width() / 2 - self.tips2.get_width() / 2, y=130)

            self.tips3 = font.render("Press 'i' to toggle tips", True, BLACK)
            self.tips3.set_alpha(150)
            self.tips3_rect = self.tips3.get_rect(x=self.screen.get_width() / 2 - self.tips3.get_width() / 2, y=160)

        self.collectMessage = font.render("Clique gauche pour manger une patate", True, BLACK)
        self.collectMessage_rect = self.collectMessage.get_rect(x=WINDOW_WIDTH / 2 - self.collectMessage.get_width() / 2, y=WINDOW_HEIGHT / 2 - self.collectMessage.get_height() / 2)
        
        # game loop draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.screen.blit(self.tips1, self.tips1_rect)
        self.screen.blit(self.tips2, self.tips2_rect)
        self.screen.blit(self.tips3, self.tips3_rect)
        self.screen.blit(self.timer, self.timer_rect)
        self.screen.blit(potato_img2, (970,20))
        self.screen.blit(corn_img2, (970,80))
        self.screen.blit(label_nb_ress1,label_nb_ress1_rect)
        self.screen.blit(label_nb_ress2,label_nb_ress2_rect)
        self.clock.tick(FPS)
        if pygame.sprite.spritecollide(self.player, self.blocks_no_collid_farm, False):
            self.screen.blit(self.collectMessage, self.collectMessage_rect)
        self.curseur()

        pygame.display.update()

    def update_day(self):
        # game llop events
        if random.randint(1,600) == 69:
            if random.randint(1,2) == 2:
                patateX = random.randint(38,42)
                patateY = random.randint(16,19)
                Block(self, self.xTopLefIsland + (patateX - 17) * TILE_WIDTH, self.yTopLefIsland + (patateY - 12) * TILE_HEIGHT, 'firstStagePotato', True, True)
            else:
                patateX = random.randint(21,22)
                patateY = random.randint(22,25)
                Block(self, self.xTopLefIsland + (patateX - 17) * TILE_WIDTH, self.yTopLefIsland + (patateY - 12) * TILE_HEIGHT, 'firstStagePotato', True, True)


        self.all_sprites.update()

    def draw_farm(self):

        title = self.font.render("It's farmer time", True, WHITE)
        title_rect = title.get_rect(x=self.screen.get_width() / 2 - title.get_width() / 2, y=100)

        font = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 25)
        subtitle = font.render("Improve your skills and damages", True, WHITE)
        subtitle_rect = subtitle.get_rect(x=self.screen.get_width() / 2 - subtitle.get_width() / 2, y=150)

        potato_img1 = pygame.image.load("assets/img/tests/potato.png")
        potato_img2 = pygame.transform.scale(potato_img1, (40,40))

        corn_img1 = pygame.image.load("assets/img/tests/corna.png")
        corn_img2 = pygame.transform.scale(corn_img1, (40,40))
 
        font = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 40)
        label_nb_ress1 = font.render(str(self.player.potat_counter), True, WHITE)
        label_nb_ress1_rect = subtitle.get_rect(x=450, y=230)
        label_nb_ress2 = font.render(str(self.player.corn_counter), True, WHITE) 
        label_nb_ress2_rect = subtitle.get_rect(x=630,y=230)

        font = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 40)
        label_gun_dam = font.render("Gun damage", True, BLACK)
        label_gun_dam_rect = label_gun_dam.get_rect(x=110, y=310)

        label_gun_ammo = font.render("Gun Ammo", True, BLACK)
        label_gun_ammo_rect = label_gun_ammo.get_rect(x=350, y=310)

        label_knife_dam = font.render("Knife damage", True, BLACK)
        label_knife_dam_rect = label_knife_dam.get_rect(x=545, y=310)

        knife_img1 = pygame.image.load("assets/img/tests/knife.png")
        knife_img2 = pygame.transform.rotate(knife_img1,45)
        knife_img3 = pygame.transform.scale(knife_img2,(100,100))

        bullet_img1 = pygame.image.load("assets/img/tests/bullet_26x64.png")
        bullet_img2 = pygame.transform.scale(bullet_img1,(30,90))

        label_stamina = font.render("Max stamina", True, BLACK)
        label_stamina_rect = label_stamina.get_rect(x=775, y=310)

        #############################################################
        font = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 70)
        gun_dam_value = font.render(str(self.player.damaged_gun), True, BLACK)
        gun_dam_rect_value = gun_dam_value.get_rect(x=165, y=450)

        gun_ammo_value = font.render(str(self.player.gun_ammo), True, BLACK)
        gun_ammo_rect_value = gun_ammo_value.get_rect(x=440, y=450)

        knife_dam_value = font.render(str(self.player.damaged_knife), True, BLACK)
        knife_dam_rect_value = knife_dam_value.get_rect(x=660, y=450)

        font = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 90)
        stamina_value = font.render(str(self.player.max_stamina), True, BLACK)
        stamina_rect_value = stamina_value.get_rect(x=800, y=390)
        

        res_btn1 = Button(80, 500, 120, 50, BLACK, (78, 85, 115), '.   10', 30)
        res_btn2 = Button(300, 500, 120, 50, BLACK, (78, 85, 115), '.        10', 30)
        res_btn3 = Button(520, 500, 120, 50, BLACK, (78, 85, 115), '.   10', 30)
        res_btn4 = Button(740, 500, 120, 50, BLACK, (78, 85, 115), '.        10', 30)

        self.buy_btn1 = Button(200, 500, 80, 50, BLACK, (115, 88, 78), 'Buy', 30)
        self.buy_btn2 = Button(420, 500, 80, 50, BLACK, (115, 88, 78), 'Buy', 30)
        self.buy_btn3 = Button(640, 500, 80, 50, BLACK, (115, 88, 78), 'Buy', 30)
        self.buy_btn4 = Button(860, 500, 80, 50, BLACK, (115, 88, 78), 'Buy', 30)

        self.screen.fill(BLACK)
        self.clock.tick(FPS)
        self.screen.blit(title, title_rect)
        self.screen.blit(subtitle, subtitle_rect)
        self.screen.blit(label_nb_ress1, label_nb_ress1_rect)
        self.screen.blit(label_nb_ress2, label_nb_ress2_rect)

        self.screen.blit(potato_img1, (370,210))
        self.screen.blit(corn_img1, (550,210))

        pygame.draw.rect(self.screen, (111, 115, 78), pygame.Rect(80, 300, 200, 200)) # gun damage
        self.screen.blit(label_gun_dam, label_gun_dam_rect)
        self.screen.blit(gun_dam_value, gun_dam_rect_value)
        self.screen.blit(res_btn1.image, res_btn1.rect)
        self.screen.blit(potato_img2, (90,505))
        self.screen.blit(self.buy_btn1.image, self.buy_btn1.rect)
        pygame.draw.rect(self.screen, (111, 115, 78), pygame.Rect(300, 300, 200, 200)) # gun ammo
        self.screen.blit(label_gun_ammo, label_gun_ammo_rect)
        self.screen.blit(gun_ammo_value, gun_ammo_rect_value)
        self.screen.blit(res_btn2.image, res_btn2.rect)
        self.screen.blit(corn_img2, (320,505))
        self.screen.blit(bullet_img2,(385,350))
        self.screen.blit(self.buy_btn2.image, self.buy_btn2.rect)
        pygame.draw.rect(self.screen, (111, 115, 78), pygame.Rect(520, 300, 200, 200)) # knife damage
        self.screen.blit(label_knife_dam, label_knife_dam_rect)
        self.screen.blit(knife_dam_value, knife_dam_rect_value)
        self.screen.blit(res_btn3.image, res_btn3.rect)
        self.screen.blit(potato_img2, (530,505))
        self.screen.blit(knife_img3,(560,350))
        self.screen.blit(self.buy_btn3.image, self.buy_btn3.rect)
        pygame.draw.rect(self.screen, (111, 115, 78), pygame.Rect(740, 300, 200, 200)) # stamina
        self.screen.blit(label_stamina, label_stamina_rect)
        self.screen.blit(stamina_value, stamina_rect_value)
        self.screen.blit(res_btn4.image, res_btn4.rect)
        self.screen.blit(corn_img2, (760,505))
        self.screen.blit(self.buy_btn4.image, self.buy_btn4.rect)
        self.curseur()

        pygame.display.update()

    def events_farm(self):
        # game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.farm_time = False
                    self.night_time = True
            if event.type == pygame.MOUSEBUTTONUP and self.buy_btn1.rect.collidepoint(pygame.mouse.get_pos()):
                if (self.player.potat_counter>0):
                    self.player.potat_counter-=10
                    # add gun damage
                    self.player.damaged_gun+=1
            if event.type == pygame.MOUSEBUTTONUP and self.buy_btn2.rect.collidepoint(pygame.mouse.get_pos()):
                if (self.player.corn_counter>0):
                    self.player.corn_counter-=10
                    # add gun ammo
                    self.player.gun_ammo+=1
                    self.player.gun_max_ammo+=1
            if event.type == pygame.MOUSEBUTTONUP and self.buy_btn3.rect.collidepoint(pygame.mouse.get_pos()):
                if (self.player.potat_counter>0):
                    self.player.potat_counter-=10
                    # add knife damage
                    self.player.damaged_knife+=1
            if event.type == pygame.MOUSEBUTTONUP and self.buy_btn4.rect.collidepoint(pygame.mouse.get_pos()):
                if (self.player.corn_counter>0):
                    self.player.corn_counter-=10
                    # add stamina
                    self.player.max_stamina+=10
                

    def main(self):
        self.playing = True

        while self.playing:
            if self.day_time:
                self.draw_day()
                self.events_day()
                self.update_day()
            elif self.farm_time:
                self.draw_farm()
                self.events_farm()
            elif self.night_time:
                self.draw()
                self.events_night()
                self.update_night()
                self.timer_value = int(self.timer_init - (pygame.time.get_ticks()) / 1000)
        pygame.display.update()

    def game_over(self):
        self.player.kill()
        self.intro_screen()
        # A REVOIR

    def curseur(self):
        mouse_pos = pygame.mouse.get_pos()
        CURSOR = pygame.transform.scale(
            pygame.image.load(os.path.join('assets/img/cursor', 'viewfinder.png')).convert_alpha(), (100, 100))
        CURSOR_RECT = CURSOR.get_rect()
        CURSOR_RECT.center = mouse_pos
        self.screen.blit(CURSOR, CURSOR_RECT)

    def intro_screen(self):
        click_sound.play()
        self.menu = True

        if self.music_played == True:
            pygame.mixer.music.load(os.path.join('assets/audio/bgm', 'Town1.ogg'))
            pygame.mixer.music.set_volume(0.05)
            pygame.mixer.music.play(fade_ms=2000)
        else:
            pygame.mixer.music.pause()

        title = self.font.render('Pog Champs Game', True, BLACK)
        title_rect = title.get_rect(x=self.screen.get_width() / 2 - title.get_width() / 2, y=100)

        play_button = Button((self.screen.get_width() / 2) - 100, 250, 200, 50, WHITE, BLACK, 'Play', 40)
        option_button = Button((self.screen.get_width() / 2) - 100, 350, 200, 50, WHITE, BLACK, 'Options', 40)
        credits_button = Button((self.screen.get_width() / 2) - 100, 450, 200, 50, WHITE, BLACK, 'Credits', 40)
        exit_button = Button((self.screen.get_width() / 2) - 100, 550, 200, 50, WHITE, BLACK, 'Exit', 40)

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
            elif option_button.is_pressed(mouse_pos, mouse_pressed):
                self.menu = False
                self.options = True
            elif credits_button.is_pressed(mouse_pos, mouse_pressed):
                self.menu = False
                self.credits = True
            elif exit_button.is_pressed(mouse_pos, mouse_pressed):
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
        title_rect = title.get_rect(x=self.screen.get_width() / 2 - title.get_width() / 2, y=100)

        font1 = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 50)
        font2 = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 30)

        sound_options = font1.render('Sound options', True, BLACK)
        sound_options_rect = sound_options.get_rect(x=self.screen.get_width() / 3 - title.get_width() / 2, y=200)

        if self.music_played == True:
            music_on_off = Button(700, 240, 60, 30, WHITE, BLACK, 'On', 30)
        else:
            music_on_off = Button(700, 240, 60, 30, BLACK, WHITE, 'Off', 30)

        if self.fx_played == True:
            fx_on_off = Button(700, 270, 60, 30, WHITE, BLACK, 'On', 30)
        else:
            fx_on_off = Button(700, 270, 60, 30, BLACK, WHITE, 'Off', 30)

        music_sound = font2.render('Music theme sound', True, BLACK)
        music_sound_rect = music_sound.get_rect(x=self.screen.get_width() / 3 - title.get_width() / 2, y=250)

        fx_sound = font2.render('FX sound', True, BLACK)
        fx_sound_rect = music_sound.get_rect(x=self.screen.get_width() / 3 - title.get_width() / 2, y=280)

        gameplay = font1.render('Gameplay', True, BLACK)
        gameplay_rect = gameplay.get_rect(x=self.screen.get_width() / 3 - title.get_width() / 2, y=320)

        top = font2.render('Top', True, BLACK)
        top_rect = top.get_rect(x=self.screen.get_width() / 3 - title.get_width() / 2, y=370)

        bottom = font2.render('Bottom', True, BLACK)
        bottom_rect = bottom.get_rect(x=self.screen.get_width() / 3 - title.get_width() / 2, y=400)

        left = font2.render('Left', True, BLACK)
        left_rect = left.get_rect(x=self.screen.get_width() / 3 - title.get_width() / 2, y=430)

        right = font2.render('Right', True, BLACK)
        right_rect = right.get_rect(x=self.screen.get_width() / 3 - title.get_width() / 2, y=460)

        if self.gameplay_ZQSD == True:
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
            back_button = Button((self.screen.get_width() / 2) - 100, 650, 200, 50, WHITE, BLACK, 'Back to game', 30)
        else:
            back_button = Button((self.screen.get_width() / 2) - 100, 650, 200, 50, WHITE, BLACK, 'Back to menu', 30)

        while self.options:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.options = False
                    self.running = False
                    exit()
                if event.type == pygame.MOUSEBUTTONUP and music_on_off.rect.collidepoint(pygame.mouse.get_pos()):
                    click_sound.play()
                    self.music_played = not self.music_played
                    if self.music_played:
                        pygame.mixer.music.unpause()
                    else:
                        pygame.mixer.music.pause()
                    self.options_screen()
                elif event.type == pygame.MOUSEBUTTONUP and fx_on_off.rect.collidepoint(pygame.mouse.get_pos()):
                    click_sound.play()
                    self.fx_played = not self.fx_played
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
                elif event.type == pygame.MOUSEBUTTONUP and (top_btn1.rect.collidepoint(pygame.mouse.get_pos()) or
                                                             bottom_btn1.rect.collidepoint(pygame.mouse.get_pos()) or
                                                             left_btn1.rect.collidepoint(pygame.mouse.get_pos()) or
                                                             right_btn1.rect.collidepoint(pygame.mouse.get_pos())):
                    self.gameplay_ZQSD = True
                    self.options_screen()
                elif event.type == pygame.MOUSEBUTTONUP and (top_btn2.rect.collidepoint(pygame.mouse.get_pos()) or
                                                             bottom_btn2.rect.collidepoint(pygame.mouse.get_pos()) or
                                                             left_btn2.rect.collidepoint(pygame.mouse.get_pos()) or
                                                             right_btn2.rect.collidepoint(pygame.mouse.get_pos())):
                    self.gameplay_ZQSD = False
                    self.options_screen()
                elif event.type == pygame.MOUSEBUTTONUP and back_button.rect.collidepoint(pygame.mouse.get_pos()) or (
                        event.type == pygame.KEYDOWN and (event.key == K_RCTRL or event.key == K_LCTRL)):
                    if self.back_to_game:
                        self.options = False
                        self.playing = True
                    else:
                        self.options = False
                        self.menu = True

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
        title_rect = title.get_rect(x=self.screen.get_width() / 2 - title.get_width() / 2, y=100)

        back_button = Button((self.screen.get_width() / 2) - 100, 650, 200, 50, WHITE, BLACK, 'Back to menu', 30)

        while self.credits:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.credits = False
                    self.running = False
                    exit()
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            if back_button.is_pressed(mouse_pos, mouse_pressed):
                self.credits = False
                self.menu = True

            self.screen.fill(BLUE)
            self.screen.blit(title, title_rect)
            self.screen.blit(back_button.image, back_button.rect)

            self.clock.tick(FPS)
            self.curseur()
            pygame.display.update()


g = Game()
while g.running == True:

    if g.menu == True:
        g.intro_screen()
    elif g.options == True:
        g.options_screen()
    elif g.credits == True:
        g.credits_screen()
    elif g.playing == True:
        g.new()
        g.main()
        g.game_over()

pygame.quit()
sys.exit()
