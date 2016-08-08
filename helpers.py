from noise import pnoise1, pnoise2
from random import randint
from hashlib import md5
import math

def noise1D(val, seed, sharp=100.):
	seed = parse_seed(seed)
	return pnoise1((val/sharp) + seed)

def noise2D(val1, val2, seed, sharp=100.):
	seed = parse_seed(seed)
	return pnoise2((val1/sharp) + seed, (val2/sharp) + seed)

def bended2D(*args, **kwargs):
	return noise2D(val1)

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
	return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def random_color():
	r=randint(0,255)
	g=randint(0,255)
	b=randint(0,255)
	return r, g, b
