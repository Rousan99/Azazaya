from manimlib.imports import *
import sympy as sp
import math as m

n = 1000
#a=list(sp.primerange(1,n))
#b=np.asarray(a)
#c=np.arange(1,len(b)+1)
#print(b)
class Number(MovingCameraScene):
	def construct(self):
		title = TextMobject("Plot of numbers (r,$\\theta$) when r = $\\theta$")
		title.set_color(YELLOW)
		self.play(Write(title))
		Note = TextMobject("Red ","= Prime Numbers ;","Blue ","= Non-Primes")
		Note.next_to(title,DOWN)
		Note.set_color(GREEN)
		Note[0].set_color(RED)
		Note[2].set_color(BLUE)
		self.play(Write(Note))
		self.play(FadeOut(title),FadeOut(Note))
		q = Square()#height = 2 unit
		factor = (n*np.sin(n)/1.5)-20
		q.scale(factor)
		#self.add(q)
		for i in range(1,n+1):
			x = i*np.cos(i)
			y = i*np.sin(i)
			point = Dot()
			if i <=25:
			    fact = 11
			else:
				fact = np.sqrt(i/1.2)
				point.scale(fact)
			if sp.isprime(i)==True:
				point.set_color(RED)
			else:
				point.set_color(BLUE)
			point.move_to(np.array([x,y,0]))
			self.add(point)
		self.play(self.camera_frame.set_height,q.get_width(),run_time=10)
		self.wait()
