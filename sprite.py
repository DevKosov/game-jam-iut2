# from tkinter import Y
from turtle import width
import pygame, os, math
#import spritesheet


class SpriteSheet():
	def __init__(self, image):
		self.sheet = image	

	def get_image(self, frame, line, width, height, scale, colour):
		image = pygame.Surface((width, height)).convert_alpha()
		image.blit(self.sheet, (0, 0), (((frame-1) * width), (line-1)*height, width, height))
		image = pygame.transform.scale(image, (width * scale, height * scale))
		image.set_colorkey(colour)

		return image

class Player(pygame.sprite.Sprite):
	def __init__(self, game, x, y):
		BLACK = (0,0,0)
		WIDTH = 24
		HEIGHT = 24


		self.game = game
		self._layer = 2
		self.groups = self.game.all_sprites
		pygame.sprite.Sprite.__init__(self, self.groups)

		self.x = x
		self.y = y
		self.width = WIDTH
		self.height = HEIGHT

		self.x_change = 0
		self.y_change = 0

		self.facing = 'right'
		self.animation_loop = 1
		
		self.image = self.game.character_spritesheet.get_image(1, 1, self.width, self.height, 3, BLACK)

		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y

	def update(self):
		self.movement()
		self.animate()

		self.rect.x += self.x_change
		self.rect.y += self.y_change

		self.x_change = 0
		self.y_change  = 0

	def movement(self):
		PLAYER_SPEED = 5
		
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			self.x_change -= PLAYER_SPEED
			self.facing = 'left'
		if keys[pygame.K_RIGHT]:
			self.x_change += PLAYER_SPEED
			self.facing = 'right'
		if keys[pygame.K_UP]:
			self.y_change -= PLAYER_SPEED
			self.facing = 'up'
		if keys[pygame.K_DOWN]:
			self.y_change += PLAYER_SPEED
			self.facing = 'down'

	def animate(self):
		BLACK = (0, 0, 0)
		SCALE = 3

		image = pygame.transform.flip(self.game.character_spritesheet.get_image(1, 1, self.width, self.height, SCALE, BLACK), 1, 0)
		image.set_colorkey(BLACK)
		image1 = pygame.transform.flip(self.game.character_spritesheet.get_image(2, 1, self.width, self.height, SCALE, BLACK), 1, 0)
		image1.set_colorkey(BLACK)
		image2 = pygame.transform.flip(self.game.character_spritesheet.get_image(3, 1, self.width, self.height, SCALE, BLACK), 1, 0)
		image2.set_colorkey(BLACK)
		left_animations = [image,
                        	image1,
                        	image2]

		right_animations = [self.game.character_spritesheet.get_image(1, 1, self.width, self.height, SCALE, BLACK),
                           self.game.character_spritesheet.get_image(2, 1, self.width, self.height, SCALE, BLACK),
                           self.game.character_spritesheet.get_image(3, 1, self.width, self.height, SCALE, BLACK)]

		if self.facing == 'left':
			if self.x_change == 0:
				pygame.transform.flip(self.game.character_spritesheet.get_image(1, 1, self.width, self.height, 1, BLACK), 1, 0)
			else :
				self.image = left_animations[math.floor(self.animation_loop)]
				self.animation_loop += 0.1
				if self.animation_loop >= 3:
					self.animation_loop = 0

		if self.facing == 'right':
			if self.x_change == 0:
				self.game.character_spritesheet.get_image(1, 1, self.width, self.height, SCALE, BLACK)
			else :
				self.image = right_animations[math.floor(self.animation_loop)]
				self.animation_loop += 0.1
				if self.animation_loop >= 3:
					self.animation_loop = 0

		if self.facing == 'up':
			if self.y_change == 0:
				self.game.character_spritesheet.get_image(1, 1, self.width, self.height, SCALE, BLACK)
			else :
				self.image = right_animations[math.floor(self.animation_loop)]
				self.animation_loop += 0.1
				if self.animation_loop >= 3:
					self.animation_loop = 0

		if self.facing == 'down':
			if self.y_change == 0:
				pygame.transform.flip(self.game.character_spritesheet.get_image(1, 1, self.width, self.height, 1, BLACK), 1, 0)
			else :
				self.image = left_animations[math.floor(self.animation_loop)]
				self.animation_loop += 0.1
				if self.animation_loop >= 3:
					self.animation_loop = 0
 
class Block(pygame.sprite.Sprite):
	def __init__(self, game, x, y,block_type):
		BLACK = (0,0,0)
		WIDTH = 32
		HEIGHT = 32
		SCALE = 1
		self.game = game
		self._layer = 1
		self.groups = self.game.all_sprites, self.game.blocks
		pygame.sprite.Sprite.__init__(self, self.groups)
		self.x = x
		self.y = y
		self.width = 64
		self.height = 64

		self.block_type = block_type

		if self.block_type == 'sand':
			self.image = self.game.terrain_spritesheet.get_image(1, 3, WIDTH, HEIGHT, SCALE, BLACK)
		if self.block_type == 'water':
			self.image = self.game.terrain_spritesheet.get_image(3, 3, WIDTH, HEIGHT, SCALE, BLACK)
		if self.block_type == 'topWater':
			self.image = self.game.terrain_spritesheet.get_image(4, 1, WIDTH, HEIGHT, SCALE, BLACK)
		if self.block_type == 'topLeftWaterBord':
			self.image = self.game.terrain_spritesheet.get_image(6, 1, WIDTH, HEIGHT, SCALE, BLACK)
		if self.block_type == 'topRightWaterBord':
			self.image = self.game.terrain_spritesheet.get_image(5, 1, WIDTH, HEIGHT, SCALE, BLACK)
		if self.block_type == 'bottomWaterBord':
			self.image = self.game.terrain_spritesheet.get_image(2, 1, WIDTH, HEIGHT, SCALE, BLACK)
		if self.block_type == 'bottomLeftSand':
			self.image = self.game.terrain_spritesheet.get_image(7, 1, WIDTH, HEIGHT, SCALE, BLACK)
		if self.block_type == 'bottomRightSand':
			self.image = self.game.terrain_spritesheet.get_image(8, 1, WIDTH, HEIGHT, SCALE, BLACK)
		if self.block_type == 'rightWaterBord':
			self.image = self.game.terrain_spritesheet.get_image(3, 1, WIDTH, HEIGHT, SCALE, BLACK)
		if self.block_type == 'leftWaterBord':
			self.image = self.game.terrain_spritesheet.get_image(1, 1, WIDTH, HEIGHT, SCALE, BLACK)

		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y


class Button:
	def __init__(self, x, y, width, height, fg, bg, content, fontsize):
		self.font = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), fontsize)
		self.content = content

		self.x = x
		self.y = y
		self.width = width
		self.height = height

		self.bg = bg
		self.fg = fg

		self.image = pygame.Surface((self.width, self.height))
		self.image.fill(self.bg)
		self.rect = self.image.get_rect()

		self.rect.x = self.x
		self.rect.y = self.y

		self.text = self.font.render(self.content, True, self.fg)
		self.text_rect = self.text.get_rect(center=(self.width//2, self.height//2))
		self.image.blit(self.text, self.text_rect)

	def is_pressed(self, pos, pressed):
		if self.rect.collidepoint(pos):
			if pressed[0]:
				return True
			return False
		return False

class Crab:
	def __init__(self,game, x, y, hp):
		BLACK = (0,0,0)
		WIDTH = 100
		HEIGHT = 79

		self._layer = 2
		self.game = game

		self.groups = self.game.all_sprites, self.game.enemies
		pygame.sprite.Sprite.__init__(self.game.enemies)

		self.x = x
		self.y = y
		self.width = WIDTH
		self.height = HEIGHT
		self.hp = hp



		self.image = self.game.character_spritesheet.get_image(1, 1, self.width, self.height, 3, BLACK)

		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y


# 		try:
# 			self.sheet_image = pygame.image.load('assets/img/characters/doux.png').convert_alpha()
# 		except pygame.error as e:
# 			print(f"Unable to load spritesheet image: player spritesheet ")
# 			raise SystemExit(e)

# 		self.sheet = spritesheet.SpriteSheet(self.sheet_image)

# 		# self.player_walk = [player_image,player_image]

# 		self.frame_7 = self.sheet.get_image(8,1, WIDTH, LENGH, SCALE,BLACK)

# 		self.rotation = 1 # 1 regarde à droite // 2 regarde à gauche

# 		self.index = 0

# 		self.image = self.frame_0

# 		self.rect = self.image.get_rect(midbottom = (80,300))
# 		self.gravity = 0

# 	def player_input(self, event):
# 		if event.type == pygame.KEYUP:
# 			self.index = 0
# 		if event.type == pygame.KEYDOWN:
# 			keys = event.key
# 			if keys == pygame.K_SPACE:
# 				self.test_sound.play()
# 		if event.type == pygame.MOUSEBUTTONDOWN:
# 			if event.button == pygame.BUTTON_LEFT:
# 				self.bullet_sound.play()






# 	def animation_state(self):
# 		if self.index == 0:
# 			self.image = self.frame_0
# 			self.flipper()
# 		if self.index >= 1:
# 			self.image = self.frame_1
# 			self.flipper()
# 		if self.index >= 2:
# 			self.image = self.frame_2
# 			self.flipper()
# 		if self.index >= 3:
# 			self.image = self.frame_3
# 			self.flipper()
# 		if self.index >= 4:
# 			self.image = self.frame_4
# 			self.flipper()
# 		if self.index >= 5:
# 			self.image = self.frame_5
# 			self.flipper()
# 		if self.index >= 6:
# 			self.image = self.frame_6
# 			self.flipper()
# 		if self.index >= 7:
# 			self.image = self.frame_7
# 			self.flipper()


# 	def update(self):
# 		self.animation_state()
# 		self.move()
# 		self.image.set_colorkey((0,0,0))

# 	def move(self):
# 		SPEED_ANIMATION = 0.2
# 		MAX_INDEX = 8
# 		DEPLACEMENT = 5

# 		keys_pressed = pygame.key.get_pressed()
# 		if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_q]:
# 			self.rect.left = self.rect.left - DEPLACEMENT
# 			self.index += SPEED_ANIMATION
# 			if self.index >= MAX_INDEX:
# 				self.index = 0
# 			if self.rotation == 1:
# 				self.rotation = 2
# 		if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
# 			self.rect.left = self.rect.left + DEPLACEMENT
# 			self.index += SPEED_ANIMATION
# 			if self.index >= MAX_INDEX:
# 				self.index = 0
# 			if self.rotation == 2:
# 				self.rotation = 1
# 		if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_z]:
# 			self.rect.top = self.rect.top - DEPLACEMENT
# 			self.index += SPEED_ANIMATION
# 			if self.index >= MAX_INDEX:
# 				self.index = 0
# 		if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
# 			self.rect.top = self.rect.top + DEPLACEMENT
# 			self.index += SPEED_ANIMATION
# 			if self.index >= MAX_INDEX:
# 				self.index = 0


# 	def flipper(self):
# 		if self.rotation != 1:
# 				self.image = pygame.transform.flip(self.image, 1, 0)
