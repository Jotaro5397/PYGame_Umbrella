import time

import pygame, sys, random
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Rain rain rain")
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGD_COLOUR = (230, 255, 250)
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
cloud_image = pygame.image.load("Assets/cloud.png").convert_alpha()
cloud_image_tr = pygame.transform.scale(cloud_image, (200,100))
player_image = pygame.image.load("Assets/avatar.png").convert()
# image should not have been converted with convert_alpha(0 but with convert()
player_image.set_colorkey((255,255,255))
player_umbrella = pygame.image.load("Assets/avatarUmbrella.png").convert()
clock = pygame.time.Clock()
last_hit_time = 0

Ui_font = pygame.font.SysFont("arial", 25)

time.time()

class RainDrop:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.vel =random.randint(1,10)
		#self.accl = 0

	def move(self):
		self.y += self.vel
		#self.accl += 0.1

	def draw(self):
		pygame.draw.circle(screen, (150,150,150), (self.x, self.y), 2)




class Cloud:
	def __init__(self):
		self.x = -400
		self.y = 100

	def move(self):
		self.x += 1

	def draw(self):
		screen.blit(cloud_image_tr, (self.x,self.y))

	def createRain(self):
		raindrops.append(RainDrop(random.randint(self.x,self.x +200), self.y +100))


class Player:
	def __init__(self):
		self.x = 0
		self.y = SCREEN_HEIGHT - 190

	def move(self):
		if pressed_keys[K_RIGHT] and self.x < SCREEN_WIDTH - 100:
			self.x += 0.5
		if pressed_keys[K_LEFT] and self.x > 0:
			self.x -= 0.5



	def draw(self):
		if time.time() - last_hit_time > 2:
			screen.blit(player_image, (self.x,self.y))
		else:
			screen.blit(player_umbrella, (self.x, self.y))

	def hit_by(self, raindrop):

		return pygame.Rect(self.x,self.y, 119,192).collidepoint((raindrop.x, raindrop.y))

raindrops = []
cloud = Cloud()
player = Player()


while 1:
	clock.tick(250)
	#pygame registers all events from the users into an event queue
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		# if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
		# 	y += 2


	pressed_keys = pygame.key.get_pressed()
	screen.fill(BACKGD_COLOUR)



	# Creating the rain one raindrop at a time

	cloud.createRain()
	cloud.draw()
	cloud.move()
	player.draw()
	player.move()

	for raindrop in raindrops[:]:
		raindrop.move()
		raindrop.draw()
		if player.hit_by(raindrop):
			last_hit_time = time.time()
		if raindrop.y > SCREEN_HEIGHT:
			del raindrop


	pygame.display.flip()
