from manimlib.imports import *

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
class AM_GM(Scene):
	def construct(self):
		plane = NumberPlane()
		#plane.set_color(YELLOW)
		#self.add(plane)
		Tit= Title("Proof of Arithmetic and Geometric Mean Inequality")
		Tit.set_color(RED)
		self.play(Write(Tit))
		words = TextMobject(
			"""
			`` Two things are Infinite: the Universe and Human stupidity; and I'm not sure about the Universe.''
			""", 
			organize_left_to_right = False
		)
		words.scale(0.75)
		words.set_width(2*(FRAME_X_RADIUS-1))
		words.next_to(Tit,DOWN)
		words.set_color(BLUE)
		author = TextMobject("-Albert Einstein")
		author.set_color(YELLOW)
		author.next_to(words, DOWN)
		author.shift(3*RIGHT)

		self.play(Write(words),run_time=7)
		self.wait()
		self.play(FadeIn(author))
		self.wait(2)
		self.play(FadeOut(words),FadeOut(author))

		proof1 = TextMobject("Proof:")
		proof1.set_color(YELLOW)
		proof1.scale(0.7)
		proof1.move_to(6.5*LEFT+2*UP)
		self.play(Write(proof1))
		main_square = Square(color=PURPLE)
		main_square.scale(2.5)
		main_square.shift(0.7*DOWN+LEFT)
		self.play(Write(main_square))
		p = []
		for i in range(16):
			q=main_square.get_points()[i]
			p.append(q)
		measure_line=Line(p[8],p[4])
		measure=MeasureDistance(measure_line).add_tips()
		measure_tex=measure.get_tex("a+b")
		measure_tex.set_color(GREEN)
		self.play(Write(measure),Write(measure_tex))
		small_rec1 = Polygon(p[14],p[0],p[2],np.array([p[2][0],p[14][1],0]))
		self.play(Write(small_rec1))
		measure_line1=Line(p[14],p[0])
		measure1=MeasureDistance(measure_line1).add_tips()
		measure_tex1=measure1.get_tex("b")
		measure_tex1.set_color(GREEN)
		self.play(Write(measure1),Write(measure_tex1))
		measure_line2=Line(p[0],p[2])
		measure2=MeasureDistance(measure_line2).add_tips()
		measure_tex2=measure2.get_tex("a")
		measure_tex2.set_color(GREEN)
		self.play(Write(measure2),Write(measure_tex2))
		small_rec2 = Polygon(p[14],p[11],p[10],np.array([p[10][0],p[14][1],0]))
		small_rec1_2 = Polygon(p[14],p[0],p[2],np.array([p[2][0],p[14][1],0]))

		tt = TextMobject("Generate 4 copies of The small Rectangle \\\\ Paste them as shown")
		tt.set_color(YELLOW)
		self.play(Write(tt))
		self.play(FadeOut(tt))
		#small_rec1_2.rotate(-PI/2,about_point=p[14])
		small_rec1_2.generate_target()
		small_rec1_2.target.rotate(-PI/2,about_point=p[14])
		self.play(MoveToTarget(small_rec1_2))
		#self.play(Transform(small_rec1.copy(),small_rec2))
		self.wait()

		small_rec2.generate_target()
		small_rec2.target.rotate(-PI/2,about_point=p[10])
		self.play(MoveToTarget(small_rec2))
		measure_line3=Line(p[11],p[7])
		measure3=MeasureDistance(measure_line3).add_tips()
		measure_tex3=measure3.get_tex("a+b")
		measure_tex3.set_color(GREEN)
		self.play(Transform(measure_tex,measure_tex3),Transform(measure,measure3))
		small_rec2.target.rotate(-PI/2,about_point=p[6])
		self.play(MoveToTarget(small_rec2.copy()))
		self.wait()
		x1 = p[2][0]


		Srqa = Polygon(np.array([p[10][0],p[14][1],0]),np.array([p[2][0],p[14][1],0]),np.array([p[9][0],p[6][1],0]),np.array([p[10][0],p[13][1],0]))
		Srqa.set_color(YELLOW)
		self.add(Srqa)
		self.wait()
		measure_line4=Line(np.array([p[10][0],p[14][1],0]),np.array([p[2][0],p[14][1],0]))
		measure4=MeasureDistance(measure_line4).add_tips()
		measure_tex4=measure4.get_tex("a-b")
		measure_tex4.set_color(GREEN)
		self.play(FadeIn(measure4),FadeIn(measure_tex4))


		Area = TextMobject("Area of the big Square:")
		Area.scale(0.7)
		Area.set_color(TEAL_B)
		Area.move_to(np.array([4.5,2,0]))
		self.play(Write(Area))
		Cal = TexMobject("(a+b)^2","=","(a-b)^2","+","4ab")
		Cal.set_color(RED)
		Cal[0].set_color(PURPLE)
		Cal[2].set_color(YELLOW)
		Cal[4].set_color(BLUE)
		Cal.scale(0.9)
		Cal.next_to(Area,DOWN)
		self.play(WiggleOutThenIn(main_square),Write(Cal[0]))
		self.add(Cal[1])
		self.play(WiggleOutThenIn(Srqa),Write(Cal[2]))
		self.add(Cal[3])
		self.play(WiggleOutThenIn(small_rec2),Write(Cal[4]))
		Cal1 = TexMobject("Gives,","(a+b)^2","\\geq","4ab")
		Cal1.set_color(RED)
		Cal1[1].set_color(PURPLE)
		#Cal1[2].set_color(YELLOW)
		Cal1[3].set_color(BLUE)
		Cal1.scale(0.9)
		Cal1.next_to(Cal,DOWN)
		self.play(Write(Cal1))

		Cl = TexMobject("\\frac{a+b}{2}\\geq\\sqrt{ab}")
		Cl.set_color(RED)
		Cl.next_to(Cal,DOWN)
		self.play(Transform(Cal1,Cl))
		self.wait(4)
		#self.play(FadeOut(Cal1),FadeOut(Cl),FadeOut(Srqa),FadeOut())


class Endingsq(Scene):
	def construct(self):
		image1=ImageMobject("AM_GM")
		#image1.opacity(0.4)
		image1.scale(4)
		self.bring_to_back(image1)
		self.play(FadeIn(image1))
		FQQ=TextMobject("Seeing You Next Time,With a new proof of same topic.")
		FQQ.set_color(YELLOW)
	
		self.play(Write(FQQ),run_time=4)
		self.wait()
		EQQ=TextMobject("LIKE--SHARE--SUBSCRIBE")
		EQQ.set_color_by_gradient(RED,GREEN,BLUE,PURPLE)
		self.play(FadeOut(image1))
		self.wait(0.5)
		self.play(Transform(FQQ,EQQ),run_time=3)
		self.wait(2)
