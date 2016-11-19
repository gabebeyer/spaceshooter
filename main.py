import pygame 
from pygame.locals import *
from player import Player
from bullet import Bullet

class App():
	"""main game class"""
	def __init__(self):
		self._running = True
		self._display_surf = None
		self.size = self.width, self.height = 400, 640
		self.screen=pygame.display.set_mode(self.size) 
		self.clock = pygame.time.Clock()
		self.FPS = 60   



	def on_init(self):
		
		pygame.init()
		pygame.font.init()
		pygame.mouse.set_visible(0)
		self._running = True
		
		self.myfont = pygame.font.SysFont('',20)
		self.background = pygame.Surface(self.size)
		self.background.fill((100,125,175))   
		self.screen.blit(self.background, (0,0))
		
		#gruoups are sets of sprites waiting to be rendered
		self.allgroup = pygame.sprite.Group()
		self.bulletgroup = pygame.sprite.Group()

		#assings sprite classes to groups 
		Player.groups = self.allgroup
		Bullet.groups = self.bulletgroup
		
		#spawn player
		self.player = Player()

	#game wide events
	def on_event(self,event):
		
		if event.type == pygame.QUIT:
			self._running = False
		
		elif event.type == pygame.MOUSEBUTTONDOWN:
			self.player.shoot()

	#called every frame
	def on_loop(self):
		pass

	def on_render(self):
		pass
	
	def on_cleanup(self):
		pygame.quit()

	def on_execute(self):
		if self.on_init() == False:
			self._running =- False

		while( self._running):
			for event in pygame.event.get():
				self.on_event(event)
			
			self.on_loop()
			self.on_render()

			self.screen.blit(self.background, (0,0))
			
			self.allgroup.update()
			self.bulletgroup.update()
	
			self.allgroup.draw(self.screen)
			self.bulletgroup.draw(self.screen)

	
			pygame.display.update()                

		self.on_cleanup()

if __name__ == '__main__':
	app = App()
	app.on_execute()

		