from manimlib.imports import *
import random
LIGHT = "#CCFF90"

#BY K.A.Rousan
#https://www.youtube.com/channel/UC5GoG8e7CNCwwgYlh4VyNqA
#Created for 1/2 ratio



class triangle(Scene):#python manim.py Euler_eq.py triangle -ps
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
		r.scale(0.20)
		r.move_to(np.array(points[0]))
		self.play(Write(r))
		self.wait()
		y = np.array(points[0])
		X = GREEN
		for i in range(1000):
			ran = random.choice(tit)
			if np.array_equal(ran,tit[0]):
				X = RED
			elif np.array_equal(ran,tit[1]):
				X = BLUE
			else:
				X = YELLOW
			q = Dot(color=X)
			q.scale(0.15)
			new = np.array([(y[0]+ran[0])/2,(y[1]+ran[1])/2,0])
			q.move_to(new)
			self.play(Write(q),run_time=0.002)
			y = new




	def generate_point_in_polygon(self,p1,p2,p3,**kwargs):
		s ,t = sorted([random.random(),random.random()])
		return (s*p1[0] + (t-s)*p2[0] + (1-t)*p3[0] , s*p1[1] + (t-s)*p2[1] + (1-t)*p3[1] , 0)


class square(Scene):#python manim.py Euler_eq.py square -ps
	def construct(self):
		a = Rectangle()
		a.set_color(GREEN)
		a.scale(2)
		self.add(a)
		p1 ,p2,p3, p4 =(a.get_points()[0],a.get_points()[4],a.get_points()[8],a.get_points()[12])#0 for 1st , 3 for 2nd and 7 for 3rd vertex
		tit = [p1,p2,p3]
		points=[self.generate_point_in_polygon(p1,p2,p3,p4) for i in range(1)]
		r = Dot(color=RED)
		r.scale(0.20)
		r.move_to(np.array(points))
		self.add(r)
		tti = np.array(points[0])
		b = p4
		for i in range(9000):#YELLOW_C,TEAL_C,RED_C
			y = len(tit)-1
			w = random.randint(0,y)
			c = tit[w]
			if np.array_equal(c,tit[0]):
				X = RED
			elif np.array_equal(c,tit[1]):
				X = BLUE
			elif np.array_equal(c,tit[2]):
				X = LIGHT
			else:
				X = YELLOW
			g = Dot(color=X)
			g.scale(0.18)
			new = np.array([(tti[0]+c[0])/2,(tti[1]+c[1])/2,0])
			g.move_to(new)
			#self.add(g)
			self.play(Write(g),run_time=0.001)
			tit.pop(w)
			tit.append(b)
			b = c
			tti = new

	def generate_point_in_polygon(self,p1,p2,p3,p4,**kwargs):
		s ,t,q = sorted([random.random(),random.random(),random.random()])
		return s*p1[0] + (t-s)*p2[0] + (q-t)*p3[0] + (1-q)*p4[0], s*p1[1] + (t-s)*p2[1] + (q-t)*p3[1] + (1-q)*p4[1] , 0


class N_gon(Scene):#Not for Sierpinski Triangle as It follows different logic
	def construct(self):
		self.generate_sierpinski(5,0.17,10000,0.001)
		#self.play(*[FadeOut(mob) for mob in self.mobjects],run_time=0.1)
		#self.generate_sierpinski(6,0.17,10000,0.001)
		#self.play(*[FadeOut(mob) for mob in self.mobjects])
	def generate_sierpinski(self,n,scale_dot,Points_number,time,**kwargs):
		#Generate a polygon using circle
		a = Circle().set_height(FRAME_HEIGHT)
		a.set_color(GREEN)
		a.rotate(90*DEGREES)
		#p is the vertices of the polygon
		p = []
		for i in range(n):
			p.append(a.point_from_proportion(i/n))
		Aust = Polygon(*[p[i] for i in range(n)])
		Aust.set_color(GREEN)
		self.play(Write(Aust))
		#self.add(Aust)

		#choosing a random point in the area of the polygon
		points=[self.generate_points_in_polygon(p) for i in range(1)]
		r = Dot(color=YELLOW_C)
		r.scale(0.20)
		r.move_to(np.array(points))
		self.play(Write(r))
		tti = np.array(points[0])
		b = p[n-1]
		#removing the last term for my algorithm(any element can be removed and it works fine.)
		p.pop(n-1)
		#Choosing a point among the vertex such that no 2 consectuive vertex are same.
		for i in range(Points_number+1):#YELLOW_C,TEAL_C,RED_C
			y = len(p)-1
			w = random.randint(0,y)
			c = p[w]
			g = Dot(color=RED_C)
			g.scale(scale_dot)
			new = np.array([(tti[0]+c[0])/2,(tti[1]+c[1])/2,0])
			g.move_to(new)
			self.play(Write(g),run_time=time)
			p.pop(w)
			p.append(b)
			b = c
			tti = new
	#Choose a point randomly inside the polygon.
	def generate_points_in_polygon(self,p,**kwargs):
		s = []
		for i in range(len(p)-2):
			s.append(random.random())
		s.insert(len(s),1)
		so = 0
		sumx = 0
		sumy = 0
		for i in range(len(p)-1):
			sumx = (s[i]-so)*p[i][0]
			so = s[i]
		for i in range(len(p)-1):
			sumy = (s[i]-so)*p[i][1]
			so = s[i]
		return sumx, sumy ,0
