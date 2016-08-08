import pygame, planets, helpers, os, loadingbars, random

#planet = planets.Planet(temp=-60, planet_type="earthlike", image_size=500, blur=5, land_color=(102, 0, 102), ocean_color=(0, 0, 204), water=45)
planet = planets.Planet(ocean_color=(200, 0, 0), land_color=(10, 10, 10))
planet.image_generate()
planet.image_save("planet.png")
planet.image_save("planet_raw.png", blurred=False)

planet = pygame.image.load("planet.png")

class Game:
	def __init__(self):
		pygame.init()

		self.title = "Test Game"
		self.rate = 60
		self.size = [500, 500]

		self.running = False
		self.frame = 0
		self.offset = 0
		self.clock = pygame.time.Clock()
		self.screen = pygame.display.set_mode(self.size)
		self.font = pygame.font.Font('freesansbold.ttf', 12)
		self.zoom = 500

		pygame.display.set_caption(self.title)

	def movement(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_UP]:
			self.zoom+=1
		if keys[pygame.K_DOWN]:
			self.zoom-=1

	def draw(self):
		self.screen.fill((0, 0, 0))
		self.screen.blit(self.p, [0, 0])

	def start(self):
		global planet
		self.running = True
		while self.running:
			self.frame += 1
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

			self.p = pygame.transform.scale(planet, [self.zoom]*2)
			self.movement()
			self.draw()

			pygame.display.update()
			self.clock.tick(self.rate)

game = Game()
game.start()