import pygame
from settings import *

def load_frames(sheet_path, frame_size):
	sheet = pygame.image.load(sheet_path).convert_alpha()
	sheet_size = sheet.get_size()
	rows = sheet_size[1] // frame_size
	cols = sheet_size[0] // frame_size

	frames = []

	for row in range(rows):
		for col in range(cols):
			rect = pygame.Rect(col * frame_size, row * frame_size, frame_size, frame_size)
			frames.append(sheet.subsurface(rect))

	return frames

def display_score(score, screen):
	score_surf = font_score.render(f'{"Score: " + str(score)}',False,(255,255,255))
	score_rect = score_surf.get_rect(center = (400,50))
	screen.blit(score_surf,score_rect)
	return score