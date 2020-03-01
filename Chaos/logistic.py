from manimlib.imports import *

def logistic(r,x):
	return r*x*(1-x)
r = 3.5
class logistic_map(MovingCameraScene):
	def func(self,t):
		return np.array([t,logistic(r,t),0])
	def construct(self):
		s = Square(color=YELLOW)
		s.scale(0.5);s.move_to(np.array([0.5,0.5,0]))
		T = Title("Logistic Map");T.set_color(GREEN)
		self.play(Write(T))
		self.wait(2)
		self.play(FadeOut(T))
		x_axis = Line(np.array([-3,0.1,0]),np.array([3,0.1,0]))
		x_axis.set_color(GREEN);x_axis.set_stroke(None,3.1)
		self.play(self.camera_frame.set_width,s.get_width()*1.5,self.camera_frame.move_to,s)
		self.camera_frame.shift(0.015*UP)
		func=ParametricFunction(self.func, t_min=0,t_max=1, fill_opacity=0)
		func.set_color(RED)
		self.play(Write(x_axis))
		self.play(Write(func))
		X = []; Y = []; x0 = 0.1;

		for i in range(60):
			x = x0
			y = logistic(r,x0)
			lin  = Line(np.array([x,x,0]),np.array([x,y,0]),color=BLUE)
			lin1 = Line(np.array([x,y,0]),np.array([y,y,0]),color=BLUE)
			lin.set_stroke(None,1.8); lin1.set_stroke(None,1.8)
			D = Dot(radius=0.006,color=YELLOW)
			D.move_to(np.array([x,y,0]))
			self.play(Write(lin),run_time=0.2)
			self.play(Write(lin1),run_time=0.2)
			self.add(D)
			X.append(x);Y.append(y)
			x0 = y

class bifurcation(MovingCameraScene):
	def construct(self):
		iterations=200000
		r = np.linspace(2.5,4.0,200000)
		N = NumberPlane();self.add(N)
		s = Polygon(np.array([2.5,0,0]),np.array([4,0,0]),np.array([4,1,0]),np.array([2.5,1,0]))
		T = Title("Bifurcation Diagram");T.set_color(GREEN)
		self.play(Write(T))
		self.wait(2)
		self.play(FadeOut(T))
		self.play(self.camera_frame.set_width,s.get_width()*1.5,self.camera_frame.move_to,s)
		self.wait(); x = 0.00001; X=[];dot=[]
		for i in range(iterations):
			x = logistic(r[i],x)
			X.append(x)
			c = Dot(radius=0.00055,color=YELLOW)
			c.move_to(np.array([r[i],x,0]))
			dot.append(c)
		#for j in range(5000):
		#	self.play(Write(dot[i]),run_time=0.005)
		q = VGroup(*[dot[i] for i in range(len(dot))])
		self.add(q)
		self.wait(3)
