from manimlib.imports import *
from collections import namedtuple
import numpy as np
import math
import random


def rif(r,x0,y0,x,y):
	if x==x0 and y ==y0:
		alpha = 1000
	else:
		dist = pow((x-x0),2)+pow((y-y0),2)
		alpha = (r*r)/dist
	x1 = alpha*(x-x0)+x0
	y1 = alpha*(y-y0)+y0
	position = np.array([x1,y1,0])
	return position
	
class MeasureDistance(VGroup):
	CONFIG = {
		"color":RED_B,
		"buff":0.3,
		"lateral":0.3,
		"invert":False,
		"dashed_segment_length":0.09,
		"dashed":True,
		"ang_arrows":30*DEGREES,
		"size_arrows":0.2,
		"stroke":2.4,
	}
	def __init__(self,mob,**kwargs):
		VGroup.__init__(self,**kwargs)
		if self.dashed==True:
			medicion=DashedLine(ORIGIN,mob.get_length()*RIGHT,dashed_segment_length=self.dashed_segment_length).set_color(self.color)
		else:
			medicion=Line(ORIGIN,mob.get_length()*RIGHT)

		medicion.set_stroke(None,self.stroke)

		pre_medicion=Line(ORIGIN,self.lateral*RIGHT).rotate(PI/2).set_stroke(None,self.stroke)
		pos_medicion=pre_medicion.copy()

		pre_medicion.move_to(medicion.get_start())
		pos_medicion.move_to(medicion.get_end())

		angulo=mob.get_angle()
		matriz_rotacion=rotation_matrix(PI/2,OUT)
		vector_unitario=mob.get_unit_vector()
		direccion=np.matmul(matriz_rotacion,vector_unitario)
		self.direccion=direccion

		self.add(medicion,pre_medicion,pos_medicion)
		self.rotate(angulo)
		self.move_to(mob)

		if self.invert==True:
			self.shift(-direccion*self.buff)
		else:
			self.shift(direccion*self.buff)
		self.set_color(self.color)
		self.tip_point_index = -np.argmin(self.get_all_points()[-1, :])
		

	def add_tips(self):
		linea_referencia=Line(self[0][0].get_start(),self[0][-1].get_end())
		vector_unitario=linea_referencia.get_unit_vector()

		punto_final1=self[0][-1].get_end()
		punto_inicial1=punto_final1-vector_unitario*self.size_arrows

		punto_inicial2=self[0][0].get_start()
		punto_final2=punto_inicial2+vector_unitario*self.size_arrows

		lin1_1=Line(punto_inicial1,punto_final1).set_color(self[0].get_color()).set_stroke(None,self.stroke)
		lin1_2=lin1_1.copy()
		lin2_1=Line(punto_inicial2,punto_final2).set_color(self[0].get_color()).set_stroke(None,self.stroke)
		lin2_2=lin2_1.copy()

		lin1_1.rotate(self.ang_arrows,about_point=punto_final1,about_edge=punto_final1)
		lin1_2.rotate(-self.ang_arrows,about_point=punto_final1,about_edge=punto_final1)

		lin2_1.rotate(self.ang_arrows,about_point=punto_inicial2,about_edge=punto_inicial2)
		lin2_2.rotate(-self.ang_arrows,about_point=punto_inicial2,about_edge=punto_inicial2)


		return self.add(lin1_1,lin1_2,lin2_1,lin2_2)

	def add_tex(self,text,scale=1,buff=-1,**moreargs):
		linea_referencia=Line(self[0][0].get_start(),self[0][-1].get_end())
		texto=TexMobject(text,**moreargs)
		ancho=texto.get_height()/2
		texto.rotate(linea_referencia.get_angle()).scale(scale).move_to(self)
		texto.shift(self.direccion*(buff+1)*ancho)
		return self.add(texto)

	def add_text(self,text,scale=1,buff=0.1,**moreargs):
		linea_referencia=Line(self[0][0].get_start(),self[0][-1].get_end())
		texto=TextMobject(text,**moreargs)
		ancho=texto.get_height()/2
		texto.rotate(linea_referencia.get_angle()).scale(scale).move_to(self)
		texto.shift(self.direccion*(buff+1)*ancho)
		return self.add(texto)

	def add_size(self,text,scale=1,buff=0.1,**moreargs):
		linea_referencia=Line(self[0][0].get_start(),self[0][-1].get_end())
		texto=TextMobject(text,**moreargs)
		ancho=texto.get_height()/2
		texto.rotate(linea_referencia.get_angle())
		texto.shift(self.direccion*(buff+1)*ancho)
		return self.add(texto)

	def add_letter(self,text,scale=1,buff=0.1,**moreargs):
		linea_referencia=Line(self[0][0].get_start(),self[0][-1].get_end())
		texto=TexMobject(text,**moreargs).scale(scale).move_to(self)
		ancho=texto.get_height()/2
		texto.shift(self.direccion*(buff+1)*ancho)
		return self.add(texto)

	def get_text(self, text,scale=1,buff=0.1,invert_dir=False,invert_texto=False,remove_rot=False,**moreargs):
		linea_referencia=Line(self[0][0].get_start(),self[0][-1].get_end())
		texto=TextMobject(text,**moreargs)
		ancho=texto.get_height()/2
		if invert_texto:
			inv=PI
		else:
			inv=0
		if remove_rot:
			texto.scale(scale).move_to(self)
		else:
			texto.rotate(linea_referencia.get_angle()).scale(scale).move_to(self)
			texto.rotate(inv)
		if invert_dir:
			inv=-1
		else:
			inv=1
		texto.shift(self.direccion*(buff+1)*ancho*inv)
		return texto

	def get_tex(self, tex,scale=1,buff=1,invert_dir=False,invert_texto=False,remove_rot=True,**moreargs):
		linea_referencia=Line(self[0][0].get_start(),self[0][-1].get_end())
		texto=TexMobject(tex,**moreargs)
		ancho=texto.get_height()/2
		if invert_texto:
			inv=PI
		else:
			inv=0
		if remove_rot:
			texto.scale(scale).move_to(self)
		else:
			texto.rotate(linea_referencia.get_angle()).scale(scale).move_to(self)
			texto.rotate(inv)
		if invert_dir:
			inv=-1
		else:
			inv=1
		texto.shift(self.direccion*(buff+1)*ancho)
		return texto



class Inversion(Scene):#python manim.py Reflections_On_Pappus.py Inversion -pmr 1080
	def construct(self):
		titlem = Title("Reflection Of Pappus")
		titlem.to_edge(UP)
		titlem.set_color(RED)
		words = TextMobject(
			"""
			`` Mathematics, rightly viewed, possesses not only truth but Supreme beauty...''
			""", 
			organize_left_to_right = False
		)
		words.scale(0.75)
		words.set_width(2*(FRAME_X_RADIUS-1))
		words.next_to(titlem,DOWN)
		words.set_color(BLUE)
		author = TextMobject("-Berlrand Russell")
		author.set_color(YELLOW)
		author.next_to(words, DOWN)
		author.shift(3*RIGHT)
		self.play(GrowFromCenter(titlem))
		self.wait()

		self.play(Write(words),run_time=4)
		self.wait(2)
		self.play(FadeIn(author))
		self.wait(4)
		self.play(Uncreate(words),FadeOut(author),run_time=2)
		self.wait(4)

		plane = NumberPlane()
		#self.add(plane)

		#Suppose we have a circle
		self.wait(7)
		RADIUS=3
		Main_Circle = Circle(radius=RADIUS,color=DARK_BROWN)
		Main_Circle.shift(3*RIGHT+(2*RADIUS/1.6)*LEFT)
		Main_Circle.shift(3.5*RIGHT+0.5*DOWN)
		Main_Circle.set_stroke(None,1.5)
		self.play(Write(Main_Circle),run_time=3)
		self.wait(6)
		#Now we draw it's center and a circle tangent to the big circle.
		center_big = Dot(radius=0.001,color=GREEN)
		center_big.move_to(Main_Circle.get_center())
		self.play(Write(center_big),run_time=2)
		self.wait(2)
		medium_circle=self.tangent_circle_pri(Main_Circle,RIGHT,1,2,RADIUS/1.6,BLUE)
		self.play(Write(medium_circle),run_time=2)
		self.wait(2)
		#Let's draw another circle tangent to the big one and this one on the other side
		self.wait(7)
		self.play(WiggleOutThenIn(Main_Circle),run_time=2)
		self.wait(4)
		self.play(WiggleOutThenIn(medium_circle),run_time=2)
		self.wait(6)
		small_circle = self.tangent_circle_pri(Main_Circle,LEFT,0,2,(RADIUS-RADIUS/1.6),PURPLE)
		self.play(Write(small_circle),run_time=2)
		self.wait(3)


		#In the upper space , we will now draw tangent circles to the 3 main circles.
		self.wait(7)

		color = [MAROON_C,RED_D,TEAL_C,BLUE_C,PURPLE_E,ORANGE,TEAL_A,RED_A]
		circle = []
		for i in range(-21,21):
			c = RADIUS; b = RADIUS/1.6
			a = c-b;
			if i==3:
				q = self.pappus_chain_circle_n(a,b,c,i,1,YELLOW_C)
				circle.append(q)
				self.play(Write(q))
			elif i==-3:
				q = self.pappus_chain_circle_n(a,b,c,i,1,YELLOW_C)
				circle.append(q)
				self.play(Write(q))
			elif i == 0:
				pass
			elif -10<=i<=10:
				q = self.pappus_chain_circle_n(a,b,c,i,1,color[i%3])
				circle.append(q)
				self.play(Write(q),run_time=0.5)
				self.wait()
			else:
				q = self.pappus_chain_circle_n(a,b,c,i,1,color[i%3])
				circle.append(q)
				self.add(q)
		self.wait(9)
		#Now here each colour ful circles is it's number times its diameter
		diameter = Line(np.array([-0.25,-0.5,0]),np.array([5.75,-0.5,0]))
		diameter.set_stroke(None,1.7)
		diameter.set_color(RED)
		self.play(Write(diameter),run_time=2)
		self.wait(3)
		c = RADIUS; b = RADIUS/1.6
		a = c-b
		denominator = (pow((3*a),2)+b*c)
		rn = a*b*c/denominator 
		xn = (-2*b)+((b*c*(b+c))/denominator) ;yn = 2*3*rn

		point1 = Dot(radius=0.05,color=BLUE)
		point1.move_to([xn+3.5,yn-0.5,0])
		point2 = Dot(radius=0.05,color=BLUE)
		point2.move_to([xn+3.5,-0.5,0])

		cir1 = circle[23].copy()
		cir2 = cir1.copy()
		cir3 = cir2.copy()
		self.bring_to_back(cir3)
		self.play(ApplyMethod(cir1.shift,2*rn*DOWN),run_time=2)
		self.wait()
		self.play(ApplyMethod(cir2.shift,4*rn*DOWN),run_time=2)
		self.wait()
		self.play(ApplyMethod(cir3.shift,6*rn*DOWN),run_time=2)
		self.wait()

		self.play(Write(point1),Write(point2),run_time=3)
		ll = Line(point2,point1)
		ll.set_stroke(None,1.7)
		ll.set_color(BLUE)
		self.play(Write(ll),run_time=2)
		self.wait(3)
		measure=MeasureDistance(ll).add_tips()
		measure.set_color(BLUE)
		measure_tex=measure.get_tex("2\\cdot 3\\cdot r")
		measure_tex.set_color(GREEN)
		rad = TextMobject("Where each circle of yellow colour,\\\\has a radius of r.")
		nth = TextMobject("So,For $n^{th}$ circle it is $(2\\cross n\\cross r_n)$.")
		nth.set_color(RED)
		nth.scale(0.8)

		rad.scale(0.75)
		rad.next_to(titlem,DOWN)
		rad.shift(2*DOWN+4*LEFT)
		rad.set_color(BLUE)
		nth.next_to(rad,DOWN)
		self.play(Write(measure),Write(measure_tex),Write(rad),run_time=3)
		self.wait(8)
		self.play(Write(nth),run_time=2)
		self.wait(7)
		#To prove this first we have to understand Circular Inversion.
		self.play(*[Uncreate(i) for i in self.mobjects],run_time=3)
		self.wait(5)










	def tangent_circle_pri(self,objectt,Direction,i,n,RADIUS,COLOUR):
		point = objectt.get_center()
		at_point = objectt.point_from_proportion(i/n)
		dd = Dot(radius=0.0000001)
		dd.move_to(at_point)
		tangent_circle = Circle(radius=RADIUS,color=COLOUR)
		tangent_circle.set_stroke(None,1.5)
		tangent_circle.move_to(point)
		tangent_circle.next_to(dd,Direction,buff=0)
		return tangent_circle




	def pappus_chain_circle_n(self,a,b,c,n,opa,COLOUR):
		denominator = (pow((n*a),2)+b*c)
		xn = (-2*b)+((b*c*(b+c))/denominator) ;
		rn = a*b*c/denominator ;yn = 2*n*rn
		circle = Circle(color=COLOUR,radius=rn,fill_opacity=opa)
		circle.move_to(np.array([xn,yn,0]))
		circle.shift(3.5*RIGHT+0.5*DOWN)
		circle.set_stroke(None,1.5)
		return circle


class Inversion_define(Scene):
	def construct(self):
		Tit = Title("Inversion through a Circle")
		Tit.set_color(RED)
		self.play(Write(Tit),run_time=3)
		#Suppose we have a object, which is kept before a mirror.
		Start = np.array([-4,2,0]); end = np.array([-4,-2,0])
		mirror = Line(Start,end)
		mirror.set_color(YELLOW)
		mirror.set_stroke(None,1.8)
		mid = np.array([-4,0,0])
		objects = Dot(radius=0.1,color=GREEN)
		objects.move_to(np.array([-5,0,0]))
		reflection = objects.copy()
		self.play(FadeIn(mirror),Write(objects),run_time=3)
		self.wait(4)#It's Distance from the mirror is x.
		measure1=MeasureDistance(Line(objects,mid)).add_tips()
		measure1.set_color(BLUE)
		measure_tex1=measure1.get_tex("x")
		measure_tex1.scale(0.7)
		measure_tex1.set_color(GREEN)

		measure2=MeasureDistance(Line(np.array([-3,0,0]),mid)).add_tips()
		measure2.set_color(BLUE)
		measure_tex2=measure2.get_tex("x")
		measure_tex2.scale(0.7)
		measure_tex2.set_color(GREEN)

		self.play(Write(measure1),Write(measure_tex1))
		self.wait(3)
		self.wait(9)#As you know it's reflection will be x unit far from the mirror.
		self.play(ApplyMethod(reflection.move_to,np.array([-3,0,0])),run_time=3)
		self.play(FadeIn(measure_tex2),FadeIn(measure2))
		self.wait(3)

		Tex = TextMobject("So, For Linear mirror \\\\Object Distance = Reflection Distance(w.r.t mirror).")
		Tex.next_to(reflection)
		Tex.scale(0.7)
		Tex.shift(0.4*LEFT)
		Tex.set_color(YELLOW)
		self.play(Write(Tex),run_time=3)
		self.wait(10)
		group = VGroup(mirror,objects,reflection,measure1,measure2,measure_tex1,measure_tex2,Tex)
		#Now what will happen if it's a spherical mirror?
		self.play(*[FadeOut(i) for i in group])
		self.wait(3)

		#Suppose we have a circular mirror(blue one)

		circle = Circle(radius=3,color=BLUE)
		circle.shift(3*LEFT+0.5*DOWN)
		self.play(Write(circle),run_time=3)
		self.wait(3)
		point = Dot(radius=0.05,color=GREEN)
		origin = circle.get_center()
		point.move_to(origin)
		#Let's Draw its center
		self.play(Write(point),run_time=2)
		self.wait(3)

		#Now let's place a particle inside it.
		Patricle = Dot(radius=0.05,color=PURPLE)
		Patricle.move_to([-1,-1,0])
		self.play(Write(Patricle),run_time=2)
		#It's radius is R.
		self.wait(6)

		measure3=MeasureDistance(Line(np.array([-6,-0.7,0]),origin+np.array([0,-0.2,0]))).add_tips()
		measure3.set_color(RED)
		measure_tex3=measure3.get_tex("R")
		measure_tex3.scale(0.7)
		measure_tex3.set_color(YELLOW)
		self.play(Write(measure_tex3),Write(measure3),run_time=3)
		self.wait(3)

		#NOW AS YOU CAN SEE THE REFLECTION OF THE PARTICLE WILL BE THERE.

		reflection = Patricle.copy()

		self.play(ApplyMethod(reflection.move_to,rif(3,origin[0],origin[1],-1,-1)),run_time=2)
		self.wait(5)
		#Let's name things for better understanding
		Names = TexMobject("O","P_1","P_2")
		Names.set_color(GREEN)
		Names.scale(0.7)
		Names[0].next_to(origin,UP,buff=SMALL_BUFF)
		Names[0].shift(0.1*RIGHT)
		Names[1].next_to(Patricle,UP,buff=SMALL_BUFF)
		Names[2].next_to(reflection,UP,buff=SMALL_BUFF)
		self.play(Write(Names),run_time=2)
		self.wait(6)
		#NOW LETS JOIN O,P1 AND P2


		OP1 = Line(origin,Patricle)
		OP2 = Line(origin,reflection)
		GG = VGroup(OP1,OP2)
		GG.set_stroke(None,1.5)
		GG.set_color(RED)
		self.bring_to_back(GG)
		reflection.shift(DOWN*0.01)
		self.remove(reflection)
		self.add(reflection)


		self.play(Write(GG),run_time=2)
		self.wait(4)
		Formula = TextMobject("Here Inversion is defined as\\\\ $OP_1\\cross OP_2 = R^2$")
		Formula.scale(0.7)
		Formula.set_color(BLUE)
		Formula.move_to(np.array([4,2,0]))
		self.play(Write(Formula),run_time=2)
		self.wait(7)
		#So, Using this we find where a point's inversion will go.

		before = TextMobject("Before moving on\\\\ let's find some properties.")
		before.scale(0.65)
		before.next_to(Formula,DOWN)
		before.set_color(GREEN)
		self.play(Write(before),run_time=2)
		self.wait(4)
		self.play(*[FadeOut(i) for i in self.mobjects])
		self.wait(3)
		#Let's see for a whole bunch of points where they land.
		self.wait(4)
		circle = Circle(color=BLUE)
		circle.set_stroke(None,1.5)
		self.play(Write(circle),run_time=3)
		self.wait()
		er = []
		cood = []
		for i in range(100):
			sign1 = random.choice([-1,1])
			sign2 = random.choice([-1,1])
			x = sign1*random.random()
			y = sign2*random.random()
			position = np.array([x,y,0])
			cood.append(position)
			q = Dot(radius=0.02)
			q.move_to(position)
			if x*x+y*y<=1:
				q.set_color(YELLOW)
			else:
				q.set_color(RED)
			er.append(q)
			self.play(Write(q),run_time=0.01)
		self.wait(10)
		#We place points on the plane such that points inside the circle are yellow and outside are red
		#Now let's find the inverse of all points
		self.wait(5)
		for i in range(100):
			pp = rif(1,0,0,cood[i][0],cood[i][1])
			self.play(ApplyMethod(er[i].move_to,pp,run_time=0.20))
		self.wait(4)
		#So, you see all points inside of circle goes outside, all of outside comes inside and points on the circle stays there.
		self.wait(10)
		Plane = NumberPlane(color=YELLOW)
		#self.add(Plane)
		TT = TextMobject("Points inside the circle goes outside\\\\Points outside of circle comes inside \\\\and points on the boundary stays there.")
		TT.set_color(PURPLE)
		TT.move_to(np.array([-4,-2,0]))
		TT.scale(0.65)
		self.play(Write(TT),run_time=3)
		self.wait(5)

		self.remove(*[er[i] for i in range(100)])
		self.play(FadeOut(TT),run_time=3)
		self.wait(3)
		self.play(ApplyMethod(circle.scale,2),run_time=2)
		self.wait(3)
		#Notice for a circle with tangent with the big circle and which touches the origin
		self.wait(5)
		Text = TexMobject("OP_2 = \\frac{R^2}{OP_1} =\\lim_{OP_1\\to 0}\\frac{R^2}{OP_1}=\\infty}")
		Text.set_color(RED)
		Text.scale(0.75)
		Text.move_to(np.array([-4,2.5,0]))
		small_circle = Circle(radius=1,color=YELLOW)
		small_circle.shift(RIGHT)
		small_circle.set_stroke(None,1.6)
		self.play(Write(small_circle),run_time=2)
		self.wait(3)
		pp = Dot(radius=0.08)
		pp.set_color(MAROON_C)
		pp.move_to(circle.get_center())
		self.wait(10)
		#For this point
		self.play(Write(pp))
		self.play(WiggleOutThenIn(pp),run_time=3)
		self.remove(pp)
		self.play(Write(Text),run_time=2)
		self.wait(3)
		#So, it will go to infinity.
		pp1 = Dot(radius=0.08)
		pp1.set_color(MAROON_C)
		pp1.move_to(np.array([2,0,0]))
		self.play(Write(pp1))
		#For this one
		self.wait(2)
		self.play(WiggleOutThenIn(pp1),run_time=2)
		#It stays there as
		Text1 = TexMobject("OP_2 = \\frac{R^2}{OP_1} =\\frac{R^2}{R}=R")
		Text1.set_color(RED)
		Text1.scale(0.75)
		Text1.move_to(np.array([-4,2.5,0]))
		self.play(Transform(Text,Text1),run_time=2)
		self.wait(5)
		self.remove(Text,pp1)
		self.wait(3)
		self.play(small_circle.apply_function,lambda p: rif(2,0,0,p[0],p[1]),run_time=0.1)
		self.wait(3)
		#So circles which are tangent to the circle of inversion and goes through the inversion circle's center will be converted into a straight line,tangent to the circle of inversion.
		self.wait(5)
		ty = TextMobject("So Circles which are tangent to the circle of inversion \\\\and goes through the inversion circle's center will be \\\\converted into a straight line,tangent to the circle of inversion.")
		ty.set_color(GREEN)
		ty.scale(0.65)
		ty.move_to(np.array([-2.5,2.5,0]))
		self.play(Write(ty),run_time=3)
		self.wait(5)
		self.wait(5)
		self.wait(4)
		#Let's see few more examples
		self.play(Uncreate(small_circle),FadeOut(ty))
		ss_circle = Circle(radius=0.66,color=RED,fill_opacity=1)
		self.bring_to_back(ss_circle)
		ss_circle.move_to(np.array([-1,1,0]))
		self.play(Write(ss_circle),run_time=2)
		self.wait(8)
		self.play(WiggleOutThenIn(ss_circle),run_time=2)
		self.wait(10)
		self.play(ss_circle.apply_function,lambda p: rif(2,0,0,p[0],p[1]),run_time=3)
		self.wait(5)
		TDTFT = TextMobject("So, In circular Inversion circles invert to circles .\\\\It will only be a straight-line,\\\\If It goes through the origin.")
		TDTFT.scale(0.65)
		TDTFT.next_to(ss_circle,DOWN)
		TDTFT.shift(3*DOWN)
		TDTFT.set_color(YELLOW)
		self.play(Write(TDTFT),run_time=4)
		self.wait(6)

		yy = TextMobject("Let's end the property view by seeing\\\\the transformation of the whole plane.")
		yy.next_to(ss_circle,DOWN)
		yy.shift(3*DOWN)
		yy.scale(0.73)
		yy.set_color(RED)
		self.play(Transform(TDTFT,yy),run_time=3)
		self.wait(3)
		self.play(*[Uncreate(i) for i in self.mobjects],run_time=2)
		self.wait(2)
		Plane1 = NumberPlane()
		Plane1.set_color_by_gradient(RED,BLUE,GREEN,YELLOW,GREEN,BLUE,RED)
		self.play(Write(Plane1),run_time=2)
		self.wait(4)
		Plane1.prepare_for_nonlinear_transform()
		self.play(Plane1.apply_function,lambda p:rif(3,0,0,p[0],p[1]),run_time=3)
		self.wait(5)
		#Now's we are ready to solve our problem
		self.wait(3)
		self.play(*[Uncreate(i) for i in self.mobjects],run_time=2)
		self.wait(3)


class Solution(Scene):
	def construct(self):
		titlem = Title("Reflection Of Pappus")
		titlem.to_edge(UP)
		titlem.set_color(RED)
		self.add(titlem)
		self.wait()
		RADIUS=3
		Main_Circle = Circle(radius=RADIUS,color=DARK_BROWN)
		Main_Circle.shift(3*RIGHT+(2*RADIUS/1.6)*LEFT)
		Main_Circle.shift(3.5*RIGHT+0.5*DOWN)
		Main_Circle.set_stroke(None,1.7)
		self.add(Main_Circle)
		medium_circle=self.tangent_circle_pri(Main_Circle,RIGHT,1,2,RADIUS/1.6,GREEN)
		self.play(Write(medium_circle))
		small_circle = self.tangent_circle_pri(Main_Circle,LEFT,0,2,(RADIUS-RADIUS/1.6),PURPLE)
		self.play(Write(small_circle))
		self.wait(2)
		color = [MAROON_C,RED_D,TEAL_C,BLUE_C,PURPLE_E,ORANGE,TEAL_A,RED_A]
		circle = []
		for i in range(-21,22):
			c = RADIUS; b = RADIUS/1.6
			a = c-b;
			if i==3:
				q = self.pappus_chain_circle_n(a,b,c,i,1,YELLOW_C)
				circle.append(q)
				self.play(Write(q))
			elif i==-3:
				q = self.pappus_chain_circle_n(a,b,c,i,1,YELLOW_C)
				circle.append(q)
				self.play(Write(q))
			elif i == 0:
				pass
			elif -10<=i<=10:
				q = self.pappus_chain_circle_n(a,b,c,i,1,color[i%3])
				circle.append(q)
				self.play(Write(q),run_time=0.1)
				self.wait()
			else:
				q = self.pappus_chain_circle_n(a,b,c,i,1,color[i%3])
				circle.append(q)
				self.add(q)
		self.wait(9)
		#Now here each colour ful circles is it's number times its diameter
		diameter = Line(np.array([-0.25,-0.5,0]),np.array([5.75,-0.5,0]))
		diameter.set_stroke(None,1.7)
		diameter.set_color(RED)
		self.add(diameter)
		self.wait(3)
		pp = NumberPlane()
		#self.add(pp)
		Algorithm1 = TextMobject("1. Take the yellow point as the Center of Inversion\\\\i.e., center of the inversion circle.")
		Algorithm2 = TextMobject("2.The circle of inversion is chosen such that \\\\it is orthogonal with the $n^{th}$ circle.")
		Algorithm3 = TextMobject("3.Now Invert all the preceding (n-1) circles of the\\\\ chain one after another and also the small purple circle.")
		Algorithm = VGroup(Algorithm1,Algorithm2,Algorithm3)
		Algorithm.scale(0.6)
		Algorithm3.scale(0.8)
		Algorithm.set_color(YELLOW)
		Algorithm[0].next_to(titlem,DOWN)
		Algorithm[0].shift(3.5*LEFT)
		Algorithm[1].next_to(Algorithm[0],DOWN)
		Algorithm[1].shift(0.5*LEFT)
		Algorithm[2].next_to(Algorithm[1],DOWN)



		Main_Circle_copy = Main_Circle.copy()
		Main_Circle_copy.shift(LEFT*RADIUS)
		self.wait(14)
		ori = Main_Circle_copy.get_center()
		origin = Dot(radius=0.05,color=YELLOW)
		origin.move_to(ori)
		self.play(Write(origin),run_time=2)
		self.wait(5)
		#Now we will see a number of steps to proceed.
		self.wait(5)
		self.play(Write(Algorithm[0]),run_time=2)
		self.wait(4)
		self.play(Write(Algorithm[1]),run_time=2)
		self.wait(4)
		self.play(Write(Algorithm[2]),run_time=2)
		self.wait(7)
		# For our case we take n = 2, so, our circle of interest is this one
		self.play(WiggleOutThenIn(circle[23]))
		self.wait(2)
		self.play(WiggleOutThenIn(circle[23]))
		self.wait(4)
		#Now let's draw the circle of inversion. Remember it's center is the Left most yellow point and it must be perpendicular with the yellow circle.
		self.wait(10)
		c = RADIUS; b = RADIUS/1.6; a = c-b;
		denominator = (pow((3*a),2)+b*c)
		x3 = (-2*b)+((b*c*(b+c))/denominator);
		r3 = a*b*c/denominator ;
		invert_of_big = Line(np.array([x3-r3,-FRAME_Y_RADIUS,0]),np.array([x3-r3,FRAME_Y_RADIUS,0]))
		invert_of_big.shift(3.5*RIGHT)
		invert_of_big.set_color(DARK_BROWN)
		invert_of_big.set_stroke(None,1.7)
		qwe=Main_Circle.copy()
		radd = np.sqrt((ori[0]-(x3+3.5))**2+(ori[1]-1.9)**2)
		print(ori)
		print(radd)
		inversion_circle = Circle(radius=radd-0.16,color=GREEN)
		inversion_circle.set_stroke(None,1.7)
		inversion_circle.move_to(ori)
		self.play(Write(inversion_circle),run_time=2)
		self.wait(4)
		#As you can see this is the circle. Now if we Invert the big brown circle,then it will become a straightline as it touches the center of inversion
		self.play(Flash(origin),color=YELLOW)
		self.wait(2)
		#And when it will invert it the points where the Brown and GReen circle touvhes will be fixed. so we get
		self.wait(12)

		Main_Circle_copy.shift(RIGHT*RADIUS)
		self.play(Transform(qwe,invert_of_big))
		self.wait(5)

		invert_of_middle = Line(np.array([x3+r3,-FRAME_Y_RADIUS,0]),np.array([x3+r3,FRAME_Y_RADIUS,0]))
		invert_of_middle.shift(3.5*RIGHT)
		invert_of_middle.set_color(GREEN)
		invert_of_middle.set_stroke(None,1.7)
		qwee=medium_circle.copy()
		#Similarly for medium one
		self.play(Transform(qwee,invert_of_middle))
		self.wait(5)


		#Now we invert all the circles of the chain before yellow one that is 
		self.play(WiggleOutThenIn(circle[22]),WiggleOutThenIn(circle[21]),WiggleOutThenIn(small_circle),run_time=2)
		self.wait(5)
		self.play(circle[22].copy().apply_function,lambda p:rif(radd-0.16,ori[0],ori[1],p[0],p[1]),run_time=2)
		self.wait()
		self.play(circle[21].copy().apply_function,lambda p:rif(radd-0.16,ori[0],ori[1],p[0],p[1]),run_time=2)
		self.wait()
		self.play(small_circle.copy().apply_function,lambda p:rif(radd-0.16,ori[0],ori[1],p[0],p[1]),run_time=2)
		self.wait(5)
		self.play(FadeOut(inversion_circle),run_time=2)
		#Beacuse the lines have a distance of the diameter of the nth circle, all circles inverted to same size
		self.wait(10)
		FGH = TextMobject("As there are (n-1) chain circles and 1 Extra circle.\\\\so $y_n = n\\cross d_n = 2n \\cross r_n$ ($d_n$= diameter of the $n^{th}$ circle).")
		FGH.set_color(BLUE)
		FGH.next_to(Algorithm3,DOWN)
		FGH.scale(0.6)
		FGH.shift(2*DOWN+RIGHT*0.5)
		self.play(Write(FGH),run_time=5)
		self.wait(10)#similarly you can find expresssion for X coordinate and radius. 
		self.wait(3)

		self.play(*[ShrinkToCenter(i) for i in self.mobjects],run_time=2)
		self.wait(5)









	def tangent_circle_pri(self,objectt,Direction,i,n,RADIUS,COLOUR):
		point = objectt.get_center()
		at_point = objectt.point_from_proportion(i/n)
		dd = Dot(radius=0.0000001)
		dd.move_to(at_point)
		tangent_circle = Circle(radius=RADIUS,color=COLOUR)
		tangent_circle.set_stroke(None,1.5)
		tangent_circle.move_to(point)
		tangent_circle.next_to(dd,Direction,buff=0)
		return tangent_circle


	def pappus_chain_circle_n(self,a,b,c,n,opa,COLOUR):
		denominator = (pow((n*a),2)+b*c)
		xn = (-2*b)+((b*c*(b+c))/denominator) ;
		rn = a*b*c/denominator ;yn = 2*n*rn
		circle = Circle(color=COLOUR,radius=rn,fill_opacity=opa)
		circle.move_to(np.array([xn,yn,0]))
		circle.shift(3.5*RIGHT+0.5*DOWN)
		circle.set_stroke(None,1.5)
		return circle


class Endingsq(Scene):
	def construct(self):
		FQQ=TextMobject("If you want things related to this comment below. \\\\Seeing You Next Time---By AzavZya")
		FQQ.set_color_by_gradient(RED,GREEN,BLUE,PURPLE)
		self.play(Write(FQQ),run_time=2)
		self.wait(10)




class Check(Scene):
	def construct(self):
		dd = CheckeredCircle()
		self.add(dd)






