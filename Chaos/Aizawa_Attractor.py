from manimlib.imports import *
from scipy.integrate import odeint


class Aizawaa(Scene):#python manim.py Austin_new\Butterfly_Lotentz_attraction.py Butterflyf -pl
	def construct(self):
		#self.set_camera_orientation(phi=80*DEGREES,theta=35*DEGREES,distance=17)
		a = self.sol(0.1,0,0,YELLOW_C,RED_D,RED_C,BLUE_D)
		self.wait(3)

	def sol_plot(self,inix,iniy,iniz,colpart,col1,col2,col3,a = 0.95, b = 0.7,c = 0.6,d = 3.5,e =0.25,g = 0.1):
		def f(state,t):
			x,y,z=state
			return (z-b)*x - d*y, d*x+(z-b)*y, c+a*z-(pow(z,3)/3)-((x*x+y*y)*(1+e*z))+(g*z*pow(x,3))
		state0=[inix,iniy,iniz]#2.0,10.0,1.0
		t=np.arange(0.0,60.0,0.01)
		states = odeint(f,state0,t)
		p=VMobject()
		p.set_points_as_corners([*[[a,b,c] for a,b,c in zip(states[:,0],states[:,1],states[:,2])]]).set_shade_in_3d(True)
		p.make_smooth().set_stroke(None,2)
		#p.set_color(BLUE)
		new_func = CurvesAsSubmobjects(p).set_shade_in_3d(True)
		new_func.set_color_by_gradient(col1,col2,col3,GREEN,TEAL_C,MAROON_B)
		r=0.05

		particle = ParametricSurface(
			lambda u,v: np.array([
				r*np.cos(u) * np.cos(v),
				r*np.sin(u) * np.cos(v),
				r*np.sin(v)]),u_max=2*PI,u_min=0,v_max=2*PI,v_min=0,
			checkerboard_colors=[colpart,colpart],
			resolution=(10,20)).set_shade_in_3d(True)
		group = VGroup(particle,p,new_func).scale(0.1).move_to(ORIGIN)
		particle.add_updater(lambda m: m.move_to(p.get_end()))
		p.fade(1)
		self.add(particle)
		v = VGroup(particle,p,new_func)
		v.scale(20)
		self.begin_ambient_camera_rotation(0.2)
		self.play(ShowCreation(new_func),ShowCreation(p),rate_func=linear,run_time=15)
		self.move_camera(phi=0*DEGREES,run_time=4)
		#self.set_camera_orientation(phi=50*DEGREES,theta=80*DEGREES,distance=17)
	def sol(self,inix,iniy,iniz,colpart,col1,col2,col3,a = 0.95, b = 0.7,c = 0.6,d = 3.5,e =0.25,g = 0.1):
		def f(state,t):
			x,y,z=state
			return (z-b)*x - d*y, d*x+(z-b)*y, c+a*z-(pow(z,3)/3)-((x*x+y*y)*(1+e*z))+(g*z*pow(x,3))
		state0=[inix,iniy,iniz]#2.0,10.0,1.0
		t=np.arange(0.0,60.0,0.01)
		states = odeint(f,state0,t)
		p=VMobject()
		p.set_points_as_corners([*[[a,b,0] for a,b,c in zip(states[:,0],states[:,1],states[:,2])]])
		p.make_smooth().set_stroke(None,2)
		#p.set_color(BLUE)
		new_func = CurvesAsSubmobjects(p)
		new_func.set_color_by_gradient(col1,col2,col3,GREEN,TEAL_C,MAROON_B)
		group = VGroup(p,new_func).scale(0.1).move_to(ORIGIN)
		vectpr = Arrow(ORIGIN,p.get_end(),color=YELLOW)
		vectpr.add_updater(lambda m: m.become(Arrow(ORIGIN,p.get_end(),color=YELLOW)))
		p.fade(1)
		self.add(vectpr)
		v = VGroup(vectpr,p,new_func)
		v.scale(20)
		self.play(ShowCreation(new_func),ShowCreation(p),rate_func=linear,run_time=15)
