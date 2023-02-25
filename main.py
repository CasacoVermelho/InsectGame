import pygame, sys
from settings import *
from utils import display_score
from eggs import Egg
from player import Player
import random


#pygame setup
pygame.init()
pygame.key.set_repeat(5)

pygame.display.set_caption('Eggsplosion!')
screen = pygame.display.set_mode((s_width,s_height))
clock = pygame.time.Clock()
score = 0

# Create a sprite group for the eggs to manage the objects
eggs = pygame.sprite.Group()

# definição do player e criação do grupo single para gerenciar seus sprites
player = Player(screen, (500, 500))
playerSP = pygame.sprite.GroupSingle(player)


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

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN:
					player.move(0)
				if event.key == pygame.K_LEFT:
					player.move(2)
				if event.key == pygame.K_RIGHT:
					player.move(1)
				if event.key == pygame.K_UP:
					player.move(3)
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_DOWN:
					player.endMove(0)
				if event.key == pygame.K_LEFT:
					player.endMove(1)
				if event.key == pygame.K_RIGHT:
					player.endMove(2)
				if event.key == pygame.K_UP:
					player.endMove(3)

	if game_menu == 0:
		if len(eggs) < 3:
			if random.randint(0, 59) == 0:
				# print("spawn")
				eggs.add(Egg(screen, (random.randint(32, s_width - 32),random.randint(32, s_height - 32))))
		
		for egg in eggs:
			if pygame.time.get_ticks() - egg.birth_time > 3000:
				eggs.remove(egg)

# desenhando as coisas da tela
		screen.fill('black')
		eggs.update()
		eggs.draw(screen)
		playerSP.draw(screen)
		display_score(score, screen)

	pygame.display.update()
	clock.tick(60)