import pygame, helpers, loadingbars
from random import randint
from PIL import Image, ImageFilter

img = Image.new('RGB', (1000, 1000))
img = img.convert("RGBA")

noise = []
size = 1000
temp = 100
seed = randint(0, 10000)
color = helpers.random_color()
ocean = helpers.random_color()
water = 50
sharp = 300.

loadingbarsbar = loadingbars.LoadingBar(minval=0, maxval=size)

for y in xrange(1, size+1):
	loadingbarsbar.set(y)
	for x in xrange(1, size+1):
		if helpers.dist_between(x, y, *[size/2]*2) < size/2:
			n = helpers.translate(helpers.noise2D(x, y, seed, sharp=sharp), -1, 1, 0, 1)
			if n > water/100.:
				r = int(n*color[0])
				g = int(n*color[1])
				b = int(n*color[2])
			else:
				r = int(n*ocean[0])
				g = int(n*ocean[1])
				b = int(n*ocean[2])
			noise.append((r, g, b))
		else:
			noise.append((0, 0, 0, 0))

x = ImageFilter.GaussianBlur(radius=size/100)

img.putdata(noise)
blurred_image = img.filter(x)
blurred_image.save('image.png')

print color, ocean, water, sharp, seed

planet = pygame.transform.scale(pygame.image.load("image.png"), [500, 500])

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
		self.screen.blit(planet, [0, 0])

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