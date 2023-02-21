import pygame
from eggs import Egg

def main():
	pygame.init()
	screen = pygame.display.set_mode((640, 480))
	pygame.display.set_caption('Eggsplosion!')

	eggs = pygame.sprite.Group()
	eggs.add(Egg(screen, (220, 240)))
	eggs.add(Egg(screen, (320, 240)))
	eggs.add(Egg(screen, (420, 240)))

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				return

		eggs.update()

		screen.fill((0, 0, 0))
		eggs.draw(screen)

		pygame.display.flip()

if __name__ == '__main__':
	main()