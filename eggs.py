import pygame
from utils import load_frames

class Egg(pygame.sprite.Sprite):
	def __init__(self, screen, pos):
		super().__init__()

		self.birth_time = pygame.time.get_ticks()

		self.screen = screen
		self.pos = pos
		self.frames = load_frames('sprites/insects/Eggsplosion.png', frame_size=32)

		self.current_frame = 0
		self.frame_duration = 100 # miliseconds
		self.last_update = pygame.time.get_ticks()

		self.image = self.frames[self.current_frame]
		self.rect = self.image.get_rect()
		self.rect.center = self.pos

	def update(self):
		now = pygame.time.get_ticks()
		elapsed = now - self.last_update

		if elapsed > self.frame_duration:
			self.current_frame = (self.current_frame + 1) % len(self.frames)
			self.image = self.frames[self.current_frame]
			self.last_update = now

	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def clickEgg(self, eggs):
		eggs.remove(self)
		print("Egg Clicked!")
