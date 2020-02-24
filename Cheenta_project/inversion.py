from manimlib.imports import *
import numpy as np


def rif(r,x0,y0,x,y):
	if x==x0 and y ==y0:
		radius = 100000000,
	else:
		dist = pow(pow((x-x0),2)+pow((y-y0),2),0.5)
		radius = (r*r)/dist
	ratio = radius/dist
	y1 = y0+ratio*(y-y0)
	x1 = x0+ratio*(x-x0)
	position = np.array([x1,y1,0])
	return position

class Inversion_define(Scene):
	def construct(self):
		rad = 3
		cc = Circle(radius=3,color=BLUE)
		tt = Circle(radius=1.5,color=YELLOW_C)
		tt.shift(1.5*RIGHT)
		r = tt.copy()

		self.add(cc,tt)
		self.play(
			cc.apply_function,lambda p:np.array([rif(rad,0,0,p[0],p[1])[0],rif(rad,0,0,p[0],p[1])[1],0]),tt.apply_function,lambda p:rif(rad,0,0,p[0],p[1]),run_time=5)
		self.wait(3)
