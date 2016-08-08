import pygame, helpers, loadingbars, os, binascii, colors
from PIL import Image, ImageFilter

def generate_values(temp, planet_type, seed):
	water = None
	land_color = None
	ocean_color = None
	sharp = None
	if planet_type == "gas":
		sharp = 400
		water = 0
	if planet_type == "earthlike":
		sharp = 100
		water = 50
	if planet_type == "desolate":
		sharp = 30
		water = 20
	land_color = colors.temperature(temp)
	ocean_color = colors.water(temp)

	return land_color, ocean_color, water, float(sharp)

class Planet:
	def __init__(self, 
			name=helpers.random_seed(),
			seed=helpers.random_seed(),
			image_size=1000,
			sharp=100,
			land_color=None,
			ocean_color=None,
			water=50,
			blur=10,
			size=100,
			temp=0,
			planet_type="earthlike"
		):
		self.blur = blur
		self.name = name
		self.seed = seed
		self.image_size = image_size
		self.size = size
		self.planet_type = planet_type
		self.temp = temp

		self.sharp_img = Image.new('RGB', (1000, 1000)).convert("RGBA")
		self.blur_filter = ImageFilter.GaussianBlur(radius=self.blur)

		self.land_color, self.ocean_color, self.water, self.sharp = generate_values(self.temp, self.planet_type, self.seed)

		"""
		self.sharp = float(sharp)

		if not land_color:
			self.land_color = helpers.random_color(seed=self.seed)
		if not ocean_color:
			self.ocean_color = helpers.random_color(seed=self.seed)

		self.water = water
		"""

	def image_generate(self):
		noise = []
		loadingbar = loadingbars.LoadingBar(minval=0, maxval=self.image_size)
		print "Generating planet named '%s' from seed '%s'..." % (self.name, str(self.seed))
		for y in xrange(1, self.image_size+1):
			loadingbar.set(y)
			for x in xrange(1, self.image_size+1):
				if helpers.dist_between(x, y, *[self.image_size/2]*2) < self.image_size/2:
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

	def image_save(self, fname, blurred=True):
		if blurred:
			self.blurred_img.save(fname)
		else:
			self.sharp_img.save(fname)