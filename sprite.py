# from tkinter import Y
from turtle import update, width
import pygame, os, math
import random
from config import *
#import spritesheet
import sprite
import time

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
	def __init__(self, game, x, y, gameplay):

		#HIhihiha

		self.game = game
		self._layer = PLAYER_LAYER
		self.groups = self.game.all_sprites
		pygame.sprite.Sprite.__init__(self, self.groups)

		self.x = x
		self.y = y
		self.width = PLAYER_SPRITE_WIDTH
		self.height = PLAYER_SPRITE_HEIGHT
		self.hp = PLAYER_HP
		self.recharge = False
		self.recolting = False

		self.takingDamage = 0


		self.x_change = 0
		self.y_change = 0

		self.facing = 'right'
		self.animation_loop = 1

		self.image = self.game.character_spritesheet.get_image(1, 1, self.width, self.height, 3, BLACK)

		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y

		self.player_gameplay_ZQSD = gameplay

		# Gestion Invulnératibilité
		self.player_invulnerability = False
		self.player_time_left = 0
		self.player_time_invulnerability = 3 * 60 # nb secondes * 60 ( Je crois )

		#Player Game Night State
		self.current_weapon = "gun"
		self.player_speed = PLAYER_SPEED
		self.potat_counter = 0
		self.corn_counter = 0
		self.damaged_knife = 0
		self.damaged_gun = 0
		self.player_health = 3

		#Gestion Gun
		self.gun_ammo = 5
		self.gun_max_ammo = 5
		self.in_realoding = False
		self.gun_time_animation = 0
		self.animation_gun_duration = 180

		#Gestion du Knife
		self.in_cutting = False

		#sprint
		self.in_running = False
		self.max_stamina = 100
		self.current_stamina = self.max_stamina
		self.basic_speed = self.player_speed
		self.speed_upgrade_with_sprint = 3

		self.takingDamage = False
		self.nbTickDamage = 0

	def update(self):
		
		self.movement()
		self.animate()

		self.rect.x += self.x_change
		self.game.xTopLefIsland -= self.x_change
		self.collision('x')
		self.rect.y += self.y_change
		self.game.yTopLefIsland -= self.y_change
		self.collision('y')

		self.x_change = 0
		self.y_change  = 0

		if not(self.takingDamage):
			if not self.player_invulnerability:
				for enemies in self.game.enemies:
					if pygame.sprite.collide_mask(self, enemies):
						self.damageDealerEnemy = enemies
						self.takingDamage = True
						self.player_health -= 1
						# Invulnératibilité pour (player_time_invulnerability) de temps
						self.game.damaged_sound.play()
						self.player_invulnerability = True
						break
			else:
				if (self.player_time_left >= self.player_time_invulnerability):
					self.player_time_left = 0
					self.player_invulnerability = False
				else:
					self.player_time_left += 1
		else:
			if self.nbTickDamage <= KNOCKBACK:
				self.damaged(self.damageDealerEnemy)
				self.nbTickDamage += 1
			else:
				self.nbTickDamage = 0
				self.takingDamage = False
		self.stamina()
		

	def movement(self):

		if self.player_gameplay_ZQSD==False:
			keys = pygame.key.get_pressed()
			if keys[pygame.K_LEFT]:
				for sprite in self.game.all_sprites:
					sprite.rect.x += self.player_speed
				self.x_change -= self.player_speed
				self.facing = 'left'
			if keys[pygame.K_RIGHT]:
				for sprite in self.game.all_sprites:
					sprite.rect.x -= self.player_speed
				self.x_change += self.player_speed
				self.facing = 'right'
			if keys[pygame.K_UP]:
				for sprite in self.game.all_sprites:
					sprite.rect.y += self.player_speed
				self.y_change -= self.player_speed
				self.facing = 'up'
			if keys[pygame.K_DOWN]:
				for sprite in self.game.all_sprites:
					sprite.rect.y -= self.player_speed
				self.y_change += self.player_speed
				self.facing = 'down'
		else:
			keys = pygame.key.get_pressed()
			if keys[pygame.K_q]:
				for sprite in self.game.all_sprites:
					sprite.rect.x += self.player_speed
				self.x_change -= self.player_speed
				self.facing = 'left'
			if keys[pygame.K_d]:
				for sprite in self.game.all_sprites:
					sprite.rect.x -= self.player_speed
				self.x_change += self.player_speed
				self.facing = 'right'
			if keys[pygame.K_z]:
				for sprite in self.game.all_sprites:
					sprite.rect.y += self.player_speed
				self.y_change -= self.player_speed
				self.facing = 'up'
			if keys[pygame.K_s]:
				for sprite in self.game.all_sprites:
					sprite.rect.y -= self.player_speed
				self.y_change += self.player_speed
				self.facing = 'down'

	def damaged(self, enemies):
		#Calcul de déplacement
		diff_x = self.rect.x - enemies.rect.x
		diff_y = self.rect.y - enemies.rect.y

		# Push le joueur out
		if abs(diff_x) > abs(diff_y):
			if diff_x < 0:
				self.rect.x -= PUSHBACK_POWER
				for sprite in self.game.all_sprites:
					sprite.rect.x += PUSHBACK_POWER
				self.game.xTopLefIsland += PUSHBACK_POWER

				hit = pygame.sprite.spritecollide(self, self.game.blocks_collid, False)
				if hit:
					self.rect.x += PUSHBACK_POWER
					for sprite in self.game.all_sprites:
						sprite.rect.x -= PUSHBACK_POWER
					self.game.xTopLefIsland -= PUSHBACK_POWER
					
			else:
				self.rect.x -= -PUSHBACK_POWER
				for sprite in self.game.all_sprites:
					sprite.rect.x += -PUSHBACK_POWER
				self.game.xTopLefIsland -= PUSHBACK_POWER
				hit = pygame.sprite.spritecollide(self, self.game.blocks_collid, False)
				if hit:
					self.rect.x -= PUSHBACK_POWER
					for sprite in self.game.all_sprites:
						sprite.rect.x += PUSHBACK_POWER
					self.game.xTopLefIsland += PUSHBACK_POWER
					
				
		else:
			if diff_y < 0:
				self.rect.y -= PUSHBACK_POWER
				for sprite in self.game.all_sprites:
					sprite.rect.y += PUSHBACK_POWER
				self.game.yTopLefIsland += PUSHBACK_POWER
				hit = pygame.sprite.spritecollide(self, self.game.blocks_collid, False)
				if hit:
					self.rect.y += PUSHBACK_POWER
					for sprite in self.game.all_sprites:
						sprite.rect.y -= PUSHBACK_POWER
					self.game.yTopLefIsland -= PUSHBACK_POWER
					
			else:
				self.rect.y -= -PUSHBACK_POWER
				for sprite in self.game.all_sprites:
					sprite.rect.y += -PUSHBACK_POWER
				self.game.yTopLefIsland -= PUSHBACK_POWER
				hit = pygame.sprite.spritecollide(self, self.game.blocks_collid, False)
				if hit:
					self.rect.y -= PUSHBACK_POWER
					for sprite in self.game.all_sprites:
						sprite.rect.y += PUSHBACK_POWER
					self.game.yTopLefIsland += PUSHBACK_POWER
					
				

		#Gestion des overlay de vie
		
		

	def animate(self):
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

	def switch_weapon(self,event):
		if event.button == 4 and self.current_weapon == "gun":
			self.game.switch_weapon_sound.play()
			self.current_weapon = "knife"
		if event.button == 5 and self.current_weapon == "knife":
			self.game.switch_weapon_sound.play()
			self.current_weapon = "gun"

	def attacks(self):
		if (self.current_weapon == "gun"):
			if (self.gun_ammo != 0):
				self.game.FireBullet = True
				self.game.bullet_sound.play()
				x, y = pygame.mouse.get_pos()
				Bullet(self.game, self.rect.centerx, self.rect.centery, x, y, 5)
				self.gun_ammo -= 1
		else:
			if (not self.in_cutting):
				self.in_cutting = True
				self.game.knife_sound.play()
				KnifeCute(self.game)

	def sprint(self,event):
		if event.type == pygame.KEYUP :
			self.player_speed = self.basic_speed
			self.in_running = False
		if event.type == pygame.KEYDOWN and self.current_stamina != 0:
			self.player_speed = self.basic_speed + self.speed_upgrade_with_sprint
			self.in_running = True

	def stamina(self):
		if self.in_running:
			if not self.current_stamina <= 0:
				self.current_stamina -= 1
			else:
				self.current_stamina = 0
				self.player_speed = self.basic_speed
		else:
			if self.current_stamina < self.max_stamina:
				self.current_stamina += 0.5

	def reloading(self):
		if (self.in_realoding):
			if (self.gun_time_animation > self.animation_gun_duration):
				self.in_realoding = False
				self.gun_time_animation = 0
				self.game.gun_reload_2.play()
				self.gun_ammo = self.gun_max_ammo
			else:
				pygame.draw.rect(self.game.screen, BLACK, pygame.Rect(self.game.player.rect.centerx - 34, self.game.player.rect.centery - 50, 74, 20), 2)
				pygame.draw.rect(self.game.screen, WHITE, pygame.Rect(self.game.player.rect.centerx - 32, self.game.player.rect.centery - 48, ((self.gun_time_animation * 74 ) // self.animation_gun_duration ) - 4, 16))
				self.gun_time_animation += 1 #self.game.animationLoading(self.animation_gun_duration,self.gun_time_animation,WHITE)


	def collision(self, direction):
		if direction == 'x':
			hit = pygame.sprite.spritecollide(self, self.game.blocks_collid, False)
			if hit:
				if self.x_change > 0:
					self.rect.x = hit[0].rect.left - self.rect.width
					for sprite in self.game.all_sprites:
						sprite.rect.x += self.player_speed
					self.game.xTopLefIsland += self.player_speed
				if self.x_change < 0:
					self.rect.x = hit[0].rect.right
					for sprite in self.game.all_sprites:
						sprite.rect.x -= self.player_speed
					self.game.xTopLefIsland -= self.player_speed
		if direction == 'y':
			hit = pygame.sprite.spritecollide(self, self.game.blocks_collid, False)
			if hit:
				if self.y_change > 0:
					self.rect.y = hit[0].rect.top - self.rect.height
					for sprite in self.game.all_sprites:
						sprite.rect.y += self.player_speed
					self.game.yTopLefIsland += self.player_speed
				if self.y_change < 0:
					self.rect.y = hit[0].rect.bottom
					for sprite in self.game.all_sprites:
						sprite.rect.y -= self.player_speed
					self.game.yTopLefIsland -= self.player_speed

class Block(pygame.sprite.Sprite):
	def __init__(self, game, x, y, block_type, colision, farm, i, j):
		self.scale = TILEMAP_SCALE

		self.colision = colision
		self.game = game
		self._layer = BLOCK_LAYER
		self.i = i
		self.j = j

		if not(farm):
			
			if colision:
				self.groups = self.game.all_sprites, self.game.blocks_collid
				pygame.sprite.Sprite.__init__(self, self.groups)
			else:
				self.groups = self.game.all_sprites, self.game.blocks_no_collid_not_farm
				pygame.sprite.Sprite.__init__(self, self.groups)
			self.x = x
			self.y = y
			self.width = TILE_WIDTH
			self.height = TILE_HEIGHT

			self.block_type = block_type
			self.growStage = 0

		else:
			self.groups = self.game.all_sprites, self.game.blocks_no_collid_farm
			pygame.sprite.Sprite.__init__(self, self.groups)
			self.x = x
			self.y = y
			self.width = TILE_WIDTH
			self.height = TILE_HEIGHT

			self.block_type = block_type
			if self.block_type == 'firstStagePotato':
				self.growStage = 1
				self.time = 0
				self.timeToGrow = random.randint(GROW_MINTIME_STAGE1,GROW_MAXTIME_STAGE1)
			if self.block_type == 'firstStageCorn':
				self.growStage = 1
				self.time = 0
				self.timeToGrow = random.randint(GROW_MINTIME_STAGE1,GROW_MAXTIME_STAGE1)

	# basic textures
		if self.block_type == 'sand':
			self.image = self.game.terrain_spritesheet.get_image(2, 3, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'grass':
			self.image = self.game.terrain_spritesheet.get_image(1, 3, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'water':
			self.image = self.game.terrain_spritesheet.get_image(3, 3, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'dirt':
			self.image = self.game.terrain_spritesheet.get_image(4, 3, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'growingPotato':
			self.image = self.game.terrain_spritesheet.get_image(5, 3, self.width, self.height, self.scale, BLACK)
		#map border textures
		if self.block_type == 'topWater':
			self.image = self.game.terrain_spritesheet.get_image(2, 2, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'topLeftWaterBord':
			self.image = self.game.terrain_spritesheet.get_image(7, 2, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'topRightWaterBord':
			self.image = self.game.terrain_spritesheet.get_image(6, 2, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'bottomWaterBord':
			self.image = self.game.terrain_spritesheet.get_image(4, 2, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'bottomLeftSand':
			self.image = self.game.terrain_spritesheet.get_image(8, 2, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'bottomRightSand':
			self.image = self.game.terrain_spritesheet.get_image(5, 2, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'rightWaterBord':
			self.image = self.game.terrain_spritesheet.get_image(1, 2, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'leftWaterBord':
			self.image = self.game.terrain_spritesheet.get_image(3, 2, self.width, self.height, self.scale, BLACK)

		#Sand + Grass Transition
		if self.block_type == 'topLeftSandGrassT':
			self.image = self.game.terrain_spritesheet.get_image(6, 1, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'topRightSandGrassT':
			self.image = self.game.terrain_spritesheet.get_image(5, 1, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'topSandGrassT':
			self.image = self.game.terrain_spritesheet.get_image(4, 1, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'leftSandGrassT':
			self.image = self.game.terrain_spritesheet.get_image(1, 1, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'rightSandGrassT':
			self.image = self.game.terrain_spritesheet.get_image(3, 1, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'bottomRightSandGrassT':
			self.image = self.game.terrain_spritesheet.get_image(8, 1, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'bottomleftSandGrassT':
			self.image = self.game.terrain_spritesheet.get_image(7, 1, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'bottomSandGrassT':
			self.image = self.game.terrain_spritesheet.get_image(2, 1, self.width, self.height, self.scale, BLACK)

		# Fences
		if self.block_type == 'topLeftFence':
			self.image = self.game.terrain_spritesheet.get_image(4, 4, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'topRightFence':
			self.image = self.game.terrain_spritesheet.get_image(5, 4, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'topFence':
			self.image = self.game.terrain_spritesheet.get_image(8, 4, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'sideFence':
			self.image = self.game.terrain_spritesheet.get_image(1, 4, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'bottomLeftFence':
			self.image = self.game.terrain_spritesheet.get_image(7, 4, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'bottomRightFence':
			self.image = self.game.terrain_spritesheet.get_image(6, 4, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'topStopFence':
			self.image = self.game.terrain_spritesheet.get_image(3, 4, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'bottomStopFence':
			self.image = self.game.terrain_spritesheet.get_image(2, 4, self.width, self.height, self.scale, BLACK)

		#campfire
		if self.block_type == 'campFire':
			self.image = self.game.terrain_spritesheet.get_image(4, 5, self.width, self.height, self.scale, BLACK)

		#Road
		if self.block_type == 'roadH':
			self.image = self.game.terrain_spritesheet.get_image(6, 6, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'roadV':
			self.image = self.game.terrain_spritesheet.get_image(1, 6, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'roadTopR':
			self.image = self.game.terrain_spritesheet.get_image(8, 6, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'roadTopL':
			self.image = self.game.terrain_spritesheet.get_image(7, 6, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'roadBottomLeft':
			self.image = self.game.terrain_spritesheet.get_image(1, 7, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'roadBottomRight':
			self.image = self.game.terrain_spritesheet.get_image(2, 7, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'roadT':
			self.image = self.game.terrain_spritesheet.get_image(2, 6, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'roadTReverse':
			self.image = self.game.terrain_spritesheet.get_image(3, 6, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'roadTRight':
			self.image = self.game.terrain_spritesheet.get_image(4, 6, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'roadTLeft':
			self.image = self.game.terrain_spritesheet.get_image(5, 6, self.width, self.height, self.scale, BLACK)

		if self.block_type == 'firstStagePotato':
			self.image = self.game.terrain_spritesheet.get_image(5, 3, self.width, self.height, self.scale, BLACK)
		if self.block_type == 'firstStageCorn':
			self.image = self.game.terrain_spritesheet.get_image(1, 5, self.width, self.height, self.scale, BLACK)

		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y

	def update(self):
		if self.growStage >= 1 and self.growStage <= 3:
			if self.block_type == 'firstStagePotato' or self.block_type == 'secondStagePotat' or self.block_type == 'rottenPotat':
				if self.growStage == 1:
					self.time += 1
					if self.time >= self.timeToGrow:
						self.image = self.game.terrain_spritesheet.get_image(6, 3, self.width, self.height, self.scale, BLACK)
						self.growStage += 1
						self.block_type = 'secondStagePotat'
						self.time = 0
						self.timeToGrow = random.randint(GROW_MINTIME_STAGE1,GROW_MAXTIME_STAGE1)
				elif self.growStage == 2:
					self.time += 1
					if self.time >= self.timeToGrow:
						self.image = self.game.terrain_spritesheet.get_image(7, 3, self.width, self.height, self.scale, BLACK)
						self.growStage += 1
						self.block_type = 'rottenPotat'
						self.time = 0
						self.timeToGrow = random.randint(GROW_MINTIME_STAGE1,GROW_MAXTIME_STAGE1)
				elif self.growStage == 3:
					self.time += 1
					if self.time >= self.timeToGrow:
						self.image = self.game.terrain_spritesheet.get_image(8, 3, self.width, self.height, self.scale, BLACK)
						self.block_type = 'deadDirt'
						self.growStage += 1

			else:
				if self.growStage == 1:
					self.time += 1
					if self.time >= self.timeToGrow:
						self.image = self.game.terrain_spritesheet.get_image(2, 5, self.width, self.height, self.scale, BLACK)
						self.growStage += 1
						self.block_type = 'secondStageCorn'
						self.time = 0
						self.timeToGrow = random.randint(GROW_MINTIME_STAGE1,GROW_MAXTIME_STAGE1)
				elif self.growStage == 2:
					self.time += 1
					if self.time >= self.timeToGrow:
						self.image = self.game.terrain_spritesheet.get_image(3, 5, self.width, self.height, self.scale, BLACK)
						self.growStage += 1
						self.block_type = 'rottenCorn'
						self.time = 0
						self.timeToGrow = random.randint(GROW_MINTIME_STAGE1,GROW_MAXTIME_STAGE1)
				elif self.growStage == 3:
					self.time += 1
					if self.time >= self.timeToGrow:
						self.image = self.game.terrain_spritesheet.get_image(8, 3, self.width, self.height, self.scale, BLACK)
						self.block_type = 'deadDirt'
						self.growStage += 1


class Button:
	def __init__(self, x, y, width, height, fg, bg, content, fontsize):
		self.font = pygame.font.Font(os.path.join('assets/font', 'Pixeltype.ttf'), fontsize)
		self.content = content

		self.x = x
		self.y = y
		self.width = BUTTON_WIDTH
		self.height = BUTTON_HEIGHT

		self.fg = fg
		self.bg = bg

		self.button_spritesheet = SpriteSheet(pygame.image.load(os.path.join('assets/img/tests', 'buttons.png')).convert_alpha())
		
		img = self.button_spritesheet.get_image(bg[0], bg[1], self.width, self.height, 10, BLACK)
		self.image = pygame.transform.scale(img,(width,height))
		self.image = self.image.convert_alpha()
		self.rect = self.image.get_rect()

		self.rect.x = self.x
		self.rect.y = self.y

		self.text = self.font.render(self.content, True, self.fg)
		self.text_rect = self.text.get_rect(center=(width//2, height//2))
		self.image.blit(self.text, self.text_rect)

	def is_pressed(self, pos, pressed):
		if self.rect.collidepoint(pos):
			if pressed[0]:
				return True
			return False
		return False

class ButtonNoText:
	def __init__(self, x, y, width, height, bg):

		self.x = x
		self.y = y
		self.width = width
		self.height = height

		self.bg = bg

		self.button_spritesheet = SpriteSheet(pygame.image.load(os.path.join('assets/img/tests', 'buttons.png')).convert_alpha())

		img = self.button_spritesheet.get_image(bg[0], bg[1], self.width, self.height, 10, BLACK)
		self.image = pygame.transform.scale(img,(width,height))
		self.image = self.image.convert_alpha()
		self.rect = (self.x,self.y)

class Crab(pygame.sprite.Sprite):
	def __init__(self, game, x, y, hp,speed):
		self.width = CRAB_WIDTH
		self.height = CRAB_HEIGHT
		self.scale = CRAB_SCALE

		self._layer = CRAB_LAYER
		self.game = game
		self.animation_loop = 0
		self.speed = speed

		self.groups = self.game.all_sprites, self.game.enemies
		pygame.sprite.Sprite.__init__(self, self.groups)

		self.x = x
		self.y = y

		#Image variable
		self.x_change = 0
		self.y_change = 0

		self.hp = hp



		self.image = self.game.crab_spritesheet.get_image(1, 1, self.width, self.height, self.scale, BLACK)

		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y

	def update(self):
		self.movement()
		self.animate()

		self.rect.x += self.x_change
		self.collision('x')
		self.rect.y += self.y_change
		self.collision('y')

		self.x_change = 0
		self.y_change  = 0

		self.death()

	def collision(self, direction):

		if direction == 'x':
			hit = pygame.sprite.spritecollide(self, self.game.blocks_collid, False)
			if hit:
				if self.x_change > 0:
					self.rect.x = hit[0].rect.left - self.rect.width
					# self.rect.y += self.speed * 2
				if self.x_change < 0:
					self.rect.x = hit[0].rect.right
					# self.rect.y += self.speed * 2
		elif direction == 'y':
			hit = pygame.sprite.spritecollide(self, self.game.blocks_collid, False)
			if hit:
				if self.y_change > 0:
					self.rect.y = hit[0].rect.top - self.rect.height
					# self.rect.x += self.speed * 2
				if self.y_change < 0:
					self.rect.y = hit[0].rect.bottom
					# self.rect.x += self.speed * 2


	def damaged(self,damaged):
		# mouse_pos = pygame.mouse.get_pos()
		# mouse_pressed = pygame.mouse.get_pressed()
		# if mouse_pressed[0]:
		# 	if self.rect.collidepoint(mouse_pos) == True:
		# 		self.hp += -20

		# hit = pygame.sprite.spritecollide(self, self.game.bullets, False)
		#
		# if hit:
			self.hp += -damaged

	def death(self):
		if self.hp <= 0:
			self.game.nb_crabs_left -= 1
			self.game.nbCrabOnScreen -= 1
			self.kill()

	def movement(self):
		if self.game.player.x > self.rect.x:
			if self.game.player.x - self.rect.x < self.speed:
				self.x_change += self.game.player.x - self.rect.x
			else:
				self.x_change += self.speed
		if self.game.player.x < self.rect.x:
			if self.rect.x - self.game.player.x < self.speed:
				self.x_change -= self.rect.x - self.game.player.x
			else:
				self.x_change -= self.speed
		if self.game.player.y > self.rect.y:
			if self.game.player.y - self.rect.y < self.speed:
				self.y_change += self.game.player.y - self.rect.y
			else:
				self.y_change += self.speed
			
		if self.game.player.y < self.rect.y:
			if self.rect.y - self.game.player.y < self.speed:
				self.y_change -= self.rect.y - self.game.player.y
			else:
				self.y_change -= self.speed
			


	def animate(self):

		image = pygame.transform.flip(self.game.crab_spritesheet.get_image(1, 1, self.width, self.height, self.scale, BLACK), 1, 0)
		image.set_colorkey(BLACK)
		image1 = pygame.transform.flip(self.game.crab_spritesheet.get_image(2, 1, self.width, self.height, self.scale, BLACK), 1, 0)
		image1.set_colorkey(BLACK)
		image2 = pygame.transform.flip(self.game.crab_spritesheet.get_image(3, 1, self.width, self.height, self.scale, BLACK), 1, 0)
		image2.set_colorkey(BLACK)

		self.animation_loop += CRAB_VITESSE_ANIMATION

		if self.animation_loop < 1:
			self.image = image
		if self.animation_loop < 2:
			self.image = image1
		elif self.animation_loop < 3:
			self.image = image2

		if self.animation_loop >= 3:
			self.animation_loop = 0


class Bullet(pygame.sprite.Sprite):



	def __init__(self, game, x, y, destX, destY, speed):
		self.x = x
		self.y = y

		self.game = game
		self._layer = BULLET_LAYER
		self.groups = self.game.all_sprites, self.game.bullets
		pygame.sprite.Sprite.__init__(self, self.groups)


		self.angle = ((self.getAngleBetweenPoints(x, y, destX, destY) / (6/4)   * 90) - 360 ) * (-1)

		self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join('assets/img/tests', 'bullet_26x64.png')).convert_alpha(), (13, 32)), self.angle - 90)

		self.deplacementX = (destX - x) / 10
		self.deplacementY = (destY - y) / 10

		self.deplacementTotal = abs(self.deplacementX) + abs(self.deplacementY)

		self.deplacementX = self.deplacementX * (VITESSE_BULLET / self.deplacementTotal)
		self.deplacementY = self.deplacementY * (VITESSE_BULLET / self.deplacementTotal)



		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y

	def getAngleBetweenPoints(self, x_orig, y_orig, x_landmark, y_landmark):
		deltaY = y_landmark - y_orig
		deltaX = x_landmark - x_orig
		t = math.atan2(deltaY, deltaX)
		return self.angle_trunc(t)

	def angle_trunc(self, a):
		pi = 3.14159265359
		while a < 0.0:
			a += pi * 2
		return a

	def collisition(self):
		for enemies in self.game.enemies:
			if pygame.sprite.collide_mask(self, enemies):
				enemies.damaged(50)
				self.game.damaged_sound.play()
				self.kill()
				break
		hit = pygame.sprite.spritecollide(self, self.game.blocks_collid, False)
		if hit:
			self.kill()

	def update(self):
		self.collisition()
		self.rect.x += self.deplacementX
		self.rect.y += self.deplacementY

class KnifeCute(pygame.sprite.Sprite):
	def __init__(self, game):

		x, y = pygame.mouse.get_pos()

		self.game = game
		self._layer = BULLET_LAYER
		self.groups = self.game.all_sprites, self.game.bullets
		pygame.sprite.Sprite.__init__(self, self.groups)

		self.image = pygame.transform.scale(pygame.image.load(os.path.join('assets/img/tests', 'knife.png')).convert_alpha(), (13, 32))

		diff_x = self.game.player.rect.x - x
		diff_y = self.game.player.rect.y - y
		marge_de_deplacement_x = 15
		marge_de_deplacement_y = 15

		if abs(diff_x) > abs(diff_y):
			self.y = self.game.player.rect.y + marge_de_deplacement_y
			if diff_x < 0:#Droite
				self.x = self.game.player.rect.x  + 50 + marge_de_deplacement_x
				self.image = pygame.transform.rotate(self.image, -90)
				self.angle = "droite"
			else:#Gauche
				self.image = pygame.transform.rotate(self.image, 90)
				self.x = self.game.player.rect.x - 50
				self.angle = "gauche"
		else:
			self.x = self.game.player.rect.x + marge_de_deplacement_x
			if diff_y < 0: #Bas
				self.image = pygame.transform.flip(self.image, 0,1)
				self.y = self.game.player.rect.y + 50+ marge_de_deplacement_y
				self.angle = "bas"
			else: #Haut
				self.y = self.game.player.rect.y - 50+ marge_de_deplacement_y
				self.angle = "haut"

		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y

		self.in_animation = True
		self.current_time_animation = 0
		self.time_animation = 15
		self.speed = 1


	def collisition(self):
		for enemies in self.game.enemies:
			if pygame.sprite.collide_mask(self, enemies):
				enemies.damaged(50)
				self.game.damaged_sound.play()
				self.in_animation = False
				break
		hit = pygame.sprite.spritecollide(self, self.game.blocks_collid, False)
		if hit:
			self.in_animation = False

	def animation(self):
		if self.in_animation:
			if (self.current_time_animation == self.time_animation ):
				self.in_animation = False
			else:
				self.current_time_animation += 1
				if (self.angle == "haut"):
					self.rect.y -= self.speed
				elif (self.angle == "bas"):
					self.rect.y += self.speed
				elif (self.angle == "gauche"):
					self.rect.x -= self.speed
				elif (self.angle == "droite"):
					self.rect.x += self.speed

		else:
			self.game.player.in_cutting = False
			self.kill()



	def update(self):
		self.collisition()
		self.animation()

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
