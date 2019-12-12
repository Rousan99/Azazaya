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




class Minkowsli2(Scene):
	def construct(self):
		Text = TextMobject("If $a_1,a_2,..,a_n$ and $b_1,b_2,..,b_n$ are positive Integers,Then")
		Text.set_color(ORANGE)
		Tex = TexMobject("\\sqrt{(\\sum_{i=1}^{n}a_i)^2+(\\sum_{i=1}^{n}b_i)^2}\\leq\\sum_{i=1}^{n}\\sqrt{a_i^2+b_i^2}")
		Tex.set_color(YELLOW)
		plane = NumberPlane()
		#plane.set_color(YELLOW)
		#self.add(plane)
		Tit= Title("Polygonal Path Inequality(Minkowsli's Inequality For p=2)")
		Tit.set_color(RED)
		self.play(Write(Tit))
		Text.next_to(Tit,DOWN)
		self.play(Write(Text))
		Tex.next_to(Text,DOWN)
		self.play(Write(Tex))
		self.wait()
		self.play(FadeOut(Text),FadeOut(Tex))
		Fist = TextMobject("Let's First see it's 2 variable form's Proof.")
		Fist.next_to(Tit,DOWN)
		Fist.set_color(GREEN)
		self.play(FadeIn(Fist))
		self.play(FadeOut(Fist))

		p1 = np.array([-4,-2,0]); p2 = np.array([2,-2,0]); p3 = np.array([2,2,0])
		Triangle = Polygon(p1,p2,p3)
		Triangle.set_color(PURPLE)
		self.play(Write(Triangle),run_time=2.5)

		np1 = np.array([0,-2,0]); np3 = np.array([2,-1,0]); np2 = np.array([2,-2,0]); np4 = np.array([0,-1,0])
		rec1 = DashedLine(np1,np2)
		rec2 = DashedLine(np2,np3)
		rec3 = DashedLine(np3,np4)
		rec4 = DashedLine(np4,np1)
		rec = VGroup(rec1,rec2,rec3,rec4)
		rec.set_color(BLUE)
		self.play(Write(rec),run_time=2)
		self.wait(2)
		measure_line1=Line(np2,np1)
		measure1=MeasureDistance(measure_line1).add_tips()
		measure_tex1=measure1.get_tex("y")
		measure_tex1.set_color(GREEN)

		measure_line2=Line(np3,np2)
		measure2=MeasureDistance(measure_line2).add_tips()
		measure_tex2=measure2.get_tex("u")
		measure_tex2.set_color(GREEN)

		self.play(Write(measure1),Write(measure_tex1),Write(measure2),Write(measure_tex2))
		self.wait(1)

		measure_line3=Line(np1,p1)
		measure3=MeasureDistance(measure_line3).add_tips()
		measure_tex3=measure3.get_tex("x")
		measure_tex3.set_color(GREEN)

		measure_line4=Line(p3,np3)
		measure4=MeasureDistance(measure_line4).add_tips()
		measure_tex4=measure4.get_tex("v")
		measure_tex4.set_color(GREEN)

		self.play(Write(measure3),Write(measure_tex3),Write(measure4),Write(measure_tex4))
		self.wait(1.5)

		point = Dot()
		point.scale(0.85)
		point.move_to(np4)
		point.set_color(GREEN)
		self.play(FadeIn(point))

		Triangle1 = Polygon(np1,np4,p1)
		Triangle1.set_color(YELLOW)
		Triangle1.set_stroke(None,1.5)

		Triangle2 = Polygon(np4,np3,p3)
		Triangle2.set_color(ORANGE)
		Triangle2.set_stroke(None,1.5)

		Linee1 = Line(p1,np4)
		Linee1.set_color(YELLOW)
		Linee2 = Line(np4,p3)
		Linee2.set_color(ORANGE)
		LL = VGroup(Linee2,Linee1)
		self.play(Write(Linee1),Write(Linee2))
		self.wait(1)
		self.play(Write(Triangle1),Write(Triangle2))
		self.play(FadeOut(Linee1),FadeOut(Linee2))
		self.wait(2)

		Names = TexMobject("Q","P","R")
		Names.set_color(BLUE)
		Names.scale(0.87)
		Names[0].move_to(p1)
		Names[0].shift(LEFT*0.2)
		Names[1].move_to(np4)
		Names[1].shift(0.2*DOWN+0.2*RIGHT)
		Names[2].move_to(p3)
		Names[2].shift(UP*0.2)
		self.play(Write(Names))
		self.wait()

		QPo = TextMobject("From This one,")
		QPo.scale(0.75)
		QPo.set_color(BLUE)
		QPo.next_to(Tit,DOWN)
		QPo.shift(LEFT*4.5)
		self.play(Write(QPo),WiggleOutThenIn(Triangle1))
		self.play(WiggleOutThenIn(Triangle1))
		QP = TexMobject("QP=\\sqrt{x^2+u^2}")
		QP.scale(0.8)
		QP.set_color(YELLOW)
		QP.next_to(QPo,DOWN)
		self.play(Write(QP))


		QPp = TextMobject("From This one,")
		QPp.scale(0.75)
		QPp.set_color(BLUE)
		QPp.next_to(QPo,RIGHT)
		QPp.shift(RIGHT*0.8)
		self.play(Write(QPp),WiggleOutThenIn(Triangle2))
		self.play(WiggleOutThenIn(Triangle2))
		PR = TexMobject("PR=\\sqrt{y^2+v^2}")
		PR.scale(0.8)
		PR.set_color(ORANGE)
		PR.next_to(QPp,DOWN)
		self.play(Write(PR))
		self.wait(2)

		QPO = TextMobject("From big-one")
		QPO.scale(0.75)
		QPO.set_color(BLUE)
		QPO.next_to(Tit,DOWN)
		QPO.shift(5*RIGHT)
		self.play(Write(QPO),WiggleOutThenIn(Triangle))
		self.play(WiggleOutThenIn(Triangle))
		QR = TexMobject("QR=\\sqrt{(x+y)^2+(u+v)^2}")
		QR.scale(0.65)
		QR.set_color(ORANGE)
		QR.next_to(QPO,DOWN)
		self.play(Write(QR))
		self.wait(2)
		Conc= TextMobject("From This,")
		Conc.scale(0.75)
		Conc.set_color(GREEN)
		Conc.next_to(QR,DOWN)
		Conc.shift(DOWN*3.7)
		Trianglee = Polygon(p1,np4,p3)
		Trianglee.set_stroke(None,1.5)
		Trianglee.set_color(RED)
		self.play(Write(Conc),WiggleOutThenIn(Trianglee))
		self.wait()
		inq = TexMobject("QP+PR\\geq QR")
		inq.scale(0.75)
		inq.next_to(Conc,DOWN)
		inq.set_color_by_gradient(RED,ORANGE,YELLOW)
		self.play(Write(inq))
		self.wait(2)
		Inequalityy = TexMobject("\\sqrt{x^2+u^2}+\\sqrt{y^2+v^2}\\geq \\sqrt{(x+y)^2+(u+v)^2}")
		Inequalityy.next_to(Conc,DOWN)
		Inequalityy.scale(0.7)
		Inequalityy.shift(2*LEFT)
		Inequalityy.set_color_by_gradient(BLUE,GREEN,YELLOW,ORANGE,RED)
		self.play(Transform(inq,Inequalityy))
		self.wait()
		Rec = SurroundingRectangle(Inequalityy)
		Rec.set_color(BLUE)
		self.play(Write(Rec))
		self.wait(2)



class Minkowsli_n(Scene):
	def construct(self):
		plane = NumberPlane()
		#self.add(plane)
		Tit= Title("Polygonal Path Inequality(Minkowsli's Inequality For p=2)")
		Tit.set_color(RED)
		Tit.scale(0.6)
		Tit.shift(UP*0.5)
		self.play(Write(Tit))
		Fist = TextMobject("Now Let's see the proof for n Integers.")
		Fist.next_to(Tit,DOWN)
		Fist.set_color(GREEN)
		self.play(FadeIn(Fist))
		self.play(FadeOut(Fist))

		origin = np.array([-6,-3,0]); y_max = np.array([-6,3.5,0]); x_max = np.array([1,-3,0]); mirror = np.array([0,3,0])
		x_axis = Line(origin,x_max)
		x_axis.set_stroke(None,1.5)
		x_axis.set_color(GREEN)
		y_axis = Line(origin,y_max)
		y_axis.set_stroke(None,1.5)
		y_axis.set_color(GREEN)
		tan45 = Line(origin,mirror)
		tan45.set_stroke(None,1.6)
		tan45.set_color(RED)
		O = Dot(color=YELLOW)
		O.move_to(origin)
		O.scale(0.8)
		Axis = VGroup(x_axis,y_axis,O)
		self.play(Write(Axis))
		self.wait()
		self.play(Write(tan45))

		p1 = np.array([-5,-3,0]); p2 = np.array([-4,-3,0]); p_n = np.array([-1.5,-3,0]); pn = np.array([0,-3,0])
		q1 = np.array([-6,-2.5,0]); q2 = np.array([-6,-0.5,0]); q_n = np.array([-6,2,0]); qn = np.array([-6,3,0])
		mid1 = np.array([-5,-2.5,0]); mid2 = np.array([-4,-0.5,0]); mid3 = np.array([-1.5,2,0]); mid4 = np.array([0,3,0])


		rec11 = DashedLine(p1,mid1)
		rec12 = DashedLine(q1,mid1)
		p1q1=Dot(color=YELLOW)
		p1q1.scale(0.8)
		p1q1.move_to(mid1)
		recf = VGroup(rec11,rec12)
		recf.set_stroke(None,1.5)
		recf.set_color(BLUE)
		self.play(Write(recf),FadeIn(p1q1))

		measure_linep1=Line(p1,origin)
		measurep1=MeasureDistance(measure_linep1).add_tips()
		measure_texp1=measurep1.get_tex("a_1")
		measure_texp1.scale(0.8)
		measure_texp1.set_color(YELLOW)
		self.play(Write(measurep1),Write(measure_texp1))
		self.wait()

		measure_lineq1=Line(origin,q1)
		measureq1=MeasureDistance(measure_lineq1).add_tips()
		measure_texq1=measureq1.get_tex("b_1")
		measure_texq1.scale(0.8)
		measure_texq1.set_color(YELLOW)
		self.play(Write(measureq1),Write(measure_texq1))
		self.wait(2)



		rec21 = DashedLine(p2,mid2)
		rec22 = DashedLine(q2,mid2)
		p2q2=Dot(color=YELLOW)
		p2q2.scale(0.8)
		p2q2.move_to(mid2)
		recf2 = VGroup(rec21,rec22)
		recf2.set_stroke(None,1.5)
		recf2.set_color(BLUE)
		self.play(Write(recf2),FadeIn(p2q2))

		measure_linep2=Line(p2,p1)
		measurep2=MeasureDistance(measure_linep2).add_tips()
		measure_texp2=measurep2.get_tex("a_2")
		measure_texp2.scale(0.8)
		measure_texp2.set_color(YELLOW)
		self.play(Write(measurep2),Write(measure_texp2))

		measure_lineq2=Line(q1,q2)
		measureq2=MeasureDistance(measure_lineq2).add_tips()
		measure_texq2=measureq2.get_tex("b_2")
		measure_texq2.scale(0.8)
		measure_texq2.set_color(YELLOW)
		self.play(Write(measureq2),Write(measure_texq2))
		self.wait(2)


		Tex = TextMobject("..............")
		Tex.set_color(ORANGE)
		Tex.next_to(x_axis,DOWN)
		Tex.shift(LEFT*0.2)
		self.play(Write(Tex))
		Texx = TextMobject(".........")
		Texx.set_color(ORANGE)
		Texx.rotate(PI/2)
		Texx.next_to(y_axis,LEFT)
		Texx.shift(UP*0.4)
		self.play(Write(Texx))
		self.wait(2)


		midd = np.array([-2,0.5,0])
		pww = np.array([-2,-3,0]); qww = np.array([-6,0.5,0])

		recc = DashedLine(pww,midd)
		reccc = DashedLine(qww,midd)
		pqe=Dot(color=YELLOW)
		pqe.scale(0.8)
		pqe.move_to(midd)
		recf34 = VGroup(recc,reccc)
		recf34.set_stroke(None,1.5)
		recf34.set_color(BLUE)
		self.play(Write(recf34),FadeIn(pqe))


		rec31 = DashedLine(p_n,mid3)
		rec32 = DashedLine(q_n,mid3)
		p3q3=Dot(color=YELLOW)
		p3q3.scale(0.8)
		p3q3.move_to(mid3)
		recf3 = VGroup(rec31,rec32)
		recf3.set_stroke(None,1.5)
		recf3.set_color(BLUE)
		self.play(Write(recf3),FadeIn(p3q3))

		rec41 = DashedLine(pn,mid4)
		rec42 = DashedLine(qn,mid4)
		p4q4=Dot(color=YELLOW)
		p4q4.scale(0.8)
		p4q4.move_to(mid4)
		recf4 = VGroup(rec41,rec42)
		recf4.set_stroke(None,1.5)
		recf4.set_color(BLUE)
		self.play(Write(recf4),FadeIn(p4q4))


		measure_linepn=Line(pn,p_n)
		measurepn=MeasureDistance(measure_linepn).add_tips()
		measure_texpn=measurepn.get_tex("a_n")
		measure_texpn.scale(0.8)
		measure_texpn.set_color(YELLOW)
		self.play(Write(measurepn),Write(measure_texpn))

		measure_lineqn=Line(q_n,qn)
		measureqn=MeasureDistance(measure_lineqn).add_tips()
		measure_texqn=measureqn.get_tex("b_n")
		measure_texqn.scale(0.8)
		measure_texqn.set_color(YELLOW)
		self.play(Write(measureqn),Write(measure_texqn))
		self.wait(2)

		path = VMobject()
		path.set_points_as_corners([origin,mid1,mid2,midd,mid3,mid4])
		path.set_color(YELLOW)
		path.set_stroke(None,1.7)
		self.play(Write(path),run_time=2)
		self.wait(2)

		base1 = np.array([p1[0],q1[1],0]); base2 = np.array([p2[0],q1[1],0]); base3 = np.array([pn[0],q_n[1],0])
		Triangle = VGroup(Polygon(origin,p1,base1),Polygon(mid1,base2,mid2),Polygon(mid3,base3,mid4),Polygon(origin,pn,mid4))
		#Triangle.set_stroke(None,1.5)
		Triangle.set_color(ORANGE)
		#self.play(Write(Triangle))
		Name = TexMobject("O","A","B","C","D")
		Name.scale(0.75)
		Name.set_color(BLUE)
		Name[0].next_to(origin,LEFT)
		Name[0].shift(DOWN*0.3)
		Name[1].next_to(p1q1,DOWN)
		Name[1].shift(UP*0.2)
		Name[2].next_to(p2q2,UP)
		Name[2].shift(DOWN*0.1)
		Name[3].next_to(p3q3,UP)
		Name[3].shift(DOWN*0.1)
		Name[4].next_to(p4q4,RIGHT)
		self.play(Write(Name),run_time=2)
		self.wait(2)
		tt = TexMobject("OA=\\sqrt{a_1^2+b_1^2}","AB=\\sqrt{a_2^2+b_2^2}","CD=\\sqrt{a_n^2+b_n^2}","OD=\\sqrt{(\\sum_{i=1}^{n}a_i)^2+(\\sum_{i=1}^{n}b_i)^2}")
		for i in range(4):
			tt[i].next_to(Tit,DOWN)
			tt[i].shift(3*RIGHT)
		tt.scale(0.7)
		tt.set_color(GREEN)
		tt[1].next_to(tt[0],DOWN)
		tt[2].next_to(tt[1],DOWN)
		tt[3].next_to(tt[2],DOWN)
		for i in range(4):
			self.play(Write(tt[i]),WiggleOutThenIn(Triangle[i]),run_time=1)
			self.play(FadeOut(Triangle[i]))
		self.wait(2)
		Text = TextMobject("$\\to$Straight Line","$\\leq$","Path")
		Text.set_color(BLUE)
		Text.scale(0.8)
		Text.set_stroke(YELLOW)
		Text.next_to(tt[3],DOWN)
		self.play(Write(Text[0]),WiggleOutThenIn(tan45))
		self.add(Text[1])
		self.play(Write(Text[2]),WiggleOutThenIn(path))
		self.wait()
		maineq = TexMobject("\\sqrt{(\\sum_{i=1}^{n}a_i)^2+(\\sum_{i=1}^{n}b_i)^2}\\leq\\sum_{i=1}^{n}\\sqrt{a_i^2+b_i^2}")
		maineq.set_color_by_gradient(RED,ORANGE,YELLOW,GREEN,BLUE)
		maineq.scale(0.65)
		maineq.move_to(DOWN*3+3.9*RIGHT)
		self.play(Write(maineq))
		self.wait(2)


class Endingsq(Scene):
	def construct(self):
		image1=ImageMobject("Path")
		#image1.opacity(0.4)
		image1.scale(4)
		self.bring_to_back(image1)
		self.play(FadeIn(image1))
		self.play(FadeOut(image1))
		FQQ=TextMobject("Seeing You Next Time,With something new.")
		FQQ.set_color(YELLOW)
	
		self.play(Write(FQQ),run_time=4)
		self.wait()
		EQQ=TextMobject("LIKE--SHARE--SUBSCRIBE")
		EQQ.set_color_by_gradient(RED,GREEN,BLUE,PURPLE)
		self.play(Transform(FQQ,EQQ),run_time=3)
		self.wait(2)
