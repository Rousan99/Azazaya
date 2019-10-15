from manimlib.imports import *
class Hypocy(Scene):
	def construct(self):
	   big_circle = 3
	   small_circle = -big_circle/4#Just ignore the negative sign , it is given just to place the circle in right place.
	   self.Hyp(big_circle,small_circle)

	def Hyp(self,r1,r2):
		c1 = Circle(radius=r1,color=BLUE)
		c2 = Circle(radius=r2,color=GREEN).rotate(PI)
		c2.next_to(c1,LEFT,buff=0)
		c2.start = c2.copy()
		c2.flip(about_point=c2.point_from_proportion(0))
		dot = Dot(c2.point_from_proportion(0),color=YELLOW)
		line = Line(c2.get_center(),dot.get_center()).set_stroke(PINK,2.5)
		trace = VMobject(color=RED)
		trace.set_points_as_corners([dot.get_center(),dot.get_center()+UP*0.0001])
		trace_group = VGroup(line,dot,trace)
		
		#self.play(ShowCreation(line),ShowCreation(c1),ShowCreation(c2),GrowFromCenter(dot))
		#self.wait()
		self.add(line,c1,c2,dot)
		def update_group(group):
			l,mob,previus_trace = group
			mob.move_to(c2.point_from_proportion(0))
			old_trace = trace.copy()
			old_trace.append_vectorized_mobject(Line(old_trace.points[-1],dot.get_center()))
			old_trace.make_smooth()
			l.put_start_and_end_on(c2.get_center(),dot.get_center())
			trace.become(old_trace)

		def update_c2(c,alpha):
			c.become(c.start)
			c.flip(about_point=c2.point_from_proportion(0))
			c.rotate(2*PI*alpha,about_point=c1.get_center())
			c.rotate(2*PI*(r1/r2)*alpha,about_point=c.get_center())

		trace_group.add_updater(update_group)
		self.add(trace_group)
		
		self.play(UpdateFromAlphaFunc(c2,update_c2,rate_func=linear,run_time=5))
		self.wait()
