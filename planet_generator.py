import pygame, planets

planet = planets.Planet()
planet.generate_image()
planet.save("image.png")

planet_img = pygame.transform.scale(pygame.image.load("image.png"), [500, 500])

class Game:
	def __init__(self):
		pygame.init()

		self.title = "Test Game"
		self.rate = 60
		self.size = [500, 500]

		self.running = False
		self.frame = 0
		self.clock = pygame.time.Clock()
		self.screen = pygame.display.set_mode(self.size)
		self.font = pygame.font.Font('freesansbold.ttf', 12)

		pygame.display.set_caption(self.title)

	def movement(self):
		pass

	def draw(self):
		self.screen.blit(planet_img, [0, 0])

	def start(self):
		self.running = True
		while self.running:
			self.frame += 1
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

			self.movement()
			self.draw()

			pygame.display.update()
			self.clock.tick(self.rate)

game = Game()
game.start()