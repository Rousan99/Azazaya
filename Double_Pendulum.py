from manimlib.imports import *
from numpy import sin, cos
from scipy.integrate import odeint
COBALT = "#0047AB"


class DouPen(Scene):
	def construct(self):
		Tit = Title("Double-Pendulum")
		Tit.to_edge(UP)
		Tit.set_color(COBALT)
		Tit.scale(0.90)
		self.play(Write(Tit))
		self.Double(100,90,5,0,9.8,RED,BLUE,GREEN,YELLOW)
		self.wait()




	def Double(self,th1,th2,w1,w2,G,xcol1,xcol1l,xcol2,xcol2l):
	    # acceleration due to gravity, in m/s^2
		L1 = 2.0  # length of pendulum 1 in m
		L2 = 2.0  # length of pendulum 2 in m
		M1 = 40  # mass of pendulum 1 in kg
		M2 = 40  # mass of pendulum 2 in kg
		def derivs(state, t):
			dydx = np.zeros_like(state)
			dydx[0] = state[1]
			del_ = state[2] - state[0]
			den1 = (M1 + M2)*L1 - M2*L1*cos(del_)*cos(del_)
			dydx[1] = (M2*L1*state[1]*state[1]*sin(del_)*cos(del_) + M2*G*sin(state[2])*cos(del_) + M2*L2*state[3]*state[3]*sin(del_) - (M1 + M2)*G*sin(state[0]))/den1
			dydx[2] = state[3]
			den2 = (L2/L1)*den1
			dydx[3] = (-M2*L2*state[3]*state[3]*sin(del_)*cos(del_) + (M1 + M2)*G*sin(state[0])*cos(del_) - (M1 + M2)*L1*state[1]*state[1]*sin(del_) - (M1 + M2)*G*sin(state[2]))/den2
			return dydx
		# create a time array from 0..100 sampled at 0.05 second step
		dt = 0.05
		t = np.arange(0.0, 20, dt)
		# th1 and th2 are the initial angles (degrees)
		# w10 and w20 are the initial angular velocities (degrees per second)
		# initial state
		state = np.radians([th1, w1, th2, w2])
		# integrate your ODE using scipy.integrate.
		y = odeint(derivs, state, t)
		p1=VMobject()
		p1.set_points_as_corners([*[[L1*sin(a),-L1*cos(a),0] for a in y[:,0]]])
		p1.make_smooth().set_stroke(None,2)

		p2=VMobject()
		p2.set_points_as_corners([*[[L2*sin(b)+L1*sin(a),-L2*cos(b)-L1*cos(a),0] for a,b in zip(y[:,0],y[:,2])]])
		p2.make_smooth().set_stroke(None,2)

		new_func1 = CurvesAsSubmobjects(p1)
		new_func1.set_color_by_gradient(BLACK)
		new_func1.set_opacity(0)
		new_func2 = CurvesAsSubmobjects(p2)
		new_func2.set_color_by_gradient(RED)






		center = np.array([0,-0.3,0])
		zero = Dot(color=PURPLE)
		zero.move_to(center)
		self.add(zero)
		Blob1 = Dot(color=xcol1)
		Blob1.move_to(p1.get_end())
		Blob1.scale(1.2)
		Blob1.add_updater(lambda m: m.move_to(p1.get_end()))
		#self.play(Write(Blob1))
		line1 = Line(center,Blob1)
		line1.set_color(xcol1l)
		self.play(Write(line1))
		line1.add_updater(lambda m: m.become(Line(zero.get_center(),Blob1.get_center(),color=xcol1l)))
		self.add(Blob1,line1)
		Blob2 = Dot(color=xcol2)
		Blob2.scale(1.6)
		Blob2.move_to(p2.get_end())
		#self.play(Write(Blob2))
		Blob2.add_updater(lambda m: m.move_to(p2.get_end()))
		line2 = Line(Blob1,Blob2)
		line2.set_color(xcol2l)
		self.play(Write(line2))
		line2.add_updater(lambda m: m.become(Line(Blob1.get_center(),Blob2.get_center(),color=xcol2l)))
		self.add(Blob2,line2)
		#label = TexMobject(f"Mass1={x},Mass2={y}").scale(2.5).to_edge(LEFT,buff=1)

		p1.fade(1)
		p2.fade(1)
		self.play(ShowCreation(new_func1),ShowCreation(p1),ShowCreation(new_func2),ShowCreation(p2),rate_func=linear,run_time=30)#Here the value of simulation starts with the 1st value after the initial conditions so you can't see the value of theta you give.
