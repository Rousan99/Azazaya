from manimlib.imports import *
from scipy.integrate import odeint


class Butterflyf(ThreeDScene):#python manim.py Austin_new\Butterfly_Lotentz_attraction.py Butterflyf -pl
    def construct(self):
        axes = ThreeDAxes(
            number_line_config={
                "color": DARK_BROWN,
                "include_tip": False,
                "exclude_zero_from_default_numbers": True,
            }
        )
        self.play(FadeIn(axes))
        self.set_camera_orientation(phi=80*DEGREES,theta=35*DEGREES,distance=17)
        self.sol_plot(28,10,8/3,2.0,10.0,1.0,YELLOW_C,RED_D,RED_C,BLUE_D)
        #self.sol_plot(28,10,8/3,-2.2,-10.2,1.0,GREEN,BLUE_D,TEAL_D,BLUE_C)


    def sol_plot(self,rho,sigma,beta,inix,iniy,iniz,colpart,col1,col2,col3):
        def f(state,t):
            x,y,z=state
            return sigma*(y-x),x*(rho-z)-y,x*y-beta*z
        state0=[inix,iniy,iniz]#2.0,10.0,1.0
        t=np.arange(0.0,60.0,0.01)
        states = odeint(f,state0,t)
        p=VMobject()
        p.set_points_as_corners([*[[a,b,c] for a,b,c in zip(states[:,0],states[:,1],states[:,2])]])
        p.make_smooth().set_stroke(None,2)
        #p.set_color(BLUE)
        new_func = CurvesAsSubmobjects(p)
        new_func.set_color_by_gradient(col1,col2,col3,TEAL_C,MAROON_B)

        particle = ParametricSurface(
            lambda u,v: np.array([
                0.5*np.cos(u) * np.cos(v),
                0.5*np.sin(u) * np.cos(v),
                0.5*np.sin(v)]),u_max=2*PI,u_min=0,v_max=2*PI,v_min=0,
            checkerboard_colors=[colpart,colpart],
            resolution=(10,20))
        group = VGroup(particle,p,new_func).scale(0.1).move_to(ORIGIN)
        particle.add_updater(lambda m: m.move_to(p.get_end()))
        p.fade(1)
        self.add(particle)
        v = VGroup(particle,p,new_func)
        v.scale(1.7)
        self.begin_ambient_camera_rotation(0.2)
        self.play(ShowCreation(new_func),ShowCreation(p),rate_func=linear,run_time=20)
        #self.set_camera_orientation(phi=50*DEGREES,theta=80*DEGREES,distance=17)
