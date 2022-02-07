import pygame, os
import spritesheet

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()

		try:
			self.sheet_image = pygame.image.load(os.path.join('assets/img/characters/', 'doux.png')).convert_alpha()
		except pygame.error as e:
			print(f"Unable to load spritesheet image: player spritesheet ")
			raise SystemExit(e)

		self.sheet = spritesheet.SpriteSheet(self.sheet_image)

		# self.player_walk = [player_image,player_image]

		BLACK = (0, 0, 0)

		self.frame_0 =  self.sheet.get_image(0, 24, 24, 3, BLACK)
		self.frame_1 =  self.sheet.get_image(1, 24, 24, 3, BLACK)
		self.frame_2 =  self.sheet.get_image(2, 24, 24, 3, BLACK)
		self.frame_3 =  self.sheet.get_image(3, 24, 24, 3, BLACK)
		self.frame_4 = self.sheet.get_image(4, 24, 24, 3, BLACK)
		self.frame_5 = self.sheet.get_image(5, 24, 24, 3, BLACK)
		self.frame_6 = self.sheet.get_image(6, 24, 24, 3, BLACK)
		self.frame_7 = self.sheet.get_image(7, 24, 24, 3, BLACK)

		self.index = 0;

		self.image = self.frame_0

		self.rect = self.image.get_rect(midbottom = (80,300))
		self.gravity = 0

		self.jump_sound = pygame.mixer.Sound('assets/audio/se/Bell3.ogg')
		self.jump_sound.set_volume(0.5)

	def player_input(self, event):
		keys = event.key
		if keys == pygame.K_SPACE:
			self.jump_sound.play()
			self.index += 1
			if self.index == 7:
				self.index = 0


		

	def animation_state(self):
		if self.index == 0:
			self.image = self.frame_0
		if self.index == 1:
			self.image = self.frame_1
		if self.index == 2:
			self.image = self.frame_2
		if self.index == 3:
			self.image = self.frame_3
		if self.index == 4:
			self.image = self.frame_4
		if self.index == 5:
			self.image = self.frame_5
		if self.index == 6:
			self.image = self.frame_6
		if self.index == 7:
			self.image = self.frame_7


	def update(self, event):
		self.player_input(event)
		self.animation_state()
		self.move()

	def move():
		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[pygame.K_LEFT]:
				self.rect.left = self.rect.left - 5
			if keys_pressed[pygame.K_RIGHT]:
				self.rect.left = self.rect.left + 5
			if keys_pressed[pygame.K_UP]:
				self.rect.top = self.rect.top - 5
			if keys_pressed[pygame.K_DOWN]:
				self.rect.top = self.rect.top + 5