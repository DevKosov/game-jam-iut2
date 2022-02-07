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
		self.image = self.sheet.get_image(0, 24, 24, 3, BLACK)
		# frame_1 = sprite_sheet.get_image(1, 24, 24, 3, BLACK)
		# frame_2 = sprite_sheet.get_image(2, 24, 24, 3, BLACK)
		# frame_3 = sprite_sheet.get_image(3, 24, 24, 3, BLACK)

		self.rect = self.image.get_rect(midbottom = (80,300))
		self.gravity = 0

		self.jump_sound = pygame.mixer.Sound('assets/audio/se/Bell3.ogg')
		self.jump_sound.set_volume(0.5)

	def player_input(self, event):
		keys = event.key
		if keys == pygame.K_SPACE:
			self.jump_sound.play()
		

	def animation_state(self):
		if self.rect.bottom < 300:
			self.image = self.player_jump
		# else:
		# 	self.player_index += 0.1
		# 	if self.player_index >= len(self.player_walk):self.player_index = 0
		# 	self.image = self.player_walk[int(self.player_index)]

	def update(self, event):
		self.player_input(event)
		self.animation_state()

	def move(self, y, deplacement):
		if y:
			self.rect.left = self.rect.left + deplacement
