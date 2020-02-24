from manimlib.imports import *


class Intro(GraphScene):
	CONFIG = {
	   "y_min" : -5,
	   "y_max" : 22,
	   "x_min" : -1,
	   "x_max" : 6
	}
	def construct(self):
		Tit = Title("General proof of Power Inequality")
		Tit.set_color(RED)
		self.play(Write(Tit))
		Text = TextMobject("This beautiful inequality says:")
		Text.scale(0.7); Text.set_color(BLUE)
		Text.next_to(Tit,DOWN)
		self.wait(2)
		self.play(Write(Text),run_time=2)
		self.wait(2)
		Form = TexMobject(r"e^A>A^e")
		Form.set_color(YELLOW)
		Form.next_to(Text,DOWN)
		Formcon = TextMobject("; where $e<A$")
		Formcon.set_color(ORANGE)
		Formcon.scale(0.7);Formcon.next_to(Form)
		self.play(Write(Form))
		self.wait(2)
		self.play(Write(Formcon))
		self.wait(5)
		gg = VGroup(Text,Tit)
		ff = VGroup(Form,Formcon)
		self.play(FadeOut(gg))
		self.play(ApplyMethod(ff.shift,1.7*UP+6*LEFT))
		self.wait(3)
		TT = TextMobject("Now we will draw the graph of $y = \\frac{e^x}{e}-1$ and a line at any point A.")
		TT.set_color(BLUE); TT.scale(0.75)
		self.play(Write(TT),run_time=2)
		self.wait(6)
		self.play(Uncreate(TT))
		self.wait(2)

		self.setup_axes(animate=True)
		self.wait(2)
		graph1 = self.get_graph(lambda x: (np.exp(x)/np.exp(1))-1,
										color = GREEN,
										x_min = -1,
										x_max = 6,
										y_max = 22
										)
		plane = NumberPlane()
		p1 = np.array([1,-2.5,0]); p2 = np.array([1,1.25,0])
		graph2 = Line(p1,p2); r1 = 0.07
		d1 = Dot(radius=r1,color=BLUE)
		d1.move_to(p1)
		d2 = Dot(radius=r1,color=BLUE)
		d2.move_to(p2)
		graph2.set_stroke(None,1.7)
		graph2.set_color(RED)
		self.remove(ff)

		self.play(Write(graph1),run_time=2)
		self.wait(3)
		self.play(Write(d1),Write(d2))
		self.wait(2)
		self.play(FadeIn(graph2),run_time=2)
		self.remove(d1,d2); self.add(d1,d2)
		TT = TexMobject("y = \\frac{e^x}{e}-1");TT.scale(0.8);TT.set_color(GREEN)
		TT.next_to(Form,DOWN); TT.shift(4.5*RIGHT+3*DOWN)
		self.play(FadeIn(TT),run_time=1.5)
		self.wait(1.5)
		TT1 = TexMobject("\\frac{A}{e}");TT1.scale(0.8);TT1.set_color(RED);TT1.next_to(d1,DOWN)
		self.play(Write(TT1))

		graph4 = self.get_graph(lambda x: (np.exp(x)/np.exp(1))-1,
										color = GREEN,
										x_min = 1,
										x_max = 6,
										y_max = 22
										)
		p3 = graph4.points[0]
		d3 = Dot(radius=r1,color=BLUE);d3.move_to(p3)
		self.play(Write(d3))
		self.wait(2)
		TT2 =TexMobject("(1,0)");TT2.scale(0.8);TT2.set_color(RED)
		TT2.next_to(d3,DOWN);self.play(Write(TT2))
		self.wait(4)
		rects = self.get_riemann_rectangles(graph1,x_min=1,x_max=3.9)
		rects.set_stroke(PURPLE, width = 0.0001)
		WW = TextMobject("Now we know area of \\\\this region is : ")
		WW.set_color(PURPLE);WW.scale(0.8); WW.shift(2*UP+5*RIGHT)
		self.play(Write(WW))
		self.wait(2)
		self.play(Write(rects),run_time=3)
		self.wait(4)
		Form = TexMobject("\\Delta","=","\\int_{1}^{\\frac{A}{e}}(\\frac{e^x}{e}-1)dx")
		Form.set_color(BLUE);Form.next_to(WW,DOWN)
		Form[0].set_color(GREEN);Form[1].set_color(YELLOW)
		Form.shift(0.5*LEFT)
		self.play(Write(Form))
		self.wait(6)
		Form1 = TexMobject("=\\frac{e^\\frac{A}{e}}{e}-\\frac{A}{e}")
		Form1.set_color(BLUE);Form1.next_to(Form[1],DOWN)
		Form1.shift(1.5*RIGHT+0.4*DOWN)
		self.play(Write(Form1),run_time=2)
		self.wait(9)
		Now = TextMobject("$0<\\Delta$","; As you see Area is \\\\positive.")
		Now.set_color(RED);Now.scale(0.77);Now[0].set_color(YELLOW)
		Now.shift(2*UP+4*RIGHT)
		self.play(Transform(WW,Now),FadeOut(Form),ApplyMethod(Form1.shift,UP))
		self.wait(8)
		Form2 = TexMobject("0<\\frac{e^\\frac{A}{e}}{e}-\\frac{A}{e}");Form2.set_color(PURPLE)
		Form2.next_to(Form[1],DOWN)
		Form2.shift(1.5*RIGHT+0.4*DOWN+UP)
		self.play(Transform(Form1,Form2))
		self.wait(5)
		Whicj = TexMobject("A^e<e^A")
		Whicj.set_color_by_gradient(RED,YELLOW,GREEN,BLUE)
		Whicj.next_to(Form[1],DOWN)
		Whicj.shift(1.5*RIGHT+0.4*DOWN+UP)
		self.play(Transform(Form1,Whicj))
		self.wait(6)
		Con = TextMobject("As ","$\\pi>e$",", we can \\\\say ;","$\\pi^e<e^\\pi$")
		Con.set_color(BLUE);Con[1].set_color(RED);Con[3].set_color(GREEN)
		Con.next_to(Form1,DOWN);Con.shift(0.5*DOWN)
		self.play(Write(Con))
		self.wait(6)
		#self.play(*[FadeOut(i) for i in self.mobjects],run_time=2)
		self.wait(5)

























