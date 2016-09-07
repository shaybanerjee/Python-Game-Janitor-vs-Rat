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
		if score_stat > 10: 
			SCREENWIDTH, SCREENHEIGHT = 640, 360 
			screen = pygame.display.set_mode((640, 360),0, 32)
			WIDTH, HEIGHT = 630, 360
			screen = pygame.display.set_mode((WIDTH, HEIGHT))
			background = pygame.image.load("basement.jpg")
			clock = pygame.time.Clock()
			FPS = 24
			exterminator = Exterminator(0, SCREENHEIGHT - 40, "Exterminator1.png")
			total_frames = 0 
			final_background = pygame.image.load("screen_end.png")
		elif score_stat > 20:
			SCREENWIDTH, SCREENHEIGHT = 640, 360 
			screen = pygame.display.set_mode((640, 360),0, 32)
			WIDTH, HEIGHT = 630, 360
			screen = pygame.display.set_mode((WIDTH, HEIGHT))
			background = pygame.image.load("basement.jpg")
			clock = pygame.time.Clock()
			FPS = 24
			exterminator = Exterminator(0, SCREENHEIGHT - 40, "Exterminator1.png")
			total_frames = 0 
		elif score_stat > 30: 
			SCREENWIDTH, SCREENHEIGHT = 640, 360 
			screen = pygame.display.set_mode((640, 360),0, 32)
			WIDTH, HEIGHT = 630, 360
			screen = pygame.display.set_mode((WIDTH, HEIGHT))
			background = pygame.image.load("basement.jpg")
			clock = pygame.time.Clock()
			FPS = 24
			exterminator = Exterminator(0, SCREENHEIGHT - 40, "Exterminator1.png")
			total_frames = 0 
		elif score_stat > 40: 
			SCREENWIDTH, SCREENHEIGHT = 640, 360 
			screen = pygame.display.set_mode((640, 360),0, 32)
			WIDTH, HEIGHT = 630, 360
			screen = pygame.display.set_mode((WIDTH, HEIGHT))
			background = pygame.image.load("basement.jpg")
			clock = pygame.time.Clock()
			FPS = 24
			exterminator = Exterminator(0, SCREENHEIGHT - 40, "Exterminator1.png")
			total_frames = 0 
		elif score_stat > 50: 
			SCREENWIDTH, SCREENHEIGHT = 640, 360 
			screen = pygame.display.set_mode((640, 360),0, 32)
			WIDTH, HEIGHT = 630, 360
			screen = pygame.display.set_mode((WIDTH, HEIGHT))
			background = pygame.image.load("basement.jpg")
			clock = pygame.time.Clock()
			FPS = 24
			exterminator = Exterminator(0, SCREENHEIGHT - 40, "Exterminator1.png")
			total_frames = 0 


	final_background = pygame.image.load("screen_end.png")


	final_background = pygame.image.load("screen_end.png")


	final_background = pygame.image.load("screen_end.png")

	final_background = pygame.image.load("screen_end.png")

		clock.tick(FPS)
		pygame.display.flip() 
	end(score_stat)