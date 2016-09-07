
import pygame
from random import randint
import math 
import copy 


class BaseClass(pygame.sprite.Sprite):
	allsprites = pygame.sprite.Group() 
	def __init__ (self, x, y, image_string, adder): 
		
		pygame.sprite.Sprite.__init__(self)
		BaseClass.allsprites.add(self) 

		self.image = pygame.image.load(image_string)
		self.rect = self.image.get_rect() 
		self.rect.x = x 
		self.rect.y = y

	def destroy(self, ClassName): 
		ClassName.List.remove(self) 
		BaseClass.allsprites.remove(self)
		del self 


class Exterminator (BaseClass): 
	List = pygame.sprite.Group()
	def __init__ (self, x, y, image_string, adder): 

		BaseClass.__init__(self, x, y, image_string, adder)
		Exterminator.List.add(self)
		self.velx, self.vely = 0, 5
		self.jumping, self.go_down = False, False 

	def motion(self, SCREENWIDTH, SCREENHEIGHT): 
		predicted_location = self.rect.x + self.velx 



		if predicted_location < 0 : 
			self.velx = 0 
		elif predicted_location + self.rect.width > SCREENWIDTH: 
			self.velx = 0
		self.rect.x += self.velx

		self.__jump(SCREENHEIGHT)
	
	def __jump (self, SCREENHEIGHT): 

		max_jump = 75

		if self.jumping: 

			if self.rect.y < max_jump: 
				self.go_down = True 
			if self.go_down: 
				self.rect.y += self.vely
				predicted_location = self.rect.y + self.vely 
				if predicted_location + self.rect.height > SCREENHEIGHT: 
					self.jumping = False
					self.go_down = False 
			else: 
				self.rect.y -= self.vely	



class Fire (BaseClass): 
	List = pygame.sprite.Group() 
	going_right = True 
	
	def __init__ (self, x, y, image_string, adder): 
		BaseClass.__init__ (self, x, y, image_string, adder)
		Fire.List.add(self)
		self.health = 100  
		self.velx, self.vely = randint(1 + adder, 2 + adder), 2
		self.amplitude, self.period = randint(20 , 140), randint (4,5) / 100.0
	
	@staticmethod
	def update_all(SCREENWIDTH, SCREENHEIGHT):
	
		for fire in Fire.List: 
			if fire.health <= 0: 
				fire.velx = 0
				if fire.rect.y + fire.rect.height < SCREENHEIGHT: 
					fire.rect.y += fire.vely
					

				else: 
					pygame.sprite.Sprite.kill(fire)
			else: 
				fire.fire(SCREENWIDTH)
	 

	



	def fire(self, SCREENWIDTH):
		if self.rect.x + self.rect.width > SCREENWIDTH or self.rect.x < 0: 
			self.image = pygame.transform.flip(self.image, True, False) 
			self.velx = -self.velx
		self.rect.x += self.velx 
		self.rect.y = self.amplitude * math.sin(self.period * self.rect.x) + 140 


	


	@staticmethod 
	def movement (SCREENWIDTH): 
		for fire in Fire.List: 
			fire.fire(SCREENWIDTH) 


class FireProjectile(pygame.sprite.Sprite): 
	List = pygame.sprite.Group()
	normal_list = [] 
	fire = True 
	def __init__ (self, x, y, if_this_variable_is_true_then_fire, image_string): 
		
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image_string)
		self.rect = self.image.get_rect() 
		self.rect.x = x 
		self.rect.y = y
		self.if_this_variable_is_true_then_fire = if_this_variable_is_true_then_fire
		self.rect.width
		
		try:
			last_element = FireProjectile.normal_list[-1] 
			difference = abs(self.rect.x - last_element.rect.x)
			if difference < self.rect.width: 
				return 

		except Exception: 
			pass

		FireProjectile.normal_list.append(self)
		FireProjectile.List.add(self)
		self.velx = None


	@staticmethod
	def movement(): 
		for projectile in FireProjectile.List: 
			projectile.rect.x += projectile.velx 

	def destroy(self): 
		FireProjectile.List.remove(self)
		FireProjectile.normal_list.remove(self)
		del self 

















