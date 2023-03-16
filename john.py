import pygame
from pygame.locals import *

class John(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		self.index = 0
		self.counter = 0
		for _ in range(1, 4):
			img = pygame.image.load('img/bird.png')
			self.images.append(img)
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]

	def update(self):
		#handle the animation
		self.counter += 1
		flap_cooldown = 5

		if self.counter > flap_cooldown:
			self.counter = 0
			self.index += 1
			if self.index >= len(self.images):
				self.index = 0
		self.image = self.images[self.index]