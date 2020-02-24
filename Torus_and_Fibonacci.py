from manimlib.imports import *

class Introduction(Scene):
	def construct(self):
		Titl = Title("Fibonacci Matrix and Torus")
		Titl.to_edge(UP)
		Titl.set_color(RED)
		Titl.scale(0.8)
		self.play(Write(Titl),run_time=2)
		Text = TextMobject("In the previous Video on the same topic you see We have told\\\\about how to visualize matrix as a Linear-Transformation(specially for Fibonacci Matrix).")
		Text.set_color(BLUE); Text.scale(0.7);Text.next_to(Titl,DOWN)
		self.play(Write(Text),run_time=3)
		self.wait(2)
		pp = TextMobject("previous Video Scene");pp.set_color(YELLOW);pp.scale(0.7);pp.to_edge(DOWN)
		self.play(Write(pp),run_time=2)
		self.wait(15)
		self.play(FadeOut(pp),FadeOut(Text),run_time=3)
		self.wait(2)
		formula = TexMobject("""
            \\Gamma= 
            \\left[
                \\begin{array}{cc}
                    2 & 1 \\\\
                    1 & 1
                \\end{array}
            \\right]""")
		formula.set_color(YELLOW)
		formula.next_to(Titl,DOWN)
		self.play(Write(formula),run_time=3)
		self.wait(7)#We can divide these matrix in 2 coloum vectors
		formula1 = TexMobject("""
            \\Gamma(0) = ""","""\\left[
                \\begin{array}{c}
                    2 \\\\
                    1
                \\end{array}
            \\right]""",""";""","""\\Gamma(1) = ""","""\\left[
                \\begin{array}{c}
                    1 \\\\
                    1
                \\end{array}
            \\right]""")
		color = [YELLOW,RED,WHITE,YELLOW,GREEN]
		for i in range(5):
			formula1[i].set_color(color[i])
		formula1.next_to(formula,DOWN)
		self.play(Transform(formula.copy(),formula1),run_time=2)
		self.wait(10)
		Where = TextMobject("Here $1^{st}$ one describes where x axis unit vector goes and \\\\ $2^{nd}$ one describes where y axis unit vector goes.")
		Where.scale(0.8)
		Where.shift(2*DOWN)
		Where.set_color(BLUE)
		self.play(Write(Where),run_time=2)
		self.wait(10)
		self.play(*[FadeOut(mob) for mob in self.mobjects],run_time=2)
		self.wait(2)
class Transformm(LinearTransformationScene):
	CONFIG = {
		"include_background_plane": True,
		"include_foreground_plane": True,
		"foreground_plane_kwargs":{
		"x_radius": FRAME_WIDTH,
		"y_radius": FRAME_HEIGHT,
		"secondary_line_ratio": 0},
		"background_plane_kwargs":{
		"color":RED,
		"secondary_color": YELLOW,
		"stroke_width": 3
		},
		"show_coordinates": True,
		"show_basis_vectors":True,
		"basis_vector_width":6,
		"i_hat_color": X_COLOR,
		"j_hat_color": YELLOW,
		"leave_ghost_vectors": False
	}
	def construct(self):
		grid = NumberPlane()
		grid.set_color(RED)
		self.play(Write(grid),run_time=2)
		self.wait(8)
		point1 = Dot(color=BLUE,radius=0.1)
		point2 = Dot(color=YELLOW,radius=0.1)
		point1.move_to(np.array([1,0,0]))
		point2.move_to(np.array([0,1,0]))
		self.play(Write(point1),run_time=2)
		self.play(Write(point2),run_time=2)
		self.wait(6)
		self.play(ApplyMethod(point1.move_to,np.array([2,1,0]),rate_func=linear,run_time=2),ApplyMethod(point2.move_to,np.array([1,1,0]),rate_func=linear,run_time=2))
		self.wait(14)
		self.play(FadeOut(point1),FadeOut(point2))
		self.wait(2)


		grid_transform_title = TextMobject(
			"Now Let's Transform it,using Fibonacci Matrix."
		)
		grid_transform_title.set_color(PURPLE)
		grid_transform_title.shift(2*DOWN)
		self.play(Write(grid_transform_title))
		self.wait(3)
		self.play(FadeOut(grid_transform_title))
		self.wait(2)
		matrix = [[2,1],[1,1]]
		self.apply_matrix(matrix,run_time=4)
		self.wait(6)

		#self.play(*[FadeOut(i) for i in self.mobjects],run_time=2)



class test(Scene):
	def construct(self):
		hammer = SVGMobject("abu")
		hammer.set_color(RED)
		hammer.scale(2)
		self.add(hammer)


















		


