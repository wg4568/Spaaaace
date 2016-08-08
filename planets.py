import pygame, helpers, loadingbars
from random import randint
from PIL import Image, ImageFilter

class Planet:
	def __init__(self, seed="planet", size=1000, sharp=100, land_color=helpers.random_color(), ocean_color=helpers.random_color(), water=50, blur=10):
		self.seed = seed
		self.size = size
		self.sharp = float(sharp)
		self.sharp_img = Image.new('RGB', (1000, 1000)).convert("RGBA")
		self.land_color = land_color
		self.ocean_color = ocean_color
		self.water = water
		self.blur = blur
		self.blur_filter = ImageFilter.GaussianBlur(radius=self.blur)

	def generate_image(self):
		noise = []
		loadingbar = loadingbars.LoadingBar(minval=0, maxval=self.size)
		for y in xrange(1, self.size+1):
			loadingbar.set(y)
			for x in xrange(1, self.size+1):
				if helpers.dist_between(x, y, *[self.size/2]*2) < self.size/2:
					n = helpers.translate(helpers.noise2D(x, y, self.seed, sharp=self.sharp), -1, 1, 0, 1)
					if n > self.water/100.:
						r = int(n*self.land_color[0])
						g = int(n*self.land_color[1])
						b = int(n*self.land_color[2])
					else:
						r = int(n*self.ocean_color[0])
						g = int(n*self.ocean_color[1])
						b = int(n*self.ocean_color[2])
					noise.append((r, g, b))
				else:
					noise.append((0, 0, 0, 0))
		self.sharp_img.putdata(noise)
		self.blurred_img = self.sharp_img.filter(self.blur_filter)

	def save(self, fname, blurred=True):
		if blurred:
			self.blurred_img.save(fname)
		else:
			self.sharp_img.save(fname)