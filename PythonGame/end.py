import pygame , sys
from classes import *
from process import process 
from score import score
from game import *

def game_fn (num, adder): 
	SCREENWIDTH, SCREENHEIGHT = 640, 360 
	screen = pygame.display.set_mode((640, 360),0, 32)
	WIDTH, HEIGHT = 630, 360
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	background = pygame.image.load("basement.jpg")
	clock = pygame.time.Clock()
	FPS = 24
	exterminator = Exterminator(0, SCREENHEIGHT - 40, "Exterminator1.png", 0)
	total_frames = 0 
	end_game = True 	
	p = 0 
	x = 0 
	while end_game:

		process(exterminator, FPS, total_frames, adder)	
		
		exterminator.motion(SCREENWIDTH, SCREENHEIGHT)
		Fire.update_all(SCREENWIDTH, SCREENHEIGHT) 
		FireProjectile.movement() 
		total_frames = total_frames + 1                                            
		screen.blit(background, (0, 0))
		BaseClass.allsprites.draw(screen)
		FireProjectile.List.draw(screen) 
		score_stat = score(num, SCREENHEIGHT)
		p = score_stat
		num = p
		if p == 10: 
			end_game = False
		elif p == 20: 
			end_game = False
		elif p == 30: 
			end_game = False 
		elif p == 40: 
			end_game = False 
		for fire in Fire.List: 
			col = pygame.sprite.spritecollide(fire, Exterminator.List, True)
			if len(col) > 0: 
				end_game = False
			font = pygame.font.Font(None, 36)
			text = font.render("Kills: " + str(num), 1, (10, 10, 10))
		screen.blit(text, (443, 7))		

		clock.tick(FPS)
		pygame.display.flip() 
	if p == 10: 
		level1(score_stat)
	elif p == 20: 
		level2(score_stat)
	elif p == 30: 
		level3(score_stat)
	elif p == 40: 
		level4(score_stat) 
	else: 
		end(score_stat)


def level1(score): 
	SCREENWIDTH, SCREENHEIGHT = 640, 360 
	screen = pygame.display.set_mode((640, 360),0, 32)
	WIDTH, HEIGHT = 630, 360
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	background = pygame.image.load("basement.jpg")
	clock = pygame.time.Clock()
	FPS = 24
	exterminator = Exterminator(0, SCREENHEIGHT - 40, "Exterminator1.png", 0)
	total_frames = 0 


	final_background = pygame.image.load("Level1.png")
	final_screen = False
	restart_game = True 
	while restart_game == True: 
		screen.blit(final_background, (0,0))
		font = pygame.font.Font(None, 25)
		text = font.render("Enjoy 1 Free Kill!!!", 1, (10, 10, 10))
		screen.blit(text, (450, 20))	
	

		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				pygame.quit() 
				sys.exit() 
			elif event.type == pygame.MOUSEBUTTONDOWN:
				restart_game = False
		pygame.display.flip() 
		clock.tick(FPS)
	Fire.List.empty()
	FireProjectile.List.empty()
	Exterminator.List.empty()
	BaseClass.allsprites.empty()
	game_fn(score+1, 3)
	


def level2(score): 
	SCREENWIDTH, SCREENHEIGHT = 640, 360 
	screen = pygame.display.set_mode((640, 360),0, 32)
	WIDTH, HEIGHT = 630, 360
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	background = pygame.image.load("basement.jpg")
	clock = pygame.time.Clock()
	FPS = 24
	exterminator = Exterminator(0, SCREENHEIGHT - 40, "Exterminator1.png", 0)
	total_frames = 0 


	final_background = pygame.image.load("Level2")
	final_screen = False
	restart_game = True 
	while restart_game == True: 
		screen.blit(final_background, (0,0))
		font = pygame.font.Font(None, 25)
		text = font.render("Enjoy 1 Free Kill!!!" , 1, (10, 10, 10))
		screen.blit(text, (377, 150))	
	

		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				pygame.quit() 
				sys.exit() 
			elif event.type == pygame.MOUSEBUTTONDOWN:
				restart_game = False
		pygame.display.flip() 
		clock.tick(FPS)
	Fire.List.empty()
	FireProjectile.List.empty()
	Exterminator.List.empty()
	BaseClass.allsprites.empty()
	game_fn(score+1, 4)
	

	

def level3(score): 
	SCREENWIDTH, SCREENHEIGHT = 640, 360 
	screen = pygame.display.set_mode((640, 360),0, 32)
	WIDTH, HEIGHT = 630, 360
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	background = pygame.image.load("basement.jpg")
	clock = pygame.time.Clock()
	FPS = 24
	exterminator = Exterminator(0, SCREENHEIGHT - 40, "Exterminator1.png", 0)
	total_frames = 0 


	final_background = pygame.image.load("Level3")
	final_screen = False
	restart_game = True 
	while restart_game == True: 
		screen.blit(final_background, (0,0))
		font = pygame.font.Font(None, 25)
		text = font.render("Enjoy 1 free kill!!!" , 1, (10, 10, 10))
		screen.blit(text, (377, 150))	
	

		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				pygame.quit() 
				sys.exit() 
			elif event.type == pygame.MOUSEBUTTONDOWN:
				restart_game = False
		pygame.display.flip() 
		clock.tick(FPS)
	Fire.List.empty()
	FireProjectile.List.empty()
	Exterminator.List.empty()
	BaseClass.allsprites.empty()
	game_fn(score+1, 5) 
	

def level4(): 
	SCREENWIDTH, SCREENHEIGHT = 640, 360 
	screen = pygame.display.set_mode((640, 360),0, 32)
	WIDTH, HEIGHT = 630, 360
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	background = pygame.image.load("basement.jpg")
	clock = pygame.time.Clock()
	FPS = 24
	exterminator = Exterminator(0, SCREENHEIGHT - 40, "Exterminator1.png", 0)
	total_frames = 0 


	final_background = pygame.image.load("Level4")
	final_screen = False
	restart_game = True 
	while restart_game == True: 
		screen.blit(final_background, (0,0))
		font = pygame.font.Font(None, 25)
		text = font.render("Congrats you made it to the last level!", 1, (10, 10, 10))
		screen.blit(text, (377, 150))	
	

		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				pygame.quit() 
				sys.exit() 
			elif event.type == pygame.MOUSEBUTTONDOWN:
				restart_game = False
		pygame.display.flip() 
		clock.tick(FPS)
	Fire.List.empty()
	FireProjectile.List.empty()
	Exterminator.List.empty()
	BaseClass.allsprites.empty()
	game_fn(score+1, 5) 
	

def score_file (score_stat): 
	hfile = open("highscore.txt", "a")
	hfile.write("\n" + str(score_stat))
	hfile.close()

def ten_scores (): 
	tfile = open("highscore.txt", "r")
	filecont = tfile.readline(10)
	tfile.close()
	nfile = open("highscore2", "w")
	nfile.write(filecont)
	nfile.close()


	tfile.close()

def end (score_stat): 
	SCREENWIDTH, SCREENHEIGHT = 640, 360 
	screen = pygame.display.set_mode((640, 360),0, 32)
	WIDTH, HEIGHT = 630, 360
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	background = pygame.image.load("basement.jpg")
	clock = pygame.time.Clock()
	FPS = 24
	exterminator = Exterminator(0, SCREENHEIGHT - 40, "Exterminator1.png", 0)
	total_frames = 0 

	score_file(score_stat)
	ten_scores()
	final_background = pygame.image.load("screen_end.png")
	final_screen = False
	restart_game = True 
	while restart_game == True: 
		screen.blit(final_background, (0,0))
		font = pygame.font.Font(None, 25)
		text = font.render("Mice killed: " + str(score_stat), 1, (10, 10, 10))
		screen.blit(text, (377, 150))	
		

		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				pygame.quit() 
				sys.exit() 
			elif event.type == pygame.MOUSEBUTTONDOWN:
				restart_game = False
		pygame.display.flip() 
		clock.tick(FPS)
	Fire.List.empty()
	FireProjectile.List.empty()
	Exterminator.List.empty()
	BaseClass.allsprites.empty()
	game_fn(0, 0)

	

