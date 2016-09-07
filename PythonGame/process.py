
import pygame, sys, classes, random

pygame.mixer.init()

woop = pygame.mixer.Sound("woop.wav")
Laser = pygame.mixer.Sound("Laser.wav")


def process(exterminator, FPS, total_frames, adder): 

	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			pygame.quit() 
			sys.exit() 

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_e: 
				classes.FireProjectile.fire = not classes.FireProjectile.fire

	keys = pygame.key.get_pressed() 

	if keys[pygame.K_d]: 
		classes.Fire.going_right = True 
		exterminator.velx = 5
		exterminator.image = pygame.image.load("Exterminator1.png")
	elif keys[pygame.K_a]: 
		exterminator.image = pygame.image.load("Exterminator_flip.png")
		classes.Fire.going_right  = False 
		exterminator.velx = -5 
	else: 
		exterminator.velx = 0

	if keys[pygame.K_w]: 
		exterminator.jumping = True
		exterminator.go_down = False
	elif keys[pygame.K_s]:
		
		exterminator.go_down = True
	if keys[pygame.K_SPACE]: 
		
		def direction(): 
			if classes.Fire.going_right: 
				Laser.play()
				projectile.velx = 8
			else: 
				Laser.play()
				projectile.image = pygame.transform.flip(projectile.image, True, False)
				projectile.velx = -8 
		if (classes.FireProjectile.fire): 
			projectile = classes.FireProjectile(exterminator.rect.x, exterminator.rect.y, True, "projectile.png")

			direction()
		else: 
			projectile = classes.FireProjectile(exterminator.rect.x, exterminator.rect.y, False, "blueflame.png")
			direction() 





	spawn(FPS, total_frames, adder)

	collisions() 


def spawn(FPS, total_frames, adder): 
	four_seconds = FPS * 4
	if total_frames % four_seconds == 0: 
		r = random.randint(1,2) 
		x = 1 
		if r == 2: 
			x = 640 - 40 
		fire = classes.Fire(x, 130, "rat.png", adder)


def collisions(): 

	for fire in classes.Fire.List: 
		proj = pygame.sprite.spritecollide(fire, classes.FireProjectile.List, True)

		for projectile in proj: 
			
			fire.health = 0 
			if projectile.if_this_variable_is_true_then_fire: 
				woop.play() 
				fire.image = pygame.image.load("skull.png")
				

			else: 
				if fire.velx > 0: 
					woop.play()
					fire.image = pygame.image.load("frozen.png")
					
					 
				elif fire.velx < 0: 
					woop.play()
					fire.image = pygame.image.load("frozen.png")
					

					fire.image = pygame.transform.flip(fire.image, True, False)
			projectile.rect.x = 2 * -projectile.rect.width 
			projectile.destroy() 




			














