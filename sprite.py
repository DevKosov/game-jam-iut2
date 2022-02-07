import pygame, os
import spritesheet



all_sprites = pygame.sprite.LayeredUpdates()
players = pygame.sprite.Group()






class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()

		try:
			self.sheet_image = pygame.image.load('assets/img/characters/doux.png').convert_alpha()
		except pygame.error as e:
			print(f"Unable to load spritesheet image: player spritesheet ")
			raise SystemExit(e)

		self.sheet = spritesheet.SpriteSheet(self.sheet_image)

		# self.player_walk = [player_image,player_image]

		BLACK = (0, 0, 0)

		self.frame_0 =  self.sheet.get_image(1, 1, 24, 24, 3, BLACK)
		self.frame_1 =  self.sheet.get_image(2,1, 24, 24, 3,BLACK)
		self.frame_2 =  self.sheet.get_image(3,1, 24, 24, 3,BLACK)
		self.frame_3 =  self.sheet.get_image(4,1, 24, 24, 3,BLACK)
		self.frame_4 = self.sheet.get_image(5,1, 24, 24, 3,BLACK)
		self.frame_5 = self.sheet.get_image(6,1, 24, 24, 3,BLACK)
		self.frame_6 = self.sheet.get_image(7,1, 24, 24, 3,BLACK)
		self.frame_7 = self.sheet.get_image(8,1, 24, 24, 3,BLACK)

		self.rotation = 1 # 1 regarde à droite // 2 regarde à gauche

		self.index = 0

		self.image = self.frame_0

		self.rect = self.image.get_rect(midbottom = (80,300))
		self.gravity = 0

		self.test_sound = pygame.mixer.Sound('assets/audio/se/Bell3.ogg')
		self.test_sound.set_volume(0.5)

		self.bullet_sound = pygame.mixer.Sound('assets/audio/se/Gun1.ogg')
		self.bullet_sound.set_volume(0.1)


	def player_input(self, event):
		if event.type == pygame.KEYUP:
			self.index = 0
		if event.type == pygame.KEYDOWN:
			keys = event.key
			if keys == pygame.K_SPACE:
				self.test_sound.play()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == pygame.BUTTON_LEFT:
				self.bullet_sound.play()






	def animation_state(self):
		if self.index == 0:
			self.image = self.frame_0
			self.flipper()
		if self.index >= 1:
			self.image = self.frame_1
			self.flipper()
		if self.index >= 2:
			self.image = self.frame_2
			self.flipper()
		if self.index >= 3:
			self.image = self.frame_3
			self.flipper()
		if self.index >= 4:
			self.image = self.frame_4
			self.flipper()
		if self.index >= 5:
			self.image = self.frame_5
			self.flipper()
		if self.index >= 6:
			self.image = self.frame_6
			self.flipper()
		if self.index >= 7:
			self.image = self.frame_7
			self.flipper()


	def update(self):
		self.animation_state()
		self.move()
		self.image.set_colorkey((0,0,0))

	def move(self):
		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_q]:
			self.rect.left = self.rect.left - 5
			self.index += 0.2
			if self.index >= 7:
				self.index = 0
			if self.rotation == 1:
				self.rotation = 2
		if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
			self.rect.left = self.rect.left + 5
			self.index += 0.2
			if self.index >= 7:
				self.index = 0
			if self.rotation == 2:
				self.rotation = 1
		if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_z]:
			self.rect.top = self.rect.top - 5
			self.index += 0.2
			if self.index >= 7:
				self.index = 0
		if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
			self.rect.top = self.rect.top + 5
			self.index += 0.2
			if self.index >= 7:
				self.index = 0


	def flipper(self):
		if self.rotation != 1:
				self.image = pygame.transform.flip(self.image, 1, 0)