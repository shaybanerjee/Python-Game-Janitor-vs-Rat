import pygame, sys, classes, random

def score (x, SCREENHEIGHT):
	score = x 
	for fire in classes.Fire.List: 
		if fire.health <= 0: 
			fire.velx = 0
			if fire.rect.y + fire.rect.height < SCREENHEIGHT: 
				None
			else: 
				score = score + 1 
	return score