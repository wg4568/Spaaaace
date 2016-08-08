from random import randint, seed as set_seed
import helpers

def temperature(value, minimum=-100, maximum=100):
	minimum, maximum = float(minimum), float(maximum)
	ratio = 2 * (value-minimum) / (maximum - minimum)
	b = int(max(0, 255*(1 - ratio)))
	r = int(max(0, 255*(ratio - 1)))
	g = 200 - b - r
	if g < 0:
		g = 0
	return r, g, b

def water(value):
	val = helpers.translate(value, -100, 100, 0, 255)
	r = val
	b = 255-val
	g = 255-(val*(val/200))
	if g<0:g=0
	return r, g, b

def random_color(seed=helpers.random_seed()):
#	set_seed(seed)
	r=randint(0,255)
	g=randint(0,255)
	b=randint(0,255)
#	set_seed(helpers.random_seed())
	return r, g, b

if __name__ == '__main__':
	import pygame
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

			self.temp = -100
			self.change = 0.5

			pygame.display.set_caption(self.title)

		def movement(self):
			keys = pygame.key.get_pressed()
			pass

		def draw(self):
			self.screen.fill(temperature(self.temp))

			text = self.font.render("%i degrees" % (self.temp), True, (0, 0, 0))
			self.screen.blit(text, (10, 10))

		def start(self):
			self.running = True
			while self.running:
				self.frame += 1
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						self.running = False

				if self.temp == 100:
					self.change = -0.5
				if self.temp == -100:
					self.change = 0.5

				self.temp += self.change

				self.movement()
				self.draw()

				pygame.display.update()
				self.clock.tick(self.rate)

	game = Game()
	game.start()