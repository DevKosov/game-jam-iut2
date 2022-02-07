import pygame
import spritesheet

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()

		try:
			self.sheet = pygame.image.load('assets/img/tests/character_test.png').convert()
		except pygame.error as e:
			print(f"Unable to load spritesheet image: player spritesheet ")
			raise SystemExit(e)

		# self.player_walk = [player_image,player_image]

		self.player_index = 0

		self.image = self.sheet #self.player_walk[self.player_index]
		self.rect = self.image.get_rect(midbottom = (80,300))
		self.gravity = 0

		self.jump_sound = pygame.mixer.Sound('assets/audio/se/Attack1.ogg')
		self.jump_sound.set_volume(0.5)

	def player_input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			self.jump_sound.play()

	def animation_state(self):
		if self.rect.bottom < 300:
			self.image = self.player_jump
		else:
			self.player_index += 0.1
			if self.player_index >= len(self.player_walk):self.player_index = 0
			self.image = self.player_walk[int(self.player_index)]

	def update(self):
		self.player_input()
		self.animation_state()
