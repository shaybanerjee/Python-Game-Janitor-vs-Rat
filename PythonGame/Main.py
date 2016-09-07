import pygame , sys
from classes import *
from process import process 
from score import score
from game import *
from end import *
pygame.init() 
pygame.mixer.init()

SCREENWIDTH, SCREENHEIGHT = 640, 360 
screen = pygame.display.set_mode((640, 360),0, 32)
WIDTH, HEIGHT = 630, 360
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load("basement.jpg")
clock = pygame.time.Clock()
FPS = 24
exterminator = Exterminator(0, SCREENHEIGHT - 40, "Exterminator1.png", 0)
total_frames = 0 



black = (0,0,0)
end_it=False
start_background = pygame.image.load("start_screen.png")
while (end_it==False):
	screen.blit(start_background, (0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			pygame.quit() 
			sys.exit() 
		elif event.type == pygame.MOUSEBUTTONDOWN:
			end_it = True
	pygame.display.flip()
Fire.List.empty()
FireProjectile.List.empty()
Exterminator.List.empty()
BaseClass.allsprites.empty()
game_fn(0, 2)	
	








