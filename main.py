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
pygame.display.set_caption('Crab Island')
pygame.display.set_icon(pygame.image.load("assets/img/tests/logo.png"))

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
   'EEEEEEEEEEEEEEEEDSSaggggggggggggggg$~~/////gbSSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSSaggggggggggggggg@gt/////tbSSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSSagggggggggg$P#gg@gipppppubSSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSSa]pp[gggggg@*@gg@ggggggggbSSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSSao//ygg$~~~(~(~~&ggggggggbSSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSSao//ggg@gggggggggggggggggbSSlEEEEEEEEEEEEEEEE',
   'EEEEEEEEEEEEEEEEDSSao//~~~&gggggggggggggggggbSSlEEEEEEEEEEEEEEEE',
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
spawn_sound = pygame.mixer.Sound(os.path.join('assets/audio', 'Up1.ogg'))
click_sound = pygame.mixer.Sound(os.path.join('assets/audio', 'Decision5.ogg'))

class Game:
	def __init__(self):
		self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		self.clock = pygame.time.Clock()
		self.running = True
		self.menu = True
		self.rules = False
		self.playing = False
		self.pause = False
		self.options = False
		self.credits = False
		self.font = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 70)
		self.music_played = True
		self.fx_played = True
		self.gameplay_ZQSD = True
		self.back_to_game = False
		self.tips = True
		self.timer_value = 30
		self.clock = pygame.time.Clock()
		self.game_day = 1;
		self.nb_crabs_left = 5+self.game_day*CRAB_ADD_PER_DAY
		self.gun_level = 1
		self.farmingTilePosGauche = [(21, 22), (22, 22), (21, 23), (22, 23), (21, 24), (22, 24), (21, 25), (22, 25)]
		self.farmingTilePosDroite = [(38, 16), (39, 16), (40, 16), (41, 16), (42, 16), (38, 17), (39, 17), (40, 17), (41, 17), (42, 17), (38, 18), (39, 18), (40, 18), (41, 18), (42, 18), (38, 19), (39, 19), (40, 19), (41, 19), (42, 19)]


		self.farminTileActGauche = []
		self.farminTileACTDroite = []
		self.apparitionFarmPossible = True
		self.peutCollect = False

		#Insane Easter Egss
		self.CODE = [pygame.K_UP, pygame.K_UP, pygame.K_DOWN, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_LEFT,
				pygame.K_RIGHT, pygame.K_b, pygame.K_a]
		self.current_code = []
		self.code_index = 0

		self.farm_btn_img11 = (3, 1) #red
		self.farm_btn_img12 = (3, 2)
		self.farm_btn_img21 = (1, 1) #green
		self.btn_img22 = (1, 2)
		self.farm_btn_img31 = (2, 1) #blue
		self.farm_btn_img32 = (2, 2)
		self.farm_btn_img41 = (5, 1) #purple
		self.btn_img42 = (5, 2)
		self.btn_img51 = (4, 1) #yellow
		self.btn_img52 = (4, 2)

		self.recolteTimeAct = 0;
		self.recolteTimeTotal = TEMPS_RECOLTE;

		self.passerDayAct = 0;
		self.passerDayTotal = TEMPS_PASSER_JOUR;

		self.xTopLefIsland = 0
		self.yTopLefIsland = 0
		self.hpCrab = HP_CRAB
		self.FireBullet = False

		self.day_time = True
		self.farm_time = False
		self.night_time = False

		self.campFireGrandit = True
		self.campFireReduit = False
		self.campFireXMax = random.randint(240, 500)
		self.campFireXMin = 0
		self.campFireYMin = 0
		self.campFireXAct = 240
		self.campfireYAct = 240

		self.nbCrabOnScreen = 0


		#Bruitage
		self.bullet_sound = pygame.mixer.Sound(os.path.join('assets/audio/se', 'Gun1.ogg'))
		self.switch_weapon_sound = pygame.mixer.Sound(os.path.join('assets/audio/se', 'Switch2.ogg'))
		self.damaged_sound = pygame.mixer.Sound(os.path.join('assets/audio/se/Damage1.ogg'))
		self.shop_sound = pygame.mixer.Sound(os.path.join('assets/audio/se/Shop2.ogg'))
		self.knife_sound = pygame.mixer.Sound(os.path.join('assets/audio/se/Sword4.ogg'))
		self.gun_reload_1 = pygame.mixer.Sound(os.path.join('assets/audio/se/Equip1.ogg'))
		self.gun_reload_2 = pygame.mixer.Sound(os.path.join('assets/audio/se/Equip3.ogg'))
		self.victory = pygame.mixer.Sound(os.path.join('assets/audio/me/Victory1.ogg'))
		self.easter_eggs = pygame.mixer.Sound(os.path.join('assets/audio/se/Easter Eggs.ogg'))
		self.easter_eggs.set_volume(0.5)
		#Musique de fond
		self.sound_title = os.path.join('assets/audio/bgm/Town1.ogg')
		self.sound_farm = os.path.join('assets/audio/bgm', 'Town8.ogg')
		self.sound_night = os.path.join('assets/audio/bgs', 'Night.ogg')

		pygame.mouse.set_visible(False)

		if self.fx_played == True:
			self.bullet_sound.set_volume(0.1)
			self.switch_weapon_sound.set_volume(0.08)
			spawn_sound.set_volume(0.1)
			click_sound.set_volume(0.1)
			self.damaged_sound.set_volume(0.05)
			self.shop_sound.set_volume(0.05)
			self.knife_sound.set_volume(0.05)
			self.gun_reload_1.set_volume(0.05)
			self.gun_reload_2.set_volume(0.05)
			self.victory.set_volume(0.05)
		else:
			self.bullet_sound.set_volume(0)
			self.switch_weapon_sound.set_volume(0)
			spawn_sound.set_volume(0)
			click_sound.set_volume(0)
			self.damaged_sound.set_volume(0)
			self.shop_sound.set_volume(0)
			self.knife_sound.set_volume(0)
			self.gun_reload_1.set_volume(0)
			self.gun_reload_2.set_volume(0)
			self.victory.set_volume(0)

		self.character_spritesheet = SpriteSheet(
			pygame.image.load(os.path.join('assets/img/tests', 'CrackedOutTheWoahZOOOODud.png')).convert_alpha())
		self.terrain_spritesheet = SpriteSheet(
			pygame.image.load(os.path.join('assets/img/tests', 'spritesBG_3par8_64x64.png')).convert_alpha())
		self.crab_spritesheet = SpriteSheet(
			pygame.image.load(os.path.join('assets/img/tests/crabUpdate_100x78.png')).convert_alpha())
		self.night_effet = [
			pygame.image.load(os.path.join('assets/img/tests', 'overlayN.png')).convert_alpha(),
			pygame.image.load(os.path.join('assets/img/tests', 'overlayNormalRed.png')).convert_alpha(),
			pygame.image.load(os.path.join('assets/img/tests', 'overlayBeforeDeath.png')).convert_alpha()
		]  # lul
		self.fireEffect = pygame.image.load(os.path.join('assets/img/tests', 'gunfire_overlay.png')).convert_alpha()
		self.campFireEffect = pygame.image.load(os.path.join('assets/img/tests', 'fire_overlay2.png')).convert_alpha()
		self.campFireEffect = pygame.transform.scale(self.campFireEffect, (500, 500))

		#init farm

		self.farm_title = self.font.render("It's farmer time", True, WHITE)
		self.farm_title_rect = self.farm_title.get_rect(x=self.screen.get_width() / 2 - self.farm_title.get_width() / 2, y=100)

		self.farm_font = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 25)
		self.farm_subtitle = self.farm_font.render("Improve your skills and weapon damages", True, WHITE)
		self.farm_subtitle_rect = self.farm_subtitle.get_rect(x=self.screen.get_width() / 2 - self.farm_subtitle.get_width() / 2, y=150)

		self.farm_potato_img1 = pygame.image.load("assets/img/tests/potato.png")
		self.farm_potato_img2 = pygame.transform.scale(self.farm_potato_img1, (30,30))

		self.farm_corn_img1 = pygame.image.load("assets/img/tests/corna.png")
		self.farm_corn_img2 = pygame.transform.scale(self.farm_corn_img1, (30,30))
 
		self.farm_font_special = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 40)


		self.farm_font = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 40)
		self.farm_label_gun_dam = self.farm_font.render("Gun damage", True, BLACK)
		self.farm_label_gun_dam_rect = self.farm_label_gun_dam.get_rect(x=110, y=320)

		self.farm_label_gun_ammo = self.farm_font.render("Gun ammo", True, BLACK)
		self.farm_label_gun_ammo_rect = self.farm_label_gun_ammo.get_rect(x=350, y=320)

		self.farm_label_knife_dam = self.farm_font.render("Knife damage", True, BLACK)
		self.farm_label_knife_dam_rect = self.farm_label_knife_dam.get_rect(x=545, y=320)


		self.farm_knife_img1 = pygame.image.load("assets/img/tests/knife.png")
		self.farm_knife_img2 = pygame.transform.rotate(self.farm_knife_img1,45)
		self.farm_knife_img3 = pygame.transform.scale(self.farm_knife_img2,(100,100))

		self.farm_bullet_img1 = pygame.image.load("assets/img/tests/bullet_26x64.png")
		self.farm_bullet_img2 = pygame.transform.scale(self.farm_bullet_img1,(30,90))

		self.farm_label_stamina = self.farm_font.render("Max stamina", True, BLACK)
		self.farm_label_stamina_rect = self.farm_label_stamina.get_rect(x=775, y=320)

		self.farm_buy_btn1 = Button(200, 500, 80, 50, BLACK, self.farm_btn_img31, 'Buy', 30)
		self.farm_buy_btn2 = Button(420, 500, 80, 50, BLACK, self.farm_btn_img31, 'Buy', 30)
		self.farm_buy_btn3 = Button(640, 500, 80, 50, BLACK, self.farm_btn_img31, 'Buy', 30)
		self.farm_buy_btn4 = Button(860, 500, 80, 50, BLACK, self.farm_btn_img31, 'Buy', 30)

		self.farm_res_btn1 = Button(80, 500, 120, 50, BLACK, self.farm_btn_img21, '.     10', 30)
		self.farm_res_btn2 = Button(300, 500, 120, 50, BLACK, self.farm_btn_img21, '.      10', 30)
		self.farm_res_btn3 = Button(520, 500, 120, 50, BLACK, self.farm_btn_img21, '.     10', 30)
		self.farm_res_btn4 = Button(740, 500, 120, 50, BLACK, self.farm_btn_img21, '.      10', 30)



		self.farm_start_before_farm = Button(self.screen.get_width()/2-100, 650, 200, 50, BLACK, self.farm_btn_img11, 'Start', 40)



	def createTileMap(self):

		self.xTopLefIsland = (17 - OFFSETX) * TILE_WIDTH
		self.yTopLefIsland = (12 - OFFSETY) * TILE_HEIGHT
		for i, row in enumerate(tilemap):
			for j, column in enumerate(row):
				# basic textures
				if column == 'E':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'water', True, False, i, j)
				if column == 'S':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'sand', False, False, i, j)
				if column == 'g':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'grass', False, False, i, j)
				if column == '/':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'dirt', False, False, i, j)

				# map border textures
				if column == 'T':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'topWater', True, False, i, j)
				if column == 'G':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'topLeftWaterBord', True, False, i, j)
				if column == 'R':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'topRightWaterBord', True, False, i, j)
				if column == 'B':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'bottomWaterBord', True, False, i, j)
				if column == 'V':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'bottomLeftSand', True, False, i, j)
				if column == 'X':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'bottomRightSand', True, False, i, j)
				if column == 'l':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'rightWaterBord', True, False, i, j)
				if column == 'D':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'leftWaterBord', True, False, i, j)

				# Sand + Grass Transition
				if column == '1':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'topLeftSandGrassT', False, False, i, j)
				if column == '2':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'topRightSandGrassT', False, False, i, j)
				if column == 'c':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'topSandGrassT', False, False, i, j)
				if column == 'a':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'leftSandGrassT', False, False, i, j)
				if column == 'b':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'rightSandGrassT', False, False, i, j)
				if column == '4':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'bottomRightSandGrassT', False, False, i, j)
				if column == '3':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'bottomleftSandGrassT', False, False, i, j)
				if column == 'x':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'bottomSandGrassT', False, False, i, j)

				# Fences
				if column == ']':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'topLeftFence', True, False, i, j)
				if column == '[':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'topRightFence', True, False, i, j)
				if column == 'p':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'topFence', True, False, i, j)
				if column == 'o':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'sideFence', True, False, i, j)
				if column == 'i':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'bottomLeftFence', True, False, i, j)
				if column == 'u':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'bottomRightFence', True, False, i, j)
				if column == 'y':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'topStopFence', True, False, i, j)
				if column == 't':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'bottomStopFence', True, False, i, j)

				#campfire
				if column == '*':
					self.campFire = Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'campFire', True, False, i, j)

				#potato
				if column == ':':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'dirt', False, False, i, j)
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'firstStagePotato', True, True, i, j)

				#Road
				if column == '~':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'roadH', False, False, i, j)
				if column == '@':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'roadV', False, False, i, j)
				if column == '#':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'roadTopR', False, False, i, j)
				if column == '$':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'roadTopL', False, False, i, j)
				if column == '^':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'roadBottomLeft', False, False, i, j)
				if column == '&':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'roadBottomRight', False, False, i, j)
				if column == '(':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'roadT', False, False, i, j)
				if column == ')':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'roadTReverse', False, False, i, j)
				if column == '_':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'roadTRight', False, False, i, j)
				if column == '+':
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'roadTLeft', False, False, i, j)


				# Player pog
				if column == 'P':
					self.player = Player(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, self.gameplay_ZQSD)
					Block(self, (j - OFFSETX) * TILE_WIDTH, (i - OFFSETY) * TILE_HEIGHT, 'roadH', False, False, i, j)

		self.screen.blit(
			pygame.image.load(os.path.join('assets/img/tests', 'spritesBG_3par8_64x64.png')).convert_alpha(), (0, 0))

	def after_win(self):
		pygame.mixer.fadeout(1000)
		pygame.mixer.music.set_volume(0.05)
		pygame.mixer.music.load(self.sound_farm)
		pygame.mixer.music.play(fade_ms=1000)
		self.timer_value = 30
		self.game_day+=1
		self.nbCrabOnScreen = 0
		self.player.player_health=3
		self.nb_crabs_left = 5+self.game_day*CRAB_ADD_PER_DAY
		for enemies in self.enemies:
			enemies.kill()
		self.night_time=False
		self.day_time=True

	def after_game_over(self):
		pygame.mixer.fadeout(1000)
		pygame.mixer.music.load(self.sound_farm)
		pygame.mixer.music.set_volume(0.05)
		pygame.mixer.music.play(fade_ms=2000)
		for enemies in self.enemies:
			enemies.kill()
		self.night_time=False
		self.reset_value_after_game_over()
		#self.day_time=True
		
		#self.menu = True
		self.intro_screen()

	def reset_value_after_game_over(self):
		self.game_day=1
		self.nb_crabs_left = 5+self.game_day*CRAB_ADD_PER_DAY
		self.player.player_health = 3
		self.player.corn_counter = 0
		self.player.potat_counter = 0
		self.player.current_stamina = 100
		self.player.damaged_gun = 0
		self.player.damaged_knife = 0
		self.player.gun_ammo = 5
		self.timer_value = 30

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
		pygame.mixer.fadeout(1000)
		pygame.mixer.music.load(self.sound_farm)
		pygame.mixer.music.set_volume(0.05)
		pygame.mixer.music.play(fade_ms=2000)

		self.day_time = True
		self.farm_time = False
		self.night_time = False
		self.createTileMap()

	def events_night(self):
		# Farm Zone
		if (self.nb_crabs_left == 0):
			self.after_win()
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
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_r:
					if not (self.player.in_realoding):
						if ((self.player.current_weapon == "gun") and not self.player.gun_ammo == self.player.gun_max_ammo):
							self.gun_reload_1.play()
							self.player.in_realoding = True
				elif event.key == pygame.K_i:
					self.tips = not self.tips
					if self.tips:
						self.tips1.set_alpha(150)
						self.tips3.set_alpha(150)
					else:
						self.tips1.set_alpha(0)
						self.tips3.set_alpha(0)
				elif event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
					self.playing = not self.playing
					self.options = not self.options
					self.back_to_game = True
			if event.type == pygame.KEYDOWN: #event Konami code
				if event.key == self.CODE[self.code_index ]:
					self.current_code.append(event.key)
					self.code_index  += 1
					if self.current_code == self.CODE:
						self.code_index  = 0
						self.easter_eggs.play()
				else:
					self.current_code = []
					self.code_index = 0
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_ESCAPE:
					self.pause = True
					#self.playing = False
					self.intro_screen()

	def events_day(self):
		# game loop events
		if self.timer_value < 0:
			self.shop_sound.play()
			self.day_time = False
			self.farm_time = True
		else:
			self.timer_value -= 1/60
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.playing = False
				self.running = False
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_i:
					self.tips = not self.tips
					if self.tips:
						self.tips1.set_alpha(150)
						self.tips3.set_alpha(150)
					else:
						self.tips1.set_alpha(0)
						self.tips3.set_alpha(0)
			if event.type == pygame.MOUSEBUTTONUP:
				self.recolteTimeAct = 0
				self.passerDayAct = 0
			if event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LSHIFT:
					self.player.sprint(event)
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_ESCAPE:
					self.pause = True
					self.playing = False
					self.intro_screen()

	def update_night(self):
		# game llop events
		self.player.update()
		self.blocks_no_collid_not_farm.update()
		self.blocks_collid.update()
		self.enemies.update()
		self.bullets.update()
		# crabSpawn
		if (random.randint(0, TIME_SPAWN_CRAB)) == 0:
			if self.nbCrabOnScreen < NB_CRAB_MAX:
				self.nbCrabOnScreen += 1
				self.crab_spawn(self.hpCrab + RATIO_VIE_CRAB*(self.game_day-1), random.randint(CRAB_VITESSE_MIN, CRAB_VITESSE_MAX) + ((self.game_day-1) / 10))

	def crab_spawn(self, hp,speed):
		spawn_sound.play()
		# Crab(self, self.player.x + (random.choice((-1, 1)) * random.randint(150, 250)),self.player.y + (random.choice((-1, 1)) * random.randint(150, 250)), 100, 2)
		position = random.randint(1,5)
		if position == 1: # Corner Top Left
			Crab(self, self.xTopLefIsland, self.yTopLefIsland, hp,speed)
		elif position == 2: # Corner Top Right
			Crab(self, self.xTopLefIsland + ISLANDWIDTH, self.yTopLefIsland, hp, speed)
		elif position == 3: # Corner Bottom Left
			Crab(self, self.xTopLefIsland, self.yTopLefIsland + ISLANDHEIGHT, hp, speed)
		elif position == 4: # Corner Bottom Right
			Crab(self, self.xTopLefIsland + ISLANDWIDTH, self.yTopLefIsland + ISLANDHEIGHT, hp, speed)
		elif position == 5: # Tous en même temps
			Crab(self, self.xTopLefIsland, self.yTopLefIsland, hp, speed)
			Crab(self, self.xTopLefIsland + ISLANDWIDTH, self.yTopLefIsland, hp, speed)
			Crab(self, self.xTopLefIsland, self.yTopLefIsland + ISLANDHEIGHT, hp, speed)
			Crab(self, self.xTopLefIsland + ISLANDWIDTH, self.yTopLefIsland + ISLANDHEIGHT, hp, speed)

	def draw(self):
		#game loop draw
		font = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 35)
		self.crabs_killed = font.render("Crabs left: "+str(self.nb_crabs_left), True, WHITE)
		self.crabs_killed.set_alpha(150)
		self.crabs_killed_rect = self.crabs_killed.get_rect(x=20, y=20)
		counter_day = font.render("Day: "+str(self.game_day), True, WHITE)
		counter_day.set_alpha(150)
		counter_day_rect = counter_day.get_rect(x=20, y=730)

		font = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 25)
		current_defense_label = font.render("Current defense", True, WHITE)
		current_defense_label.set_alpha(150)
		current_defense_label_rect = current_defense_label.get_rect(x=860, y=650)

		heart_img1 = pygame.image.load("assets/img/tests/heart.png")
		heart_img2 = pygame.transform.scale(heart_img1, (30,30))

		if self.player.current_weapon=="gun":
			if self.gun_level==1:
				gun_img1 = pygame.image.load("assets/img/tests/gunNormal2.png")
				gun_img2 = pygame.transform.scale(gun_img1,(70,45))
				gun_img2.set_alpha(150)
			elif self.gun_level==2:
				gun_img1 = pygame.image.load("assets/img/tests/gunUpgraded2.png")
				gun_img2 = pygame.transform.scale(gun_img1,(70,45))
				gun_img2.set_alpha(150)
			font = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 25)
			current_ammo = font.render(str(self.player.gun_ammo)+"/"+str(self.player.gun_max_ammo), True, WHITE)
			current_ammo.set_alpha(150)
			current_ammo_label_rect = current_ammo.get_rect(x=880, y=720)
		else:
			knife_img1 = pygame.image.load("assets/img/tests/knife.png")
			knife_img2 = pygame.transform.rotate(knife_img1,45)
			knife_img2.set_alpha(150)

		self.screen.fill(BLACK)
		self.all_sprites.draw(self.screen)
		self.clock.tick(FPS)
		

		if (self.player.player_health == 3):
			self.screen.blit(self.night_effet[0], (0,0))
		elif (self.player.player_health == 2):
			self.screen.blit(self.night_effet[1], (0,0))
		else:
			self.screen.blit(self.night_effet[2], (0,0))
		if self.FireBullet:
			self.screen.blit(self.fireEffect, (self.player.rect.centerx - self.fireEffect.get_width() / 2, self.player.rect.centery - self.fireEffect.get_height() / 2))
			self.FireBullet = False
		self.screen.blit(counter_day,counter_day_rect)
		self.screen.blit(self.crabs_killed,self.crabs_killed_rect)
		self.screen.blit(current_defense_label,current_defense_label_rect)
		if self.player.current_weapon=="gun":
			self.screen.blit(gun_img2, (900,680))
			self.screen.blit(current_ammo,current_ammo_label_rect)
		else:
			self.screen.blit(knife_img2, (900,680))
		for i in range(int(self.player.player_health)):
			self.screen.blit(heart_img2, (900+35*i,20))

		self.campFireAnimation()
		if self.player.in_realoding:
			if self.player.gun_time_animation > self.player.animation_gun_duration:
				self.player.in_realoding = False
				self.player.gun_time_animation = 0
				self.gun_reload_2.play()
				self.player.gun_ammo = self.player.gun_max_ammo
			else:
				self.player.gun_time_animation = self.animationLoading(self.player.animation_gun_duration,self.player.gun_time_animation,WHITE)


		# trouver
		pygame.draw.rect(self.screen, BLACK, pygame.Rect(900, 60, 100, 20), 2)
		pygame.draw.rect(self.screen, DARK_GREEN, pygame.Rect(902, 62, ((self.player.current_stamina * 100 ) // self.player.max_stamina ) - 4, 16))
		

		self.curseur()
		pygame.display.update()

	def draw_day(self):

		# game loop draw
		font = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 35)
		self.timer = font.render("Time left:  " + str(int(math.ceil(self.timer_value))) + "s", True, BLACK)
		self.timer_rect = self.timer.get_rect(x=20, y=20)

		counter_day = font.render("Day: "+str(self.game_day), True, BLACK)
		counter_day_rect = counter_day.get_rect(x=20, y=730)

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
			self.tips1 = font.render("Press 'esc' to open options", True, BLACK)
			self.tips1.set_alpha(150)
			self.tips1_rect = self.tips1.get_rect(x=self.screen.get_width() / 2 - self.tips1.get_width() / 2, y=130)

			self.tips3 = font.render("Press 'i' to toggle tips", True, BLACK)
			self.tips3.set_alpha(150)
			self.tips3_rect = self.tips3.get_rect(x=self.screen.get_width() / 2 - self.tips3.get_width() / 2, y=160)

		self.collectMessage = font.render("Right click to collect", True, BLACK)
		self.collectMessage.set_alpha(150)
		self.collectMessage_rect = self.collectMessage.get_rect(x=WINDOW_WIDTH / 2 - self.collectMessage.get_width() / 2, y=700)

		self.comebackMessage = font.render("Come back when the plant has fully grown", True, BLACK)
		self.comebackMessage.set_alpha(150)
		self.comebackMessage_rect = self.comebackMessage.get_rect(x=WINDOW_WIDTH / 2 - self.comebackMessage.get_width() / 2, y=700)

		self.marketMessage = font.render("Left click to go to the market", True, BLACK)
		self.marketMessage.set_alpha(150)
		self.marketMessage_rect = self.marketMessage.get_rect(x=WINDOW_WIDTH / 2 - self.marketMessage.get_width() / 2, y=700)

		# game loop draw
		self.screen.fill(BLACK)
		self.all_sprites.draw(self.screen)
		self.screen.blit(self.tips1, self.tips1_rect)
		self.screen.blit(self.tips3, self.tips3_rect)
		self.screen.blit(self.timer, self.timer_rect)
		self.screen.blit(counter_day,counter_day_rect)
		self.screen.blit(potato_img2, (970,20))
		self.screen.blit(corn_img2, (970,80))
		self.screen.blit(label_nb_ress1,label_nb_ress1_rect)
		self.screen.blit(label_nb_ress2,label_nb_ress2_rect)
		self.clock.tick(FPS)

		for block in self.blocks_no_collid_farm:
			if block.block_type == 'secondStageCorn' or block.block_type == 'secondStagePotat' or block.block_type == 'rottenPotat' or block.block_type == 'rottenCorn':
					if pygame.sprite.collide_mask(self.player, block):
						self.screen.blit(self.collectMessage, self.collectMessage_rect)
						self.peutCollect = True
			elif (block.block_type == 'firstStagePotato' or block.block_type == 'firstStageCorn') and self.peutCollect:
				if pygame.sprite.collide_mask(self.player, block):
					self.screen.blit(self.comebackMessage, self.comebackMessage_rect)
			self.peutCollect = False


		if pygame.mouse.get_pressed()[2]:
			for block in self.blocks_no_collid_farm:
				if block.block_type == 'secondStageCorn' or block.block_type == 'secondStagePotat' or block.block_type == 'rottenPotat' or block.block_type == 'rottenCorn':
					if pygame.sprite.collide_mask(self.player, block):
						if self.recolteTimeAct < self.recolteTimeTotal :
							self.recolteTimeAct = self.animationLoading(self.recolteTimeTotal, self.recolteTimeAct, GREEN_VALIDATION)
						else:
							if block.block_type == 'secondStageCorn':
								self.player.corn_counter += random.randint(3, 5)
							elif block.block_type == 'rottenCorn':
								self.player.corn_counter += random.randint(1, 2)
							elif block.block_type == 'secondStagePotat':
								self.player.potat_counter += random.randint(3, 5)
							else:
								self.player.potat_counter += random.randint(1, 2)
							case = (block.i, block.j)
							if block.i > 30: # si c'étais un block du champ droit
								self.farmingTilePosDroite.append(case)
								self.apparitionFarmPossible = True
							else:
								self.farmingTilePosGauche.append(case)
								self.apparitionFarmPossible = True

							block.kill()
			if not(pygame.sprite.spritecollide(self.player, self.blocks_no_collid_farm, False)): # si bug
					self.recolteTimeAct = 0
		if pygame.mouse.get_pressed()[0]:
			if self.campFire.rect.collidepoint(pygame.mouse.get_pos()):
				if self.passerDayAct < self.passerDayTotal :
					self.passerDayAct = self.animationLoading(self.passerDayTotal, self.passerDayAct, ORANGE)
				else:
					self.shop_sound.play()
					self.day_time = False
					self.farm_time = True
		mouse_pos = pygame.mouse.get_pos()
		if self.campFire.rect.collidepoint(mouse_pos[0],mouse_pos[1]):
			self.screen.blit(self.marketMessage, self.marketMessage_rect)

		self.campFireAnimation()
		self.curseur()

		pygame.display.update()




		# self.campFireGrandit = True
		# self.campFireReduit = False
		# self.campFireXMax = random.randint(512, 812)
		# self.campFireYMax = random.randint(384, 609)
		# self.campFireXMin = 0
		# self.campFireYMin = 0
		# self.campFireXAct = 512
		# self.campfireYAct = 384


	def campFireAnimation(self):
		if self.campFireGrandit:
			if self.campFireXMax > self.campFireXAct:
				self.campFireXAct += 5
			else:
				self.campFireGrandit = False
				self.campFireReduit = True
				self.campFireXMin = random.randint(150, 240)
		else:
			if self.campFireXMin < self.campFireXAct:
				self.campFireXAct -= 5
			else:
				self.campFireGrandit = True
				self.campFireReduit = False
				self.campFireXMax = random.randint(240, 500)
		self.campfireYAct = self.campFireXAct
		#self.campFireEffect = pygame.transform.scale(self.campFireEffect, (self.campFireXAct, self.campfireYAct))
		alpha = (105 * (self.campFireXAct-150) ) // 350
		alpha += 150
		self.campFireEffect.set_alpha(alpha)
		self.screen.blit(self.campFireEffect, ((self.xTopLefIsland + (31-16.8) * TILE_WIDTH) - self.campFireEffect.get_width() / 2, (self.yTopLefIsland + (21-11.8) * TILE_HEIGHT) - self.campFireEffect.get_height() / 2))


	def update_day(self):
		# game llop events

		if self.apparitionFarmPossible and random.randint(1,POTATO_APPEAR_TIME) == 15:
			self.caseMaxFarmGauche = len(self.farmingTilePosGauche)
			self.caseMaxFarmDroite = len(self.farmingTilePosDroite)

			if self.caseMaxFarmGauche == 0 and self.caseMaxFarmDroite > 0: # Si peut que spawn a droite
				pos = random.randint(1, self.caseMaxFarmDroite)
				case = self.farmingTilePosDroite[pos-1]
				self.farmingTilePosDroite.remove(case)
				if random.randint(1,2) == 2:
					element = 'Potato'
				else:
					element = 'Corn'
				patateX = case[0]
				patateY = case[1]
				Block(self, self.xTopLefIsland + (patateX - 17) * TILE_WIDTH, self.yTopLefIsland + (patateY - 12) * TILE_HEIGHT, 'firstStage' + element, True, True, patateX, patateY)


			elif self.caseMaxFarmDroite == 0 and self.caseMaxFarmGauche > 0: # Si peut que spawn a gauche
				pos = random.randint(1, self.caseMaxFarmGauche)
				case = self.farmingTilePosGauche[pos-1]
				self.farmingTilePosGauche.remove(case)
				if random.randint(1,2) == 2:
					element = 'Potato'
				else:
					element = 'Corn'
				patateX = case[0]
				patateY = case[1]
				Block(self, self.xTopLefIsland + (patateX - 17) * TILE_WIDTH, self.yTopLefIsland + (patateY - 12) * TILE_HEIGHT, 'firstStage' + element, True, True, patateX, patateY)


			elif self.caseMaxFarmDroite > 0 and self.caseMaxFarmGauche > 0: # Si peut spawn a droite et a gauche
				if random.randint(1, 2) == 2: # spawn a gauche
					pos = random.randint(1, self.caseMaxFarmGauche)
					case = self.farmingTilePosGauche[pos-1]

					self.farmingTilePosGauche.remove(case)

					if random.randint(1,2) == 2:
						element = 'Potato'
					else:
						element = 'Corn'
					patateX = case[0]
					patateY = case[1]
					Block(self, self.xTopLefIsland + (patateX - 17) * TILE_WIDTH, self.yTopLefIsland + (patateY - 12) * TILE_HEIGHT, 'firstStage' + element, True, True, patateX, patateY)

				else: # spawn a droite
					pos = random.randint(1, self.caseMaxFarmDroite)
					case = self.farmingTilePosDroite[pos-1]

					self.farmingTilePosDroite.remove(case)

					if random.randint(1,2) == 2:
						element = 'Potato'
					else:
						element = 'Corn'
					patateX = case[0]
					patateY = case[1]
					Block(self, self.xTopLefIsland + (patateX - 17) * TILE_WIDTH, self.yTopLefIsland + (patateY - 12) * TILE_HEIGHT, 'firstStage' + element, True, True, patateX, patateY)

			else:
				self.apparitionFarmPossible = False



		self.all_sprites.update()

	def draw_farm(self):

		self.farm_label_nb_ress1 = self.farm_font_special.render(str(self.player.potat_counter), True, WHITE)
		self.farm_label_nb_ress1_rect = self.farm_subtitle.get_rect(x=450, y=230)
		self.farm_label_nb_ress2 = self.farm_font_special.render(str(self.player.corn_counter), True, WHITE)
		self.farm_label_nb_ress2_rect = self.farm_subtitle.get_rect(x=630,y=230)


		if self.gun_level==1:
			gun_img1 = pygame.image.load("assets/img/tests/gunNormal2.png")
			gun_img2 = pygame.transform.scale(gun_img1,(100,70))
		elif self.gun_level==2:
			gun_img1 = pygame.image.load("assets/img/tests/gunUpgraded2.png")
			gun_img2 = pygame.transform.scale(gun_img1,(100,70))


		self.farm_font = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 60)
		self.farm_gun_dam_value = self.farm_font.render("+"+str(self.player.damaged_gun), True, BLACK)
		self.farm_gun_dam_rect_value = self.farm_gun_dam_value.get_rect(x=200, y=450)

		self.farm_gun_ammo_value = self.farm_font.render("+"+str(self.player.gun_ammo), True, BLACK)
		self.farm_gun_ammo_rect_value = self.farm_gun_ammo_value.get_rect(x=420, y=450)

		self.farm_knife_dam_value = self.farm_font.render("+"+str(self.player.damaged_knife), True, BLACK)
		self.farm_knife_dam_rect_value = self.farm_knife_dam_value.get_rect(x=640, y=450)

		self.farm_font = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 90)
		self.farm_stamina_value = self.farm_font.render(str(self.player.max_stamina), True, BLACK)
		self.farm_stamina_rect_value = self.farm_stamina_value.get_rect(x=800, y=390)

		#############################################################

		mouse_pos = pygame.mouse.get_pos()
		if self.farm_buy_btn1.rect.collidepoint(mouse_pos[0],mouse_pos[1]):
			self.farm_buy_btn1 = Button(200, 500, 80, 50, BLACK, self.farm_btn_img32, 'Buy', 30)
			self.farm_buy_btn2 = Button(420, 500, 80, 50, BLACK, self.farm_btn_img31, 'Buy', 30)
			self.farm_buy_btn3 = Button(640, 500, 80, 50, BLACK, self.farm_btn_img31, 'Buy', 30)
			self.farm_buy_btn4 = Button(860, 500, 80, 50, BLACK, self.farm_btn_img31, 'Buy', 30)
			self.farm_start_before_farm = Button(self.screen.get_width()/2-100, 650, 200, 50, BLACK, self.farm_btn_img11, 'Start', 40)
		else:
			self.farm_buy_btn1 = Button(200, 500, 80, 50, BLACK, self.farm_btn_img31, 'Buy', 30)
			if self.farm_buy_btn2.rect.collidepoint(mouse_pos[0],mouse_pos[1]):
				self.farm_buy_btn2 = Button(420, 500, 80, 50, BLACK, self.farm_btn_img32, 'Buy', 30)
				self.farm_buy_btn3 = Button(640, 500, 80, 50, BLACK, self.farm_btn_img31, 'Buy', 30)
				self.farm_buy_btn4 = Button(860, 500, 80, 50, BLACK, self.farm_btn_img31, 'Buy', 30)
				self.farm_start_before_farm = Button(self.screen.get_width()/2-100, 650, 200, 50, BLACK, self.farm_btn_img11, 'Start', 40)
			else:
				self.farm_buy_btn2 = Button(420, 500, 80, 50, BLACK, self.farm_btn_img31, 'Buy', 30)
				if self.farm_buy_btn3.rect.collidepoint(mouse_pos[0],mouse_pos[1]):
					self.farm_buy_btn3 = Button(640, 500, 80, 50, BLACK, self.farm_btn_img32, 'Buy', 30)
					self.farm_buy_btn4 = Button(860, 500, 80, 50, BLACK, self.farm_btn_img31, 'Buy', 30)
					self.farm_start_before_farm = Button(self.screen.get_width()/2-100, 650, 200, 50, BLACK, self.farm_btn_img11, 'Start', 40)
				else:
					self.farm_buy_btn3 = Button(640, 500, 80, 50, BLACK, self.farm_btn_img31, 'Buy', 30)
					if self.farm_buy_btn4.rect.collidepoint(mouse_pos[0],mouse_pos[1]):
						self.farm_buy_btn4 = Button(860, 500, 80, 50, BLACK, self.farm_btn_img32, 'Buy', 30)
						self.farm_start_before_farm = Button(self.screen.get_width()/2-100, 650, 200, 50, BLACK, self.farm_btn_img11, 'Start', 40)
					else:
						self.farm_buy_btn4 = Button(860, 500, 80, 50, BLACK, self.farm_btn_img31, 'Buy', 30)
						if self.farm_start_before_farm.rect.collidepoint(mouse_pos[0],mouse_pos[1]):
							self.farm_start_before_farm = Button(self.screen.get_width()/2-100, 650, 200, 50, BLACK, self.farm_btn_img12, 'Start', 40)
						else:
							self.farm_start_before_farm = Button(self.screen.get_width()/2-100, 650, 200, 50, BLACK, self.farm_btn_img11, 'Start', 40)

		self.screen.blit(pygame.image.load('assets/img/tests/shopBG.png'),(0,0))
		self.clock.tick(60)
		self.screen.blit(self.farm_title, self.farm_title_rect)
		self.screen.blit(self.farm_subtitle, self.farm_subtitle_rect)
		self.screen.blit(self.farm_label_nb_ress1, self.farm_label_nb_ress1_rect)
		self.screen.blit(self.farm_label_nb_ress2, self.farm_label_nb_ress2_rect)

		self.screen.blit(self.farm_potato_img1, (370,210))
		self.screen.blit(self.farm_corn_img1, (550,210))


		background_square = ButtonNoText(70,290,220,240,self.farm_btn_img41)
		self.screen.blit(background_square.image, background_square.rect)
		self.screen.blit(self.farm_label_gun_dam, self.farm_label_gun_dam_rect)
		self.screen.blit(self.farm_gun_dam_value, self.farm_gun_dam_rect_value)
		self.screen.blit(self.farm_res_btn1.image, self.farm_res_btn1.rect)
		self.screen.blit(self.farm_potato_img2, (100,507))
		self.screen.blit(gun_img2,(130,360))
		self.screen.blit(self.farm_buy_btn1.image, self.farm_buy_btn1.rect)

		# background_square = ButtonNoText(290,290,220,240,self.farm_btn_img41)
		# self.screen.blit(background_square.image, background_square.rect)
		self.screen.blit(self.farm_label_gun_ammo, self.farm_label_gun_ammo_rect)
		self.screen.blit(self.farm_gun_ammo_value, self.farm_gun_ammo_rect_value)
		self.screen.blit(self.farm_res_btn2.image, self.farm_res_btn2.rect)
		self.screen.blit(self.farm_corn_img2, (322,507))
		self.screen.blit(self.farm_bullet_img2,(385,350))
		self.screen.blit(self.farm_buy_btn2.image, self.farm_buy_btn2.rect)

		# background_square = ButtonNoText(510,290,220,240,self.farm_btn_img41)
		# self.screen.blit(background_square.image, background_square.rect)
		self.screen.blit(self.farm_label_knife_dam, self.farm_label_knife_dam_rect)
		self.screen.blit(self.farm_knife_dam_value, self.farm_knife_dam_rect_value)
		self.screen.blit(self.farm_res_btn3.image, self.farm_res_btn3.rect)
		self.screen.blit(self.farm_potato_img2, (540,507))
		self.screen.blit(self.farm_knife_img3,(560,350))
		self.screen.blit(self.farm_buy_btn3.image, self.farm_buy_btn3.rect)

		# background_square = ButtonNoText(730,290,220,240,self.farm_btn_img41)
		# self.screen.blit(background_square.image, background_square.rect)
		self.screen.blit(self.farm_label_stamina, self.farm_label_stamina_rect)
		self.screen.blit(self.farm_stamina_value, self.farm_stamina_rect_value)
		self.screen.blit(self.farm_res_btn4.image, self.farm_res_btn4.rect)
		self.screen.blit(self.farm_corn_img2, (762,507))
		self.screen.blit(self.farm_start_before_farm.image, self.farm_start_before_farm.rect)
		self.screen.blit(self.farm_buy_btn4.image, self.farm_buy_btn4.rect)
		self.curseur()

		pygame.display.update()

	def events_farm(self):
		# game loop events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.playing = False
				self.running = False
				exit()
			if event.type == pygame.MOUSEBUTTONUP and self.farm_buy_btn1.rect.collidepoint(pygame.mouse.get_pos()):
				if (self.player.potat_counter>=10):
					self.player.potat_counter-=10
					# add gun damage
					self.player.damaged_gun+=1
					self.shop_sound.play()
					if self.player.damaged_gun>=5:
						self.gun_level=2
			if event.type == pygame.MOUSEBUTTONUP and self.farm_buy_btn2.rect.collidepoint(pygame.mouse.get_pos()):
				if (self.player.corn_counter>=10):
					self.player.corn_counter-=10
					# add gun ammo
					self.player.gun_ammo+=1
					self.player.gun_max_ammo+=1
					self.shop_sound.play()
			if event.type == pygame.MOUSEBUTTONUP and self.farm_buy_btn3.rect.collidepoint(pygame.mouse.get_pos()):
				if (self.player.potat_counter>=10):
					self.player.potat_counter-=10
					# add knife damage
					self.player.damaged_knife+=1
					self.shop_sound.play()
			if event.type == pygame.MOUSEBUTTONUP and self.farm_buy_btn4.rect.collidepoint(pygame.mouse.get_pos()):
				if (self.player.corn_counter>=10):
					self.player.corn_counter-=10
					# add stamina
					self.player.max_stamina+=10
					self.shop_sound.play()
			if event.type == pygame.MOUSEBUTTONUP and self.farm_start_before_farm.rect.collidepoint(pygame.mouse.get_pos()):
				self.farm_time = False
				self.night_time = True
				pygame.mixer.fadeout(1000)
				pygame.mixer.music.load(self.sound_night)
				pygame.mixer.music.set_volume(0.05)
				pygame.mixer.music.play(fade_ms=2000)
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_ESCAPE:
					self.pause = True
					self.playing = False
					self.intro_screen()
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
				self.update_night()
				self.draw()
				self.events_night()

				if self.nb_crabs_left==0:
					self.after_win()
					pygame.mixer.music.load(self.sound_title)
				if self.player.player_health==0:
					self.after_game_over()

		pygame.display.update()

	def curseur(self):
		mouse_pos = pygame.mouse.get_pos()
		CURSOR = pygame.transform.scale(
			pygame.image.load(os.path.join('assets/img/tests', 'viewfinder.png')).convert_alpha(), (100, 100))
		CURSOR_RECT = CURSOR.get_rect()
		CURSOR_RECT.center = mouse_pos
		self.screen.blit(CURSOR, CURSOR_RECT)

	def intro_screen(self):
		click_sound.play()
		self.menu = True

		if self.music_played == True:
			pygame.mixer.music.load(self.sound_title)
			pygame.mixer.music.set_volume(0.05)
			pygame.mixer.music.play(fade_ms=2000)
			self.music_played = False

		title = self.font.render('Crab Island', True, BLACK)
		title_rect = title.get_rect(x=self.screen.get_width() / 2 - title.get_width() / 2, y=100)

		if (self.pause):
			Text_Button = "Resume"
		else:
			Text_Button = "Play"

		play_button = Button((self.screen.get_width() / 2) - 100, 250, 200, 50, BLACK, self.farm_btn_img11, Text_Button, 40)

		rules_button = Button((self.screen.get_width() / 2) - 100, 350, 200, 50, BLACK, self.farm_btn_img11, 'Game Rules', 40)
		option_button = Button((self.screen.get_width() / 2) - 100, 450, 200, 50, BLACK, self.farm_btn_img11, 'Options', 40)
		credits_button = Button((self.screen.get_width() / 2) - 100, 550, 200, 50, BLACK, self.farm_btn_img11, 'Credits', 40)
		exit_button = Button((self.screen.get_width() / 2) - 100, 650, 200, 50, BLACK, self.farm_btn_img11, 'Exit', 40)

		while self.menu:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.menu = False
					self.running = False
					exit()
			mouse_pos = pygame.mouse.get_pos()
			mouse_pressed = pygame.mouse.get_pressed()

			if play_button.rect.collidepoint(mouse_pos[0],mouse_pos[1]):
				play_button = Button((self.screen.get_width() / 2) - 100, 250, 200, 50, BLACK, self.btn_img22, Text_Button, 40)
			else:
				play_button = Button((self.screen.get_width() / 2) - 100, 250, 200, 50, BLACK, self.farm_btn_img21, Text_Button, 40)

			if rules_button.rect.collidepoint(mouse_pos[0],mouse_pos[1]):
				rules_button = Button((self.screen.get_width() / 2) - 100, 350, 200, 50, BLACK, self.btn_img42, 'Game Rules', 40)
			else:
				rules_button = Button((self.screen.get_width() / 2) - 100, 350, 200, 50, BLACK, self.farm_btn_img41, 'Game Rules', 40)

			if option_button.rect.collidepoint(mouse_pos[0],mouse_pos[1]):
				option_button = Button((self.screen.get_width() / 2) - 100, 450, 200, 50, BLACK, self.btn_img42, 'Options', 40)
			else:
				option_button = Button((self.screen.get_width() / 2) - 100, 450, 200, 50, BLACK, self.farm_btn_img41, 'Options', 40)

			if credits_button.rect.collidepoint(mouse_pos[0],mouse_pos[1]):
				credits_button = Button((self.screen.get_width() / 2) - 100, 550, 200, 50, BLACK, self.btn_img42, 'Credits', 40)
			else:
				credits_button = Button((self.screen.get_width() / 2) - 100, 550, 200, 50, BLACK, self.farm_btn_img41, 'Credits', 40)

			if exit_button.rect.collidepoint(mouse_pos[0],mouse_pos[1]):
				exit_button = Button((self.screen.get_width() / 2) - 100, 650, 200, 50, BLACK, self.farm_btn_img12, 'Exit', 40)
			else:
				exit_button = Button((self.screen.get_width() / 2) - 100, 650, 200, 50, BLACK, self.farm_btn_img11, 'Exit', 40)

			if play_button.is_pressed(mouse_pos, mouse_pressed):
				if (self.pause):
					self.menu = False
					self.pause = False
					self.playing = True
				else:
					self.menu = False
					self.playing = True
			if rules_button.is_pressed(mouse_pos, mouse_pressed):
					self.menu = False
					self.rules = True
			if option_button.is_pressed(mouse_pos, mouse_pressed):
					self.menu = False
					self.options = True
			if credits_button.is_pressed(mouse_pos, mouse_pressed):
					self.menu = False
					self.credits = True
			if exit_button.is_pressed(mouse_pos, mouse_pressed):
				exit()
			self.screen.blit(pygame.image.load('assets/img/tests/menu.png'),(0,0))
			# self.screen.blit(title, title_rect)
			self.screen.blit(play_button.image, play_button.rect)
			self.screen.blit(rules_button.image, rules_button.rect)
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
			music_on_off = Button(700, 240, 60, 30, BLACK, self.farm_btn_img31, 'On', 30)
		else:
			music_on_off = Button(700, 240, 60, 30, BLACK, self.farm_btn_img32, 'Off', 30)

		if self.fx_played == True:
			fx_on_off = Button(700, 270, 60, 30, BLACK, self.farm_btn_img31, 'On', 30)
		else:
			fx_on_off = Button(700, 270, 60, 30, BLACK, self.farm_btn_img32, 'Off', 30)

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
			top_btn1 = Button(700, 370, 60, 30, BLACK, self.farm_btn_img31, 'Z', 30)
			bottom_btn1 = Button(700, 400, 60, 30, BLACK, self.farm_btn_img31, 'S', 30)
			left_btn1 = Button(700, 430, 60, 30, BLACK, self.farm_btn_img31, 'Q', 30)
			right_btn1 = Button(700, 460, 60, 30, BLACK, self.farm_btn_img31, "D", 30)
			top_btn2 = Button(590, 370, 110, 30, BLACK, self.farm_btn_img32, 'Arr. Top', 30)
			bottom_btn2 = Button(590, 400, 110, 30, BLACK, self.farm_btn_img32, 'Arr. Bottom', 30)
			left_btn2 = Button(590, 430, 110, 30, BLACK, self.farm_btn_img32, 'Arr. Left', 30)
			right_btn2 = Button(590, 460, 110, 30, BLACK, self.farm_btn_img32, "Arr. Right", 30)
		else:
			top_btn1 = Button(700, 370, 60, 30, BLACK, self.farm_btn_img32, 'Z', 30)
			bottom_btn1 = Button(700, 400, 60, 30, BLACK, self.farm_btn_img32, 'S', 30)
			left_btn1 = Button(700, 430, 60, 30, BLACK, self.farm_btn_img32, 'Q', 30)
			right_btn1 = Button(700, 460, 60, 30, BLACK, self.farm_btn_img32, "D", 30)
			top_btn2 = Button(590, 370, 110, 30, BLACK, self.farm_btn_img31, 'Arr. Top', 30)
			bottom_btn2 = Button(590, 400, 110, 30, BLACK, self.farm_btn_img31, 'Arr. Bottom', 30)
			left_btn2 = Button(590, 430, 110, 30, BLACK, self.farm_btn_img31, 'Arr. Left', 30)
			right_btn2 = Button(590, 460, 110, 30, BLACK, self.farm_btn_img31, "Arr. Right", 30)

		if self.back_to_game:
			back_button = Button((self.screen.get_width() / 2) - 100, 650, 200, 50, BLACK, self.farm_btn_img11, 'Back to game', 30)
		else:
			back_button = Button((self.screen.get_width() / 2) - 100, 650, 200, 50, BLACK, self.farm_btn_img11, 'Back to menu', 30)

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
						self.shop_sound.set_volume(0.05)
						self.knife_sound.set_volume(0.05)
						self.gun_reload_1.set_volume(0.05)
						self.gun_reload_2.set_volume(0.05)
						self.victory.set_volume(0.0)
					else:
						self.bullet_sound.set_volume(0)
						self.switch_weapon_sound.set_volume(0)
						spawn_sound.set_volume(0)
						click_sound.set_volume(0)
						self.damaged_sound.set_volume(0)
						self.shop_sound.set_volume(0)
						self.knife_sound.set_volume(0)
						self.gun_reload_1.set_volume(0)
						self.gun_reload_2.set_volume(0)
						self.victory.set_volume(0)
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

			mouse_pos = pygame.mouse.get_pos()
			if back_button.rect.collidepoint(mouse_pos[0],mouse_pos[1]):
				if self.back_to_game:
					back_button = Button((self.screen.get_width() / 2) - 100, 650, 200, 50, BLACK, self.farm_btn_img12, 'Back to game', 30)
				else:
					back_button = Button((self.screen.get_width() / 2) - 100, 650, 200, 50, BLACK, self.farm_btn_img12, 'Back to menu', 30)
			else:
				if self.back_to_game:
					back_button = Button((self.screen.get_width() / 2) - 100, 650, 200, 50, BLACK, self.farm_btn_img11, 'Back to game', 30)
				else:
					back_button = Button((self.screen.get_width() / 2) - 100, 650, 200, 50, BLACK, self.farm_btn_img11, 'Back to menu', 30)

			self.screen.blit(pygame.image.load('assets/img/tests/menuForAll.png'),(0,0))
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

		font1 = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 50)
		font2 = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 30)

		line1 = font1.render('Graphics', True, BLACK)
		line1_rect = line1.get_rect(x=self.screen.get_width() / 3 - line1.get_width() / 2, y=200)

		line2 = font2.render('All the graphics of the game have been handmade by Altin Rrahmani.', True, BLACK)
		line2_rect = line2.get_rect(x=self.screen.get_width() / 3 - line1.get_width() / 2, y=250)

		line3 = font1.render('Development', True, BLACK)
		line3_rect = line3.get_rect(x=self.screen.get_width() / 3 - line1.get_width() / 2, y=300)

		line4 = font2.render('This game has been developed in python with the pygame library.', True, BLACK)
		line4_rect = line4.get_rect(x=self.screen.get_width() / 3 - line1.get_width() / 2, y=350)

		line5 = font2.render('Developers: Alexandre Arle, Remi Del Medico, Romain Miras.', True, BLACK)
		line5_rect = line5.get_rect(x=self.screen.get_width() / 3 - line1.get_width() / 2, y=380)

		line6 = font1.render('Sounds', True, BLACK)
		line6_rect = line6.get_rect(x=self.screen.get_width() / 3 - line1.get_width() / 2, y=420)

		line7 = font2.render('All game sounds are from www.rpgmakerweb.com.', True, BLACK)
		line7_rect = line7.get_rect(x=self.screen.get_width() / 3 - line1.get_width() / 2, y=470)

		line8 = font2.render('A game created by Pog Champs Team.', True, BLACK)
		line8_rect = line8.get_rect(x=self.screen.get_width() / 2 - line8.get_width() / 2, y=560)

		back_button = Button((self.screen.get_width() / 2) - 100, 650, 200, 50, BLACK, self.farm_btn_img11, 'Back to menu', 30)

		while self.credits:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.credits = False
					self.running = False
					exit()
				elif event.type == pygame.MOUSEBUTTONUP and back_button.rect.collidepoint(pygame.mouse.get_pos()):
					if self.back_to_game:
						self.credits = False
						self.playing = True
					else:
						self.credits = False
						self.menu = True
			mouse_pos = pygame.mouse.get_pos()
			if back_button.rect.collidepoint(mouse_pos[0],mouse_pos[1]):
				back_button = Button((self.screen.get_width() / 2) - 100, 650, 200, 50, BLACK, self.farm_btn_img12, 'Back to menu', 30)
			else:
				back_button = Button((self.screen.get_width() / 2) - 100, 650, 200, 50, BLACK, self.farm_btn_img11, 'Back to menu', 30)

			self.screen.blit(pygame.image.load('assets/img/tests/menuForAll.png'),(0,0))
			self.screen.blit(title, title_rect)
			self.screen.blit(line1, line1_rect)
			self.screen.blit(line2, line2_rect)
			self.screen.blit(line3, line3_rect)
			self.screen.blit(line4, line4_rect)
			self.screen.blit(line5, line5_rect)
			self.screen.blit(line6, line6_rect)
			self.screen.blit(line7, line7_rect)
			self.screen.blit(line8, line8_rect)
			self.screen.blit(back_button.image, back_button.rect)

			self.clock.tick(FPS)
			self.curseur()
			pygame.display.update()

	def rules_screen(self):
		click_sound.play()
		self.rules = True

		title = self.font.render('Game Rules', True, BLACK)
		title_rect = title.get_rect(x=self.screen.get_width() / 2 - title.get_width() / 2, y=100)

		font = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 30)
		rules_desc1 = font.render('The rules are simple!', True, BLACK)
		rules_desc1_rect = rules_desc1.get_rect(x=self.screen.get_width() / 2 - rules_desc1.get_width() / 2, y=200)

		rules_desc2 = font.render('You will play a character who, during the day, must', True, BLACK)
		rules_desc2_rect = rules_desc2.get_rect(x=self.screen.get_width() / 2 - rules_desc2.get_width() / 2, y=220)

		rules_desc3 = font.render('harvest potatoes and corn to buy ammunition at the market.', True, BLACK)
		rules_desc3_rect = rules_desc3.get_rect(x=self.screen.get_width() / 2 - rules_desc3.get_width() / 2, y=240)

		rules_desc4 = font.render('Once night falls, you have to survive the nasty little crabs...', True, BLACK)
		rules_desc4_rect = rules_desc4.get_rect(x=self.screen.get_width() / 2 - rules_desc4.get_width() / 2, y=260)

		font = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), 40)
		rules_desc5 = font.render('To move the character :', True, BLACK)
		rules_desc5_rect = rules_desc5.get_rect(x=230, y=350)

		btn1 = Button(620,340,180,40,BLACK,self.farm_btn_img21,"ZQSD or Arrows",30)

		rules_desc6 = font.render('To target crabs :', True, BLACK)
		rules_desc6_rect = rules_desc6.get_rect(x=230, y=400)

		btn2 = Button(620,390,80,40,BLACK,self.farm_btn_img21,"Mouse",30)

		rules_desc7 = font.render('To collect potatoes/corn :', True, BLACK)
		rules_desc7_rect = rules_desc7.get_rect(x=230, y=450)

		btn3 = Button(620,440,150,40,BLACK,self.farm_btn_img21,"Right click",30)

		rules_desc8 = font.render('To shoot :', True, BLACK)
		rules_desc8_rect = rules_desc8.get_rect(x=230, y=500)

		btn4 = Button(620,490,150,40,BLACK,self.farm_btn_img21,"Left click",30)

		rules_desc9 = font.render('To change weapons :', True, BLACK)
		rules_desc9_rect = rules_desc9.get_rect(x=230, y=550)

		btn5 = Button(620,540,150,40,BLACK,self.farm_btn_img21,"Mouse wheel",30)

		rules_desc10 = font.render('To reload the gun :', True, BLACK)
		rules_desc10_rect = rules_desc10.get_rect(x=230, y=600)

		btn6 = Button(620,590,40,40,BLACK,self.farm_btn_img21,"R",30)

		back_button = Button((self.screen.get_width() / 2) - 100, 670, 200, 50, BLACK, self.farm_btn_img11, 'Back to menu', 30)

		while self.rules:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.rules = False
					self.running = False
					exit()
				elif event.type == pygame.MOUSEBUTTONUP and back_button.rect.collidepoint(pygame.mouse.get_pos()):
					self.rules = False
					self.menu = True
			mouse_pos = pygame.mouse.get_pos()
			if back_button.rect.collidepoint(mouse_pos[0],mouse_pos[1]):
				back_button = Button((self.screen.get_width() / 2) - 100, 650, 200, 50, BLACK, self.farm_btn_img12, 'Back to menu', 30)
			else:
				back_button = Button((self.screen.get_width() / 2) - 100, 650, 200, 50, BLACK, self.farm_btn_img11, 'Back to menu', 30)

			self.screen.blit(pygame.image.load('assets/img/tests/menuForAll.png'),(0,0))
			self.screen.blit(title, title_rect)
			self.screen.blit(rules_desc1, rules_desc1_rect)
			self.screen.blit(rules_desc2, rules_desc2_rect)
			self.screen.blit(rules_desc3, rules_desc3_rect)
			self.screen.blit(rules_desc4, rules_desc4_rect)
			self.screen.blit(rules_desc5, rules_desc5_rect)
			self.screen.blit(rules_desc6, rules_desc6_rect)
			self.screen.blit(rules_desc7, rules_desc7_rect)
			self.screen.blit(rules_desc8, rules_desc8_rect)
			self.screen.blit(rules_desc9, rules_desc9_rect)
			self.screen.blit(rules_desc10, rules_desc10_rect)
			self.screen.blit(btn1.image, btn1.rect)
			self.screen.blit(btn2.image, btn2.rect)
			self.screen.blit(btn3.image, btn3.rect)
			self.screen.blit(btn4.image, btn4.rect)
			self.screen.blit(btn5.image, btn5.rect)
			self.screen.blit(btn6.image, btn6.rect)
			self.screen.blit(back_button.image, back_button.rect)

			self.clock.tick(FPS)
			self.curseur()
			pygame.display.update()

	def animationLoading(self, animationTotalTime, animationTime, color):
		pygame.draw.rect(self.screen, BLACK, pygame.Rect(self.player.rect.centerx - 34, self.player.rect.centery - 50, 74, 20), 2)
		pygame.draw.rect(self.screen, color, pygame.Rect(self.player.rect.centerx - 32, self.player.rect.centery - 48, ((animationTime * 74 ) // animationTotalTime ) - 4, 16))

		animationTime += 1
		return animationTime


g = Game()
while g.running == True:

	if g.menu == True:
		g.intro_screen()
	if g.rules == True:
		g.rules_screen()
	elif g.options == True:
		g.options_screen()
	elif g.credits == True:
		g.credits_screen()
	elif g.playing == True:
		g.new()
		g.main()

pygame.quit()
sys.exit()
