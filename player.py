
import pygame

from bullet import Bullet


class Player(pygame.sprite.Sprite):
	"""docstring for player"""
	def __init__(self):

		pygame.sprite.Sprite.__init__(self,self.groups) # never forget this line !
		self.image = pygame.image.load('ship.png')
		self.image = pygame.transform.scale(self.image, (50,50))
		self.rect  = self.image.get_rect()

		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
	


	def update(self):
		self.rect.center = pygame.mouse.get_pos()

	def shoot(self):
		newbullet = Bullet(pygame.mouse.get_pos())
