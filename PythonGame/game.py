import pygame , sys
from classes import *
from process import process 
from score import score
from end import *

pygame.mixer.init()

Explosion = pygame.mixer.Sound("Explosion.wav")
Laser = pygame.mixer.Sound("Laser.wav")

def game_fn (): 
	Fire.List.empty()
	FireProjectile.List.empty()
	Exterminator.List.empty()
	BaseClass.allsprites.empty()
	pygame.mixer.music.load("cartoon.wav")
	pygame.mixer.music.play(-1)
	SCREENWIDTH, SCREENHEIGHT = 640, 360 
	screen = pygame.display.set_mode((640, 360),0, 32)
	WIDTH, HEIGHT = 630, 360
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	background = pygame.image.load("basement.jpg")
	clock = pygame.time.Clock()
	FPS = 24
	exterminator = Exterminator(0, SCREENHEIGHT - 40, "Exterminator1.png")
	total_frames = 0 
	
	end_game = True 	
	x = 0
	while end_game:

		process(exterminator, FPS, total_frames)	
	
		exterminator.motion(SCREENWIDTH, SCREENHEIGHT)
		Fire.update_all(SCREENWIDTH, SCREENHEIGHT) 
		FireProjectile.movement() 
		total_frames = total_frames + 1                                            
		screen.blit(background, (0, 0))
		BaseClass.allsprites.draw(screen)
		FireProjectile.List.draw(screen) 
		score_stat = score(x, SCREENHEIGHT)
		x = score_stat 
		for fire in Fire.List: 
			col = pygame.sprite.spritecollide(fire, Exterminator.List, True)
			if len(col) > 0: 
				end_game = False
		font = pygame.font.Font(None, 36)
		text = font.render("Kills: " + str(score_stat), 1, (10, 10, 10))
		screen.blit(text, (440, 7))		

		clock.tick(FPS)
		pygame.display.flip() 
	end(score_stat)
