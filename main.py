import pygame, sys
from settings import *
from utils import display_score
from eggs import Egg
import random


#pygame setup
pygame.init()

pygame.display.set_caption('Eggsplosion!')
screen = pygame.display.set_mode((s_width,s_height))
clock = pygame.time.Clock()
score = 0

# Create a sprite group for the eggs to manage the objects
eggs = pygame.sprite.Group()


game_menu = 0

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	if game_menu == 0:
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_pos = pygame.mouse.get_pos()
			for egg in eggs:
				if egg.rect.collidepoint(mouse_pos):
					egg.clickEgg(eggs)
					score += 1

		if len(eggs) < 3:
			if random.randint(0, 59) == 0:
				print("spawn")
				eggs.add(Egg(screen, (random.randint(32, s_width - 32),random.randint(32, s_height - 32))))
		
		for egg in eggs:
			if pygame.time.get_ticks() - egg.birth_time > 3000:
				eggs.remove(egg)

# desenhando as coisas da tela
		screen.fill('black')
		eggs.update()
		eggs.draw(screen)
		display_score(score, screen)

	pygame.display.update()
	clock.tick(60)