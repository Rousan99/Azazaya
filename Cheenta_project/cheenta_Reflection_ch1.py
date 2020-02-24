from manimlib.imports import *
from Austin_new.Reflections_On_Pappus import*


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

class OpeningScene(Scene):
	def func(self,t):
		return np.array([t*t-0.5,1.4*t,0])
	def construct(self):
			dot = Dot()
			dot_end = Dot()
			plane = NumberPlane()
			plane.set_color_by_gradient(YELLOW,ORANGE,GREEN)
			self.add(plane)

			square = Square()
			self.wait(1)
			self.add(dot)
			self.wait(0.1)
			q = []; c=[]
			for k in range(1,4):
				triangle = Polygon(k*np.array([1, 0, 0]),
								   k*np.array([0, 1, 0]),
								   k*np.array([1, 1, 0]))
				self.play(Transform(dot, triangle))
				self.add(triangle)
				q.append(triangle)
				triangle = Polygon(k * np.array([0, -1, 0]),
								   k * np.array([1, 0, 0]),
								   k * np.array([1, -1, 0]))
				self.play(Transform(dot, triangle))
				self.add(triangle)
				q.append(triangle)
				triangle = Polygon(k*np.array([-1, 0, 0]),
								   k*np.array([0, -1, 0]),
								   k*np.array([-1, -1, 0]))
				self.play(Transform(dot, triangle))
				self.add(triangle)
				q.append(triangle)
				triangle = Polygon(k*np.array([0, 1, 0]),
								   k*np.array([-1, 0, 0]),
								   k*np.array([-1, 1, 0]))
				self.play(Transform(dot, triangle))
				self.add(triangle)
				q.append(triangle)
				self.wait(0.1)



			for k in range(1,4):
				circle = Circle(radius=k)
				circle.set_fill(GREEN, opacity=0.2)
				self.play(Transform(dot, circle))
				self.add(circle)
				self.play(Transform(dot, dot_end))
				self.wait(0.1)
				c.append(circle)
			self.wait(0.2)
			group = VGroup(*[q[i] for i in range(len(q))],*[c[i] for i in range(len(c))])
			self.play(group.apply_function,lambda p:rif(2,0,0,p[0],p[1]),run_time=2)
			self.play(*[FadeOut(i) for i in self.mobjects])
			
			func=ParametricFunction(self.func, t_min=-TAU,t_max=TAU, fill_opacity=0)
			func.set_color_by_gradient(BLUE, RED)
			self.play(Write(func))
			self.play(func.apply_function,lambda p:rif(1,0,0,p[0],p[1]),run_time=2)
			self.play(*[FadeOut(i) for i in self.mobjects])
			Plane1 = NumberPlane()
			Plane1.set_color_by_gradient(RED,BLUE,GREEN,YELLOW,GREEN,BLUE,RED)
			self.add(Plane1)
			self.wait()
			Plane1.prepare_for_nonlinear_transform()
			self.play(Plane1.apply_function,lambda p:rif(3,0,0,p[0],p[1]),run_time=2)
			self.wait(10)
			img1 = ImageMobject("cheenta1")
			img1.scale(2)
			img1.shift(3.5*LEFT+2*UP)
			img2 = ImageMobject("cheenta2")
			img2.scale(2)
			img2.next_to(img1,RIGHT)
			img3 = ImageMobject("cheenta3")
			img3.scale(2)
			img3.next_to(img1,DOWN)
			img3.shift(2*RIGHT)

			self.add(img1,img2,img3)
			self.wait(10)


class Introduction(Scene):
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
		#So, Using this we find where a point's inversion will go.
		self.wait(5)
		things1 = TextMobject("Remember $P_1$ and $P_2$ are colinear.")
		things1.scale(0.6)
		things1.set_color(YELLOW)
		things1.next_to(Formula,DOWN)
		self.add(things1)
		self.wait(9)

class Propterties(MovingCameraScene):
	def construct(self):
		Tit = Title("Region and Length")
		Tit.set_color(RED)
		self.play(Write(Tit),run_time=3)
		self.wait(2)
		#Let's begin by taking a circle at origin, which is our circle of inversion and it's radius is r
		self.wait(8)
		circle_of_inversion = Circle(color=BLUE,radius=2)
		self.play(Write(circle_of_inversion))
		#Now take a point inside the circle
		self.wait(6)
		point = Dot(radius=0.05,color=YELLOW)
		point.move_to(np.array([0.5,0.5,0]))
		self.play(Write(point))
		#for this point op1 = the green line
		ray = Line(ORIGIN,point.get_center())
		ray.set_color(GREEN)
		ray.set_stroke(None,1.7)
		self.play(Write(ray))
		#Now from the formula
		self.wait(4)
		Formula = TexMobject("OP_2=\\frac{R^2}{	OP_1}")
		Formula.set_color(BLUE)
		Formula.scale(0.7)
		Formula.move_to(np.array([3.5,2,0]))
		self.play(Write(Formula))
		Form = TexMobject("OP_1< R")
		Form.set_color(RED)
		Form.scale(0.6)
		Form.align_to(Formula,LEFT)
		Form.shift(1.2*UP)
		self.add(Form)
		#As OP1 is less than Radius
		self.wait(5)
		Form3 = TexMobject("OP_2=\\frac{R^2}{OP_1}>\\frac{R^2}{R}")
		Form3.scale(0.7)
		Form3.set_color(BLUE)
		Form3.next_to(Form,DOWN)
		Form3.align_to(Formula,LEFT)
		self.play(Write(Form3))
		self.wait(7)
		self.play(FadeOut(Tit))
		refPos = rif(2,0,0,0.5,0.5)
		#It's inversion will be out side
		self.wait(2)
		image = point.copy()
		self.play(self.camera_frame.set_height,self.camera_frame.get_width()*0.6,run_time=2)
		self.play(ApplyMethod(image.move_to,refPos),run_time=2)
		rayim = Line(ORIGIN,refPos)
		rayim.set_color(GREEN)
		rayim.set_stroke(None,1.7)
		self.play(Write(rayim))
		#Similarly for a point outside OP2 is greaterthan R so, It's reflection will be outside
		#Let's see for many points
		self.wait(11)
		self.remove(*[i for i in self.mobjects])
		self.add(circle_of_inversion)
		self.wait(4)
		er = []
		cood = []
		for i in range(100):
			sign1 = random.choice([-2,2])
			sign2 = random.choice([-2,2])
			x = sign1*random.random()
			y = sign2*random.random()
			position = np.array([x,y,0])
			cood.append(position)
			q = Dot(radius=0.02)
			q.move_to(position)
			if x*x+y*y<=4:
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
			pp = rif(2,0,0,cood[i][0],cood[i][1])
			self.play(ApplyMethod(er[i].move_to,pp,run_time=0.20))
		self.wait(4)
		#So, you see all points inside of circle goes outside, all of outside comes inside and points on the circle stays there.
		self.wait(10)
		#Notice one thing that for points on the circle perimeter , they keep fixed rto their place.
		self.wait(8)
		Formula = TexMobject("OP_2=\\frac{R^2}{	R}=R")
		Formula.set_color(BLUE)
		Formula.scale(0.7)
		Formula.move_to(np.array([3.5,2,0]))
		self.play(Write(Formula))
		self.wait(3)
		#Now let's see how length changes in inversion.
		self.wait(8)
		self.remove(Formula,*[er[i] for i in range(len(er))])
		self.wait(3)
		center = Dot(radius=0.04,color=PURPLE)
		self.add(center)
		#Suppose we have 2 points a and b
		self.wait(5)
		a = Dot(radius=0.04,color=YELLOW)
		a.move_to(np.array([-1.5,0.5,0]))
		b = Dot(radius=0.04,color=YELLOW)
		b.move_to(np.array([-1,-0.6,0]))
		self.play(Write(a),Write(b))
		#We will find the length between image of  a and b
		lline = Line(a.get_center(),b.get_center())
		lline.set_color(YELLOW)
		lline.set_stroke(None,1.7)
		self.wait(8)
		self.play(Write(lline))
		self.wait(2)
		#a and b's reflection is
		self.wait(6)
		a_img = rif(2,0,0,a.get_center()[0],a.get_center()[1])
		b_img = rif(2,0,0,b.get_center()[0],b.get_center()[1])
		a_re = a.copy(); b_re = b.copy()
		a_re.set_color(GREEN); b_re.set_color(GREEN)
		self.play(ApplyMethod(a_re.move_to,a_img),ApplyMethod(b_re.move_to,b_img),run_time=2)
		self.wait(2)
		self.play(self.camera_frame.set_height,self.camera_frame.get_width()*0.3,run_time=2)
		#Let's name then
		self.wait(3)
		a1 = TexMobject("a"); b1 = TexMobject("b")
		a1.set_color(YELLOW); b1.set_color(YELLOW)
		a2 = TexMobject("\\bar{a}"); b2 = TexMobject("\\bar{b}")
		a2.set_color(GREEN); b2.set_color(GREEN)
		group1 = VGroup(a,b,a_re,b_re)
		group2 = VGroup(a1,b1,a2,b2)
		group2.scale(0.6)
		for i in range(4):
			if i%2==0:
				group2[i].next_to(group1[i],UP,buff=SMALL_BUFF)
			else:
				group2[i].next_to(group1[i],DOWN,buff=SMALL_BUFF)

		self.play(Write(group2),run_time=2)
		self.wait(5)
		#So, we want  to calculate the length bewtween a bar and b bar
		self.wait(9)
		lline_re = Line(a_re.get_center(),b_re.get_center())
		lline_re.set_color(GREEN)
		lline_re.set_stroke(None,1.7)
		self.play(Write(lline_re))
		#To calcuate AB bar with respect to AB, let's join Abar a and Bbar b with the center
		self.wait(8)
		ex1 = Line(ORIGIN,a_re.get_center())
		ex2 = Line(ORIGIN,b_re.get_center())
		ex1.set_color(RED);ex2.set_color(RED)
		ex1.set_stroke(None,1.7);ex2.set_stroke(None,1.7)
		self.play(Write(ex2),Write(ex1))
		self.remove(group1);self.add(group1)
		self.wait(3)
		O = TexMobject("O");O.scale(0.6);O.next_to(center,RIGHT,buff=SMALL_BUFF)
		self.play(Write(O))
		#Now we know from definaion
		self.wait(6)
		formula2 = TexMobject("Oa\\cross O\\bar{a}=Ob\\cross O\\bar{b}=R^2")
		formula2.scale(0.45)
		formula2.set_color(ORANGE)
		formula2.move_to(np.array([2,1.5,0]))
		self.play(Write(formula2))
		self.wait(5)
		#Now as abo and abar b bar o are similar
		self.wait(4)
		triangle1 = Polygon(center.get_center(),a.get_center(),b.get_center())
		triangle2 = Polygon(center.get_center(),a_re.get_center(),b_re.get_center())
		triangle1.set_color(YELLOW)
		triangle2.set_color(GREEN)
		self.play(WiggleOutThenIn(triangle1))
		self.remove(triangle1)
		self.play(WiggleOutThenIn(triangle2))
		self.remove(triangle2)
		self.wait(3)
		formula1 = TexMobject("\\bar{a}\\bar{b}=\\frac{R^2}{Oa\\cross Ob}(ab)")
		formula1.scale(0.5)
		formula1.set_color(ORANGE)
		formula1.move_to(np.array([3,1.5,0]))
		self.play(Transform(formula2,formula1),run_time=2)
		self.wait(10)
		#keep this formula in back of your head. Now let's see another property.
		self.play(*[Uncreate(i) for i  in self.mobjects],run_time=2)
		self.wait(3)

class Propterty2(MovingCameraScene):
	def construct(self):
		self.wait(2)
		Tit = Title("Preservation of Circles")
		Tit.set_color(RED)
		self.play(Write(Tit),run_time=3)
		#Let's draw a circle
		self.wait(5)
		main_Circle = Circle(radius=2,color=BLUE)
		self.play(Write(main_Circle))
		self.wait(3)
		circle1 = Dot(radius=0.4,color=GREEN)
		circle1.move_to(np.array([-1,0.9,0]))
		#Now take a circle inside this circle.
		self.wait(5)
		self.play(FadeIn(circle1))
		self.wait(2)
		#As we remember from the formula that inside region will go outside and the region near center goes far and the region which are far from center goes near perimeter
		self.wait(8)
		#You can see using those 2 dots
		circle2 = Dot(radius=0.06,color=RED)
		circle3 = Dot(radius=0.06,color=YELLOW)
		circle2.move_to(np.array([-0.85,0.65,0]))
		circle3.move_to(np.array([-1.2,1,0]))
		self.play(Write(circle2))
		self.play(Write(circle3))
		self.wait(3)
		group = VGroup(circle1,circle2,circle3)
		circle2_pos = rif(2,0,0,circle2.get_center()[0],circle2.get_center()[1])
		circle3_pos = rif(2,0,0,circle3.get_center()[0],circle3.get_center()[1])
		#Transforming it we see
		self.wait(5)
		self.play(Uncreate(Tit))
		self.play(group.apply_function,lambda p:rif(2,0,0,p[0],p[1]),ApplyMethod(circle2.move_to,circle2_pos),ApplyMethod(circle3.move_to,circle3_pos),run_time=2)
		self.wait(3)
		#So, You see circles transform to circles. But what if it's half inside and half outside?
		self.wait(8)
		self.play(FadeOut(group))
		self.wait(2)
		ss_circle = Circle(radius=0.66,color=RED,fill_opacity=1)
		self.bring_to_back(ss_circle)
		ss_circle.move_to(np.array([-1,1,0]))
		self.play(Write(ss_circle),run_time=2)
		self.wait(4)
		self.camera_frame.save_state()
		self.play(self.camera_frame.set_height,self.camera_frame.get_width()*0.6,run_time=2)
		#For this notice some points are on the perimeter of our original circle.
		self.wait(8)
		#So, as we know they will stay in their place, while outside goes inside and inside goes outside, as shown
		self.wait(10)
		self.play(ss_circle.apply_function,lambda p: rif(2,0,0,p[0],p[1]),run_time=3)
		self.wait(3)
		self.remove(ss_circle)
		self.wait(2)
		#Now what about a circle which touches the origin?
		self.wait(4)


		Text = TexMobject("OP_2 = \\frac{R^2}{OP_1} =\\lim_{OP_1\\to 0}\\frac{R^2}{OP_1}=\\infty}")
		Text.set_color(RED)
		Text.scale(0.75)
		Text.move_to(np.array([-4,2.5,0]))
		small_circle = Circle(radius=1,color=YELLOW)
		small_circle.shift(RIGHT)
		small_circle.set_stroke(None,1.6)
		#Lets draw a circle tangent to the big one and also whic goes from its center
		self.wait(10)
		self.play(Write(small_circle),run_time=2)
		self.wait(3)
		pp = Dot(radius=0.08)
		pp.set_color(MAROON_C)
		pp.move_to(main_Circle.get_center())
		self.wait(10)
		#For this point
		self.wait(3)
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
		ty = TextMobject("So Circles which goes through the inversion circle's center will be \\\\converted into a straight line,tangent to the circle of inversion.")
		ty.set_color(GREEN)
		ty.scale(0.65)
		ty.move_to(np.array([-2.5,2.5,0]))
		self.play(Write(ty),run_time=3)
		self.wait(5)
		#Let's see few more examples
		self.play(Uncreate(small_circle),FadeOut(ty))
		self.wait(10)

		self.play(*[FadeOut(i) for i in self.mobjects])
		self.wait(3)
class Ptolemy_Theorem(MovingCameraScene):
	def construct(self):
		Tit = Title("Ptolemy's Theorem")
		Tit.set_color(RED)
		self.play(Write(Tit),run_time=2)
		self.wait(5)
		#Fist draw a circle
		self.wait(3)
		circle = Circle(radius=2,color=YELLOW)
		self.play(Write(circle))
		self.wait(2)
		#Now draw a inscribed quadrilaterial
		self.wait(5)
		d_pos = circle.point_from_proportion(0)
		d = Dot(radius=0.07,color=BLUE)
		d.move_to(d_pos)
		a_pos = circle.point_from_proportion(1/4)
		a = Dot(radius=0.07,color=BLUE)
		a.move_to(a_pos)
		b_pos = circle.point_from_proportion(6/11)
		b = Dot(radius=0.07,color=BLUE)
		b.move_to(b_pos)
		c_pos = circle.point_from_proportion(9/11)
		c = Dot(radius=0.07,color=BLUE)
		c.move_to(c_pos)
		corners = VGroup(d,a,b,c)
		quadrilaterial = Polygon(*[corners[i].get_center() for i in range(len(corners))])
		quadrilaterial.set_color(ORANGE)
		quadrilaterial.set_stroke(None,1.7)
		self.play(Write(quadrilaterial),run_time=2)
		self.add(corners)
		self.wait(3)
		#Now his theorem says that
		self.wait(5)
		Theorem = TextMobject("The sum of the product of the opposite sides is the Product of the diagonals.")
		Theorem.set_color(GREEN)
		Theorem.scale(0.7)
		Theorem.shift(2.7*DOWN)
		self.play(Write(Theorem))
		self.wait(5)
		d_tex = TextMobject("d")
		a_tex = TextMobject("a")
		b_tex = TextMobject("b")
		c_tex = TextMobject("c")
		names = VGroup(d_tex,a_tex,b_tex,c_tex)
		names.set_color(RED)
		names.scale(0.9)
		d_tex.next_to(d,RIGHT,buff=SMALL_BUFF)
		a_tex.next_to(a,UP,buff=SMALL_BUFF)
		b_tex.next_to(b,LEFT,buff=SMALL_BUFF)
		c_tex.next_to(c,LEFT+DOWN,buff=SMALL_BUFF)
		self.play(Write(names),lag_ratio=0.5)
		self.wait(2)
		theorem = TexMobject("(ad\\cross bc) + (ab \\cross cd) = ac \\cross bd")
		theorem.scale(0.8)
		theorem.next_to(Theorem,DOWN)
		theorem.set_color(YELLOW)
		self.play(Write(theorem),run_time=2)
		self.wait(5)
		#In his original proof ptolemy uses pure euclidian geometry, but we will do that in much more eligent way
		self.wait(8)
		self.play(FadeOut(Tit),FadeOut(Theorem),FadeOut(theorem),run_time=2)
		self.camera_frame.save_state()
		#To begin the prof first we have to find the point of inversion.
		#Here as we have to consider respective length , so we take a as the point of inversion.thought you can take any one of the vertex
		self.wait(15)
		#so, with respect to this 
		self.play(Flash(a,color=RED,flash_radius=0.5))
		self.wait(5)
		self.play(self.camera_frame.set_height,self.camera_frame.get_width()*1.05,run_time=2)
		invertcircle = Circle(radius=4.4,color=PURPLE)
		invertcircle.set_stroke(None,1.5)
		invertcircle.move_to(a_pos)
		self.play(ShowCreation(invertcircle),run_time=2)
		self.wait(3)
		self.play(Restore(self.camera_frame))
		self.wait(2)
		d_rif = rif(4.4,a_pos[0],a_pos[1],d.get_center()[0],d.get_center()[1])
		b_rif = rif(4.4,a_pos[0],a_pos[1],b.get_center()[0],b.get_center()[1])
		c_rif = rif(4.4,a_pos[0],a_pos[1],c.get_center()[0],c.get_center()[1])
		d_re = d.copy(); b_re = b.copy(); c_re = c.copy()
		#Now reflect our yellow circle with the vertex , we get
		self.wait(7)
		self.remove(quadrilaterial)
		ll = Line(np.array([-50,d_rif[1],0]),np.array([50,d_rif[1],0]))
		ll.set_color(YELLOW)
		ll.set_stroke(None,1.6)
		self.play(Transform(circle.copy(),ll),ApplyMethod(d_re.move_to,d_rif),ApplyMethod(b_re.move_to,b_rif),ApplyMethod(c_re.move_to,c_rif),run_time=3)
		self.wait(3)
		d_rif_tex = TexMobject("\\bar{d}")
		b_rif_tex = TexMobject("\\bar{b}")
		c_rif_tex = TexMobject("\\bar{c}")
		rif_tex = VGroup(d_rif_tex,b_rif_tex,c_rif_tex)
		rif_tex.scale(0.85)
		rif_tex.set_color(RED)
		riff = VGroup(d_re,b_re,c_re)
		for i in range(len(riff)):
			rif_tex[i].next_to(riff[i],DOWN,buff=SMALL_BUFF)
		#Let's name the reflected points
		self.wait(5)
		self.play(Write(rif_tex))
		self.wait(3)
		#Now join abb bar , ac c bar and ad d bar
		self.wait(6)
		abb = Line(a.get_center(),b_re.get_center())
		acc = Line(a.get_center(),c_re.get_center())
		add = Line(a.get_center(),d_re.get_center())
		lines = VGroup(abb,acc,add)
		lines.set_stroke(None,1.6)
		lines.set_color(GREEN)
		self.bring_to_back(lines)
		self.play(Write(lines))
		self.wait(3)
		self.camera_frame.save_state()
		self.play(ApplyMethod(self.camera_frame.shift,2.5*RIGHT),run_time=2)
		self.wait(3)
		#from this figure
		self.wait(4)
		cal = TexMobject("\\bar{b}\\bar{c}+\\bar{c}\\bar{d}=\\bar{b}\\bar{d}")
		cal.set_color(RED)
		cal.scale(0.9)
		cal.move_to(np.array([7,3,0]))
		self.play(Write(cal),run_time=2)
		self.wait(3)
		#Now from previous property
		self.wait(5)
		formula1 = TexMobject("\\bar{a}\\bar{b}=\\frac{R^2}{Oa\\cross Ob}(ab)")
		formula1.scale(0.6)
		formula1.set_color(ORANGE)
		formula1.next_to(cal,DOWN)
		self.play(Write(formula1))
		self.wait(4)
		#This one
		self.play(WiggleOutThenIn(formula1))
		self.wait(4)
		self.play(FadeOut(formula1))
		self.wait(3)
		#We get
		self.wait(3)
		call = TexMobject(r"\frac{bc}{(ab\cross ac)} +\frac{cd}{(ac\cross ad)}=\frac{bd}{(ab\cross ad)}")
		call.set_color(BLUE)
		call.scale(0.6)
		call.next_to(cal,DOWN)
		self.play(Write(call),run_time=2)
		self.wait(3)
		#Multiplying both side by ab ac ad
		self.wait(4)
		tt = TextMobject("Multiplying by $(ab\\cross ac \\cross ad)$")
		tt.scale(0.6)
		tt.next_to(call,DOWN)
		self.play(Write(tt))
		self.wait(3)
		#We get
		self.wait(4)
		final = TexMobject("(ad\\cross bc) + (ab \\cross cd) = ac \\cross bd")
		final.next_to(call,DOWN)
		final.set_color(YELLOW)
		final.scale(0.7)
		self.play(Transform(tt,final))
		self.wait(9)
		self.play(*[FadeOut(i) for i in self.mobjects])
		self.play(Restore(self.camera_frame))
		self.wait(3)
		tt6 = TextMobject("In the next video we will learn some other\\\\properties and will solve another problem.")
		tt6.set_color_by_gradient(RED,ORANGE,YELLOW,GREEN,BLUE)
		tt6.shift(2.5*UP)
		self.play(Write(tt6),run_time=2)
		self.wait(8)


