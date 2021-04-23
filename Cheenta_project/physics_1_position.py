from manimlib import *
import numpy as np
from math import radians as rad, degrees as deg


class opening(Scene):
	def construct(self):
		title = Title("Idea of Frame of reference").set_color(RED)
		title.fix_in_frame()

		self.play(Write(title),run_time=2)
		self.wait(2)

		frame = self.camera.frame
		frame.save_state()
		frame.set_euler_angles(
			theta=-30 * DEGREES,
			phi=70 * DEGREES,
		)

		wood_box = Cube(side_length=1).set_color(YELLOW)
		wood_box.save_state()

		self.play(FadeIn(wood_box),run_time=2)
		self.wait(2)
		self.play(wood_box.animate.shift(2*RIGHT))
		self.play(wood_box.animate.shift(2*UP))
		self.play(wood_box.animate.shift(6*LEFT))
		self.play(wood_box.animate.restore())
		self.wait(6)
		#restore

		earth_sp = Sphere(radius=1)#, resolution=torus1.resolution)

		day_texture = "earth_day_map"
		night_texture = "earth_night_map"

		earth = TexturedSurface(earth_sp, day_texture, night_texture)

		self.play(FadeOut(wood_box),FadeIn(earth))
		self.wait(3)
		self.play(Rotate(earth, 2*PI), run_time=2)
		self.wait(5)
		self.play(earth.animate.shift(2*UP-4.5*LEFT))
		self.wait(4)


		sun_sp = Sphere(radius=2.5)
		sun_texture = "sun_map"

		sun = TexturedSurface(sun_sp,sun_texture)
		sun.shift(LEFT)
		self.play(FadeIn(sun),run_time=2)
		self.wait(9)
		self.play(frame.animate.restore())
		self.wait(2)
		self.play(*[FadeOut(i) for i in self.mobjects])
		self.wait()

class explanation_one(Scene):
	def construct(self):
		title = Title("Idea of Frame of reference in 1D").set_color(RED)
		title.fix_in_frame()
		self.add(title)
		self.wait(4)

		tri = Triangle(fill_opacity=1,fill_color=YELLOW,color=YELLOW).shift(4*LEFT)
		a = tri.point_from_proportion(0)
		tri_cpy = tri.copy()
		tri_cpy.set_opacity(0.4)
		self.play(Write(tri),Write(tri_cpy),run_time=2)
		self.wait(5)
		tri.save_state()
		self.play(tri.animate.shift(7*RIGHT),run_time=6)
		self.wait(3)

		pause = SVGMobject("play_symbol")
		self.add(pause)

		self.wait(12)

		reference_point = Dot(radius=0.08,color=BLUE).move_to(a)
		self.play(Write(reference_point))
		self.wait(7)
		line = NumberLine(color=RED,x_range=[0,8,1])
		line.shift(a[1]*UP)
		self.play(Write(line),run_time=2)
		self.remove(reference_point);self.add(reference_point)
		self.wait(15)
		self.remove(pause)
		self.play(tri.animate.restore(),run_time=2)

		dist = DecimalNumber(0,unit="cm").scale(0.8)
		dist.add_updater(lambda d: d.next_to(tri,UP,buff=0.1))
		dist.add_updater(lambda d: d.set_value(line.p2n(tri.point_from_proportion(0))))
		self.add(dist)
		self.play(tri.animate.shift(7*RIGHT),run_time=6)
		self.wait(8)
		names = Tex("O","A").scale(0.8);names[0].set_color(BLUE);names[1].set_color(YELLOW)
		names[0].next_to(reference_point,UP,buff=0.2);names[1].move_to(tri.point_from_proportion(0)+0.3*UP)
		self.play(FadeIn(names),FadeOut(dist))
		self.wait(5)
		value = TexText("position of the triangle w.r.t ","blue-point"," = ","OA").set_color(GREEN)
		value[1].set_color(BLUE);value[3].set_color_by_gradient(BLUE,YELLOW)
		value.shift(2*DOWN)
		self.play(Write(value))
		self.wait(10)
		direction = Arrow(line.n2p(0)+[0,0.2,0],line.n2p(1)+[0,0.2,0],buff=0,color=YELLOW)
		self.play(Write(direction),run_time=2)
		self.wait(6)
		val_vec = Tex("OA","\\ ","\\hat{i}").set_width(value[3].get_width())
		val_vec[0].set_color_by_gradient(BLUE,YELLOW)
		val_vec.move_to(value[3].get_center())
		self.play(Transform(value[3],val_vec))
		self.wait(10)
		foref = TexText("The ","red Number-Line"," is the frame of reference for this case.").next_to(value,DOWN)
		foref[1].set_color(RED)
		self.play(Write(foref),run_time=2)
		self.wait(7)
		self.play(FadeOut(VGroup(tri,tri_cpy,reference_point,line,names,value,direction,foref)))
		self.wait(5)
		road = Line([-7,-1.5,0],[7,-1.5,0],color=GREEN)
		self.play(Write(road),run_time=2)
		self.wait(6)
		any_shape = ImageMobject("road").scale(0.7).shift(UP+3*RIGHT)
		straight_shape = ImageMobject("straight_road").set_width(any_shape.get_width()).next_to(any_shape,LEFT,buff=2)

		self.play(FadeIn(any_shape),run_time=2)
		self.wait(8)
		self.play(FadeIn(straight_shape))
		self.wait(10)
		self.play(FadeOut(any_shape),FadeOut(straight_shape))
		self.wait(2)
		car = SVGMobject("car",color=BLUE).scale(0.8).shift(0.7*DOWN+LEFT*5)
		self.play(Write(car),run_time=2)
		self.wait(5)
		self.play(car.animate.shift(7*RIGHT),run_time=6)
		self.wait(7)
		self.play(*[FadeOut(i) for i in self.mobjects],run_time=2)
		self.wait()

class explanation_two_int(Scene):
	def construct(self):
		title = Title("Idea of Frame of reference in 2D").set_color(RED)
		title.fix_in_frame()
		self.play(Write(title),run_time=2)
		self.wait(4)
		foot_ball_match_side = ImageMobject("football_match_side").shift(3.5*LEFT)
		self.play(FadeIn(foot_ball_match_side),run_time=2)
		self.wait(10)
		want = TexText("Position of all the players in field").set_color(BLUE).set_width(foot_ball_match_side.get_width())
		want.next_to(foot_ball_match_side,DOWN)
		self.play(Write(want),run_time=2)
		self.wait(10)

		foot_ball_match_top = ImageMobject("football_match_top").shift(3*LEFT)
		self.play(FadeOut(foot_ball_match_side),FadeIn(foot_ball_match_top))
		self.wait(10)
		a = TexText("It is now just a 2-D problem"," i.e., finding positions of object in 2-D plane.").set_color_by_gradient(BLUE,YELLOW)
		a[0].next_to(foot_ball_match_top,DOWN)
		a[1].next_to(a[0],DOWN);a[1].shift(RIGHT*0.5)
		self.play(ReplacementTransform(want,a[0]))
		self.wait(4)
		self.play(Write(a[1]))
		self.wait(12)
		self.play(FadeOut(foot_ball_match_top),Uncreate(a))
		self.wait()

class explanation_two(Scene):
	def construct(self):
		title = Title("Idea of Frame of reference in 2D").set_color(RED)
		title.fix_in_frame()
		self.add(title)

		ball = SVGMobject("oak_leap").set_color(GREEN)
		self.play(Write(ball),run_time=2)
		self.wait(10)
		self.play(ball.animate.shift(2*DOWN+4*RIGHT),run_time=2)
		self.play(ball.animate.shift(-4*DOWN-8*RIGHT),run_time=2)
		self.play(ball.animate.shift(3*DOWN+2*RIGHT),run_time=2)
		self.wait(16)



		axes = Axes(
			x_range=(-7, 7),
			y_range=(-4, 4),
			height=6,
			width=14,
			axis_config={
				"stroke_color": GREY_A,
				"stroke_width": 2,
			},
			y_axis_config={
				"include_tip": False,
			},
			x_axis_config={
				"include_tip": False,
			}
		)
		axes.add_coordinate_labels(
			font_size=17,
			num_decimal_places=1,
		)
		# axes.move_to([0,0,0])
		a = axes.copy()
		self.play(Write(a),run_time=2)
		self.wait(10)

		axes2 = Axes(
			x_range=(-7, 7),
			y_range=(-4, 4),
			angle = 30,
			height=8,
			width=14,
			axis_config={
				"stroke_color": GREY_A,
				"stroke_width": 2,
			},
			y_axis_config={
				"include_tip": False,
			},
			x_axis_config={
				"include_tip": False,
			}
		)
		axes2.add_coordinate_labels(
			font_size=17,
			num_decimal_places=1,
		)
		# self.add(axes2)
		self.play(ReplacementTransform(a,axes2),run_time=2)
		self.wait(10)
		self.play(ReplacementTransform(axes2,axes),run_time=2)
		self.wait(5)
		self.play(ball.animate.shift(LEFT+DOWN),run_time=2)
		self.wait(6)
		com = Dot(radius=0.06,color=YELLOW,point=ball.get_center_of_mass())
		self.play(Write(com),run_time=2)
		self.wait(6)
		self.play(ball.animate.set_opacity(0.1),run_time=2)
		self.wait(5)
		f_always(com.move_to, lambda: ball.get_center_of_mass())

		h_line  = always_redraw(lambda: axes.get_h_line(com.get_center(),color=BLUE,stroke_width=6))
		x_arrow = Arrow(axes.c2p(0,0),[ball.get_center()[0],0,0],buff=0).set_color(BLUE)
		self.play(Write(x_arrow),run_time=2)
		self.wait(6)
		self.play(ReplacementTransform(x_arrow,h_line),run_time=2)
		self.remove(com);self.add(com)
		self.wait(4)

		v_line = always_redraw(lambda: axes.get_v_line(com.get_center(),color=BLUE,stroke_width=6))
		y_arrow = Arrow(axes.c2p(0,0),[0,ball.get_center()[1],0],buff=0).set_color(BLUE)
		self.play(Write(y_arrow),run_time=2)
		self.wait(6)
		self.play(ReplacementTransform(y_arrow,v_line),run_time=2)
		self.remove(com);self.add(com)
		self.wait(4)

		x_val = DecimalNumber(axes.p2c(com.get_center_of_mass())[0],num_decimal_places=1).scale(0.5)
		y_val = DecimalNumber(axes.p2c(com.get_center_of_mass())[1],num_decimal_places=1).scale(0.5)



		position_val = TexText("position"," = ","(",",",")").set_color(YELLOW)
		position_val[0].set_color(BLUE)
		position_val.next_to(title,DOWN).shift(5*LEFT)
		x_val.move_to(position_val[-2].get_center()).shift(0.2*RIGHT+0.13*UP)
		position_val[-2].shift(x_val.get_width()*RIGHT)
		position_val[-1].shift(2*x_val.get_width()*RIGHT)
		y_val.next_to(position_val[-2],buff=0.01).shift(UP*0.13+0.08*RIGHT)
		

		x_val_c = x_val.copy().scale(0.6).set_color(RED).next_to(h_line,DOWN)
		y_val_c = y_val.copy().scale(0.6).set_color(RED).next_to(v_line,LEFT)

		self.play(Write(VGroup(x_val_c,y_val_c)),run_time=2)
		self.wait(8)


		self.play(Write(position_val),Write(VGroup(x_val,y_val)),run_time=2)
		self.wait(10)

		x_val.add_updater(lambda d: d.set_value(axes.p2c(com.get_center_of_mass())[0]))
		y_val.add_updater(lambda d: d.set_value(axes.p2c(com.get_center_of_mass())[1]))

		x_val_c.add_updater(lambda d: d.become(x_val.copy().scale(0.6).set_color(RED)))
		y_val_c.add_updater(lambda d: d.become(y_val.copy().scale(0.6).set_color(RED)))

		x_val_c.add_updater(lambda d: d.next_to(h_line,DOWN))
		y_val_c.add_updater(lambda d: d.next_to(v_line,LEFT))
		self.add(x_val,y_val,x_val_c,y_val_c)

		self.play(ball.animate.move_to([0,0,0]),run_time=2)
		def fun(t):
			return np.array([5*np.sin(2*t),2*np.sin(3*t),0])

		curve = ParametricCurve(fun,t_range=[0,2*PI])
		self.play(MoveAlongPath(ball,curve),run_time=15)
		self.wait(5)

		# new_form = Tex("\\hat{i}","+(","\\hat{j})").scale.set_color(BLUE)
		# new_form[0:2].move_to(position_val[3]).shift(UP*0.21)
		# new_form[2].next_to(position_val[-1])
		# self.play(FadeOut(VGroup(position_val[2:5])),x_val.animate.shift(0.25*LEFT),y_val.animate.shift(0.3*RIGHT))
		# self.play(Write(new_form))
		# self.wait(5)
		self.play(FadeOut(VGroup(position_val,x_val,y_val)),run_time=2)
		self.play(ball.animate.shift(2.5*RIGHT+1.5*UP),run_time=3)
		self.wait(13)

		names = Tex("O","A","B","P").set_color(RED).scale(0.6)
		names[0].move_to(axes.c2p(-0.15,-0.15))
		names[1].move_to([com.get_center()[0],-0.3,0])
		names[2].move_to([-0.3,com.get_center()[1],0])
		names[-1].next_to(com,RIGHT)
		self.play(Write(names))
		self.wait(6)

		x_vec = Arrow([0,0,0],[com.get_center()[0],0,0],buff=0).set_color(YELLOW)
		y_vec = Arrow([com.get_center()[0],0,0],com.get_center(),buff=0).set_color(YELLOW)

		text = TexText("Position of the leaf = ","+").scale(0.8).set_color(BLUE)
		text.to_corner(UL).shift(DOWN+LEFT*0.5)
		self.play(Write(text[0]),run_time=2)
		self.wait(5)

		self.play(Write(x_vec),run_time=2)
		self.wait(6)

		x_vec_text = Tex("OA","\\hat{i}").set_color(YELLOW)
		x_vec_text[0].set_color(RED)
		x_vec_text.next_to(text[0])

		self.play(ReplacementTransform(x_vec.copy(),x_vec_text))
		self.wait(6)
		text[1].next_to(x_vec_text)
		self.play(FadeIn(text[1]))

		self.play(Write(y_vec),run_time=2)
		self.wait(4)

		y_vec_text = Tex("OB","\\hat{j}").set_color(YELLOW)
		y_vec_text[0].set_color(RED)
		y_vec_text.next_to(text[1])
		self.play(ReplacementTransform(y_vec.copy(),y_vec_text))

		self.wait(10)
		final = Vector(com.get_center()).set_color(RED)
		self.play(ReplacementTransform(VGroup(x_vec,y_vec),final),run_time=2)
		self.wait(10)
		self.play(*[FadeOut(i) for i in self.mobjects])
		a = NumberPlane()
		self.play(Write(a),run_time=2)
		a.prepare_for_nonlinear_transform()
		self.play(a.animate.apply_complex_function(np.exp), run_time=5)
		self.wait(6)

		self.play(*[FadeOut(i) for i in self.mobjects],run_time=2)

		self.wait()

