from manimlib.imports import *
import random




class triangle(Scene):
	def construct(self):
		tt = Title("Sierpinski Triangle")
		tt.set_color(GREEN)
		self.play(Write(tt))
		a = Triangle()
		a.scale(4)
		self.play(Write(a))
		self.play(FadeOut(tt))
		p1 ,p2,p3 =(a.get_points()[0],a.get_points()[3],a.get_points()[7])#0 for 1st , 3 for 2nd and 7 for 3rd vertex
		tit = [p1,p2,p3]
		points=[self.generate_point_in_polygon(p1,p2,p3) for i in range(1)]
		r = Dot(color=RED)
		r.scale(0.4)
		r.move_to(np.array(points[0]))
		self.play(Write(r))
		self.wait()
		y = np.array(points[0])
		X = GREEN
		for i in range(1500):
			ran = random.choice(tit)
			if np.array_equal(ran,tit[0]):
				X = RED
			elif np.array_equal(ran,tit[1]):
				X = BLUE
			else:
				X = YELLOW
			q = Dot(color=X)
			q.scale(0.38)
			new = np.array([(y[0]+ran[0])/2,(y[1]+ran[1])/2,0])
			q.move_to(new)
			self.play(Write(q),run_time=0.06)
			y = new




	def generate_point_in_polygon(self,p1,p2,p3,**kwargs):
		s ,t = sorted([random.random(),random.random()])
		return (s*p1[0] + (t-s)*p2[0] + (1-t)*p3[0] , s*p1[1] + (t-s)*p2[1] + (1-t)*p3[1] , 0)


class square(Scene):
	def construct(self):
		a = Rectangle()
		a.scale(2)
		self.add(a)
		p1 ,p2,p3, p4 =(a.get_points()[0],a.get_points()[4],a.get_points()[8],a.get_points()[12])#0 for 1st , 3 for 2nd and 7 for 3rd vertex
		tit = [p1,p2,p3,p4]
		points=[self.generate_point_in_polygon(p1,p2,p3,p4) for i in range(1)]
		r = Dot(color=RED)
		r.scale(0.25)
		r.move_to(np.array(points))
		self.add(r)
		y = np.array([points])
		ran = p1
		tan = p2
		for i in range(1000):
			#ran = random.choice(tit)
			#tan = random.choice(tit)

			if ran[0]!=tan[0]:
				#ran = random.choice(tit)
				#ran = ranz[0]
				q = Dot(color=GREEN)
				q.scale(0.25)
				new = np.array([(y[0]+tan[0])/2,(y[0]+tan[1])/2,0])
				q.move_to(new)
				self.add(q)
				#tit = []
				#a = np.setdiff1d(points,ran)
				#a = tit
				y = new
				ran = tan
				tan = random.choice(tit)
			else:
				pass


	def generate_point_in_polygon(self,p1,p2,p3,p4,**kwargs):
		s ,t,q = sorted([random.random(),random.random(),random.random()])
		return s*p1[0] + (t-s)*p2[0] + (q-t)*p3[0] + (1-q)*p4[0], s*p1[1] + (t-s)*p2[1] + (q-t)*p3[1] + (1-q)*p4[1] , 0
