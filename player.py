import pygame
from utils import load_frames

class Player(pygame.sprite.Sprite):
	def __init__(self, screen, pos):
		super().__init__()

		self.screen = screen
		self.pos = list(pos)

		self.standFrames = load_frames('sprites/insects/Mantis.png', 32, 2)
		self.walkingFrames = load_frames('sprites/insects/MantisMove.png', 32, 2)
		# frame shanenigans
		self.current_frame = 0 #herdado da classe eggs, sem uso por enquanto
		self.frameAux = 0
		self.frame_duration = 100 # miliseconds
		self.last_update = pygame.time.get_ticks()
		self.last_dir = 5

		self.image = self.standFrames[0]
		self.rect = self.image.get_rect()
		self.rect.center = self.pos

	def move(self, direction):
		now = pygame.time.get_ticks()
		elapsed = now - self.last_update

		if elapsed > self.frame_duration:
			if self.last_dir != direction:
				print("diff dir")
				self.frameAux = 0
				self.last_dir = direction

			self.image = self.walkingFrames[self.frameAux%4+(direction*4)]
			self.frameAux += 1
			self.last_update = now

		if direction == 0:
			self.pos[1] += 1
			self.rect.center = self.pos
		if direction == 1:
			self.pos[0] += 1
			self.rect.center = self.pos
		if direction == 2:
			self.pos[0] += -1
			self.rect.center = self.pos
		if direction == 3:
			self.pos[1] += -1
			self.rect.center = self.pos

		# As 4 direções são:
		# 0 = baixo 0 ate 3
		# 1 = direita 4 ate 7
		# 2 = esquerda 8 ate 11
		# 3 = cima	12 ate 15

	def endMove(self, direction):
		self.image = self.standFrames[direction]

		# As 4 direções são:
		# 0 = baixo
		# 1 = esquerda
		# 2 = direita
		# 3 = cima