import pygame

class Bullet(pygame.sprite.Sprite):
	"""docstring for player"""
	def __init__(self, pos):

		pygame.sprite.Sprite.__init__(self,self.groups)
		self.image = pygame.image.load('energy_ball.png')
		self.image = pygame.transform.scale(self.image, (30,30))
		self.rect  = self.image.get_rect()
		self.rect.center = pos

		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
	

	def update(self):
		self.rect.center = (self.rect.center[0],self.rect.center[1]-10)