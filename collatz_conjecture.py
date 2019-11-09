from manimlib.imports import *
#By K.A.Rousan




def colz(n):
	if n%2==0:
		col = int(n/2)
	else:
		col = ((3*n)+1)/2
	return col
class Collatz_con(MovingCameraScene):
	def construct(self):
		tt = Title("Collatz Conjecture")
		tt.set_color(YELLOW)
		self.play(Write(tt))
		self.play(FadeOut(tt),run_time=0.1)
		seq = []
		s = 1
		f = 1
		a = 0
		ia = 8.5944
		x = 0
		y = 0.2
		M = []
		NUMBER = 1000
		#r = 1
		iniposi = [2,-2,0]
		incre = [x,y,0]
		newpos = [iniposi[0]+incre[0],iniposi[1]+incre[1],0]
		for n in range(1,NUMBER+1):
			while (n!=1):
				col = colz(n)
				seq.append(col)
				n = col
			#seq.append(1)
			seq.reverse()
			for i in seq:
				if i%2==1:
					q = Line(iniposi,newpos,stroke_width=1.2,opacity=0.7)
					q.set_color(RED)
					a = a-ia
					q.rotate((a)*DEGREES,about_point=iniposi)
					self.play(Write(q),run_time=0.0007)
					iniposi = q.get_end()
					newpos = [iniposi[0]+incre[0],iniposi[1]+incre[1],0]
					M.append(q)

				else:
					w = Line(iniposi,newpos,stroke_width=1.2,opacity=0.7)
					w.set_color(BLUE)
					a = a+ia
					w.rotate((a)*DEGREES,about_point=iniposi)
					self.play(Write(w),run_time=0.0007)
					iniposi = w.get_end()
					newpos = [iniposi[0]+incre[0],iniposi[1]+incre[1],0]
					M.append(w)
			n = VGroup(*[M[i] for i in range(len(M))])
			a = 0
			iniposi = [2,-2,0]
			incre = [x,y,0]
			newpos = [iniposi[0]+incre[0],iniposi[1]+incre[1],0]
			seq = []
		self.wait(2)
		self.play(self.camera_frame.set_height,n.get_width()*2,run_time=3)
		self.wait()
