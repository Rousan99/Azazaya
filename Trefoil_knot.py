from manimlib.imports import *
import random
MY_PINK = "#FF66CC"
ore = "#FF9999"

class knot(ThreeDScene):
	def construct(self):
		axes = ThreeDAxes(
			number_line_config={
				"color": GREEN,
				"include_tip": False,
				"exclude_zero_from_default_numbers": True,
			}
		)
		self.play(FadeIn(axes))
		self.set_camera_orientation(phi=80*DEGREES,theta=35*DEGREES)
		particle = ParametricSurface(
			lambda u,v: np.array([
				0.06*np.cos(u) * np.cos(v),
				0.06*np.sin(u) * np.cos(v),
				0.06*np.sin(v)]),u_max=2*PI,u_min=0,v_max=4*PI,v_min=0,
			checkerboard_colors=[YELLOW_C,YELLOW_D],
			resolution=(20,30))
		def func(t):
			return np.array([(2+np.cos(3*t))*np.cos(2*t),
				(2+np.cos(3*t))*np.sin(2*t),
				np.sin(3*t)])
		func = ParametricFunction(func,t_max=2*PI,fill_opacity=0)
		new_func = CurvesAsSubmobjects(func)
		new_func.set_color_by_gradient(BLUE_D,BLUE_C,RED_C,RED_D,RED_C,BLUE_C)
		particle.add_updater(lambda m: m.move_to(func.get_end()))
		func.fade(1)
		particle.move_to(np.array([3,0,0]))
		self.add(particle)

		self.begin_ambient_camera_rotation(0.2)
		self.play(ShowCreation(new_func),ShowCreation(func),rate_func=linear,run_time=7)
		self.play(FadeOut(particle))
		#self.play(ApplyMethod(self.set_camera_orientation(phi=80*DEGREES)))
		self.set_camera_orientation(phi=0*DEGREES)
		self.wait(4)

class draw(Scene):
	def construct(self):
		q = NumberPlane()
		q.set_color(GREEN)
		q.set_opacity(0.5)
		self.play(Write(q),run_time=1)
		dot = Dot(color=YELLOW_C)
		def fun(t):
			return np.array([(2+np.cos(3*t))*np.cos(2*t),
				(2+np.cos(3*t))*np.sin(2*t),0])
		fun = ParametricFunction(fun,t_max=2*PI,fill_opacity=0)
		new_fun = CurvesAsSubmobjects(fun)
		new_fun.set_color_by_gradient(BLUE_D,BLUE_C,RED_C,RED_D,RED_C,BLUE_C)
		dot.add_updater(lambda m: m.move_to(fun.get_end()))
		fun.fade(1)
		origin = Dot(color=MY_PINK)
		origin.move_to(np.array([0,0,0]))
		origin.scale(0.5)
		self.add(origin)
		dot.move_to(np.array([3,0,0]))
		dot.scale(0.5)
		self.add(dot)
		#self.wait(0.7)
		radius = Arrow(origin,dot,buff=0,color=MY_PINK)
		self.add(radius)
		radius.add_updater(lambda m: m.become(Arrow(origin.get_center(),dot.get_center(),buff=0,color=MY_PINK)))
		self.add(radius)
		self.play(ShowCreation(new_fun),ShowCreation(fun),rate_func=linear,run_time=7)
		self.play(FadeOut(dot))
		self.wait(4)
