from noise import pnoise1, pnoise2
from random import randint
from hashlib import md5
from PIL import Image
from math import sqrt
import pygame

def noise1D(val, seed, sharp=100.):
	seed = parse_seed(seed)
	return pnoise1((val/sharp) + seed)
def noise2D(val1, val2, seed, sharp=100.):
	seed = parse_seed(seed)
	return pnoise2((val1/sharp) + seed, (val2/sharp) + seed)
def translate(value, leftMin, leftMax, rightMin, rightMax):
	leftSpan = leftMax - leftMin
	rightSpan = rightMax - rightMin
	valueScaled = float(value - leftMin) / float(leftSpan)
	return rightMin + (valueScaled * rightSpan)
def parse_seed(seed):
	h = md5(str(seed)).hexdigest()
	s = translate(int(h, 16), 0, 10**38, 0, 100)
	return s
def dist_between(x1, y1, x2, y2):
	return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
def randcolor():
	r=randint(0,255)
	g=randint(0,255)
	b=randint(0,255)
	return r, g, b

img = Image.new('RGB', (1000, 1000))
img = img.convert("RGBA")

noise = []
size = 1000
seed = randint(0, 10000)
color = randcolor()
ocean = randcolor()
water = randint(20, 80)
sharp = float(randint(50, 100))

for y in xrange(1, size+1):
	for x in xrange(1, size+1):
		if dist_between(x, y, *[size/2]*2) < size/2:
			n = translate(noise2D(x, y, seed, sharp=sharp), -1, 1, 0, 1)
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
			noise.append((255, 255, 255, 0))

img.putdata(noise)
img.save('image.png')

print color
print ocean
print water
print sharp