from manimlib.imports import *


class Opening_Quote(Scene):

    def construct(self):
        quote1 = TextMobject("Imagination is more important than knowledge")
        quote1.set_color(RED)
        quote1.to_edge(UP)
        author = TextMobject("-Albert Einstein")
        author.set_color(GOLD_B)
        author.scale(0.75)
        author.next_to(quote1.get_corner(DOWN+RIGHT),DOWN)
        self.play(Write(quote1),Write(author))

        LINE1 = TextMobject("What is Laplace's equation?\\\\ It is a second-order P.D.E of form $$\\nabla^2f=0$$")
        LINE1.to_edge(UP,buff=2)
        LINE1.set_color(BLUE)
        self.play(FadeIn(LINE1))
        self.wait()
        LINE2 = TextMobject("Where $\\nabla^2 = \\vec \\nabla \\cdot \\vec \\nabla $ and f is scalar valued function.")
        LINE2.next_to(LINE1,DOWN)
        self.play(FadeIn(LINE2))
        self.wait(2)
        Poission = TexMobject("\\nabla^2V=-\\frac{\\rho}{\\epsilon}")
        Poission.set_color(GREEN)

        title = Title("Laplace's Equation")
        title.set_color(RED)
        title.to_edge(UP)
        self.play(Transform(quote1,title),FadeOut(author))
        self.remove(LINE2)
        self.wait()
        Poission.next_to(title,DOWN)
        Laplace = TexMobject("\\nabla^2V=0")
        
        Laplace.set_color(GREEN)
        rect = SurroundingRectangle(Poission)
        rect.set_color(GOLD_B)
        rect1 = SurroundingRectangle(Laplace)
        rect.set_color(GOLD_B)
        Poission_T = TextMobject("Poisson Equation")
        Poission_T.next_to(rect, RIGHT)
        Poission_T.scale(0.75)
        self.play(Transform(LINE1,Poission),ShowCreation(rect),Write(Poission_T))
        self.wait(2)
        LINE3 = TextMobject("When $\\rho =0$ Poisson's eqn Transform to Laplace eqn.")
        LINE3.next_to(Poission.get_corner(DOWN+RIGHT),DOWN)
        self.play(Write(LINE3))
        self.wait()
        Laplace_T = TextMobject("Laplace Equation")
        Laplace_T.scale(0.75)
        Laplace_T.next_to(rect1, RIGHT)
        self.play(Transform(Poission,Laplace),Transform(rect,rect1),Transform(Poission_T,Laplace_T))
        self.wait(2)
        LINE4 = TextMobject("The Solution of Laplace eqn are called $\\textbf{Harmonic Functions}$.")
        LINE4.set_color(ORANGE)
        LINE4.next_to(Laplace,DOWN)
        self.play(Write(LINE4))
        self.wait(2)
        LINE5 = TextMobject("Laplacian is used in various fields of maths and physics but\\\\We will examine its's value in electrostatics.")
        LINE5.next_to(LINE4,DOWN)
        self.play(GrowFromCenter(LINE5))
        self.wait(2)
        self.remove(*self.mobjects)

        Laplace.next_to(title.get_corner(DOWN+LEFT),DOWN)
        self.play(Write(title),FadeIn(Laplace))
        self.wait(2)
        TYPE = TextMobject("Here We will learn the topic in 2 steps:")
        TYPE.set_color(BLUE)
        TYPE.next_to(title,DOWN)
        TYPE1 = TextMobject("1.General Intution of Laplacian","2.Laplace's Equation in many dimension and their Solution")
        TYPE1[0].set_color(GOLD_B)
        TYPE1[1].set_color(GOLD_B)
        TYPE1[0].next_to(TYPE,DOWN)
        TYPE1[1].next_to(TYPE1[0],DOWN)
        self.play(Write(TYPE),GrowFromCenter(TYPE1[0]),GrowFromCenter(TYPE1[1]))
        self.wait(2)
        LINE6 = TextMobject("We will see the Intution and significance.. \\\\ and also what it means to be the Laplacian in next video.")
        LINE6.set_color(ORANGE)
        LINE6.to_edge(DOWN)
        self.play(GrowFromCenter(LINE6))
        self.wait(2)




class Introduction_Intution(Scene):

    def construct(self):
        INTEXT1 = TextMobject("In the previous video we have seen that"," $\\nabla^2V=0$ is called Laplace's Equation","But have does it signify?," ,"Here we will learn that:")
        INTEXT1[0].set_color(RED)
        INTEXT1[1].set_color(BLUE)
        INTEXT1[2].set_color(GOLD_B)
        INTEXT1[3].set_color(GREEN)
        INTEXT1[0].to_edge(UP+RIGHT)
        INTEXT1[1].next_to(INTEXT1[0],DOWN)
        INTEXT1[2].next_to(INTEXT1[1],DOWN)
        INTEXT1[3].next_to(INTEXT1[2],DOWN)
        self.play(Write(INTEXT1[0]),Write(INTEXT1[1]),Write(INTEXT1[2]),Write(INTEXT1[3]))
        self.wait(3)
        self.play(FadeOut(INTEXT1[0]),FadeOut(INTEXT1[1]),FadeOut(INTEXT1[2]),FadeOut(INTEXT1[3]))
        self.wait()
        INtitle = Title("Laplace's Equation")
        INtitle.set_color(RED)
        INtitle.to_edge(UP)
        self.play(GrowFromCenter(INtitle))
        INTEXT2 =TextMobject("Now to understand the equation we have to understand","$\\nabla^2 \\simeq \\vec{\\nabla}\\cdot\\vec{\\nabla}$ itself.","$\\nabla^2 V \\simeq ((divergence)(gradient)(V)$")
        INTEXT2[0].set_color(BLUE)
        INTEXT2[1].set_color(GOLD_B)
        INTEXT2[2].set_color(GREEN)
        INTEXT2[0].next_to(INtitle,DOWN)
        INTEXT2[1].next_to(INTEXT2[0],DOWN)
        INTEXT2[2].next_to(INTEXT2[1],DOWN)
        INTEXT2[2].scale(0.7)
        INTEXT3 =  TextMobject("Divergence","Gradient")
        INTEXT3[0].set_color(RED)
        INTEXT3[1].set_color(RED)
        INTEXT3[0].to_edge(DOWN+RIGHT)
        INTEXT3[1].to_edge(DOWN+LEFT)

        self.play(FadeIn(INTEXT2[0]),Write(INTEXT2[1]))
        self.wait(2)
        self.play(Write(INTEXT2[2]),runtime=4)
        self.play(FadeIn(INTEXT3[0]),FadeIn(INTEXT3[1]))
        self.wait(74)
        self.remove(INTEXT2[0],INTEXT2[1],INTEXT2[2],INTEXT3[0],INTEXT3[1])
        self.remove(7)



class LaplacianSig1(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            number_line_config={
                "color": RED,
                "include_tip": False,
                "exclude_zero_from_default_numbers": True,
            }
        )
        parabola = ParametricSurface(
            lambda u,v: np.array([
                u,
                v,
                7*u*v/np.exp((u**2 + v**2))]),u_max=2,u_min=-2,v_max=2,v_min=-2,
            checkerboard_colors=[PURPLE_D,PURPLE_E],
            resolution=(10,32)).scale(2)
        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(0.3)
        self.play(Write(parabola),Write(axes))
        self.wait()
        circle1 = Circle(radius=0.1,fill_opacity=1.0)
        circle2 = Circle(radius=0.1,fill_opacity=1.0)
        circle7 = Circle(radius=0.1,fill_opacity=1.0)
        circle8 = Circle(radius=0.1,fill_opacity=1.0)
        vect1=np.array([np.sqrt(2),-np.sqrt(2),-2*1.2876])
        vect2=np.array([-np.sqrt(2),np.sqrt(2),-2*1.2876])
        vect7=np.array([np.sqrt(2),np.sqrt(2),2*1.2876])
        vect8=np.array([-np.sqrt(2),-np.sqrt(2),2*1.2876])
        circle1.move_to(vect1)
        circle2.move_to(vect2)
        circle7.move_to(vect7)
        circle8.move_to(vect8)
        line0 = Arrow(np.array([np.sqrt(2),np.sqrt(2),2*1.2876]),np.array([-np.sqrt(2),np.sqrt(2),-2*1.2876]))
        line1 = Arrow(np.array([np.sqrt(2),-np.sqrt(2),-2*1.2876]),np.array([np.sqrt(2),np.sqrt(2),2*1.2876]))
        line2 = Arrow(np.array([np.sqrt(2),-np.sqrt(2),2*1.2876]),np.array([-np.sqrt(2),-np.sqrt(2),2*1.2876]))
        line2.set_color(BLUE)
        line1.set_color(BLUE)
        line0.set_color(GREEN)
        line3 = Arrow(np.array([-np.sqrt(2),np.sqrt(2),-2*1.2876]),np.array([-np.sqrt(2),-np.sqrt(2),2*1.2876]))
        line4 = Arrow(np.array([-np.sqrt(2),np.sqrt(2),-2*1.2876]),np.array([np.sqrt(2),np.sqrt(2),2*1.2876]))
        line3.set_color(GOLD_B)
        line4.set_color(GOLD_B)
        circle7.set_color(GREEN)
        circle8.set_color(GREEN)


        self.set_camera_orientation(phi=0 * DEGREES)
        self.play(FadeIn(circle1),FadeIn(circle2),FadeIn(circle7),FadeIn(circle8))
        self.wait(21)
        self.play(Write(line2),Write(line1),Write(line3),Write(line0))
        self.wait(12)
        self.play(Transform(line0,line4))
        self.begin_ambient_camera_rotation(0.0)
        self.wait()
        #INtitle1 = Title("Laplacian significance")
        #INtitle1.set_color(RED)
        #INtitle1.to_edge(UP)
        #self.add_fixed_in_frame_mobjects(INtitle1)
        #self.play(Write(INtitle1))
        self.wait(5)
        self.remove(line1,line2,line3,line4,circle2,circle1,circle7,circle8,line0)
        self.play(FadeOut(parabola),FadeOut(axes))
        #Text100=TextMobject("Now Drawing the Gradient of the surface \\\\ for all possible points in XY plane")
        self.wait()
        #Text100.set_color(RED)
        #self.play(GrowFromCenter(Text100))
        #self.wait(4)


        #field = VGroup(*[self.calc_field(u*RIGHT+v*UP)])


class Field(Scene):
    CONFIG = {
        "color_list": ['#2be22b', '#e88e10', '#eae600', '#88ea00',
                       '#00eae2', '#0094ea', "#2700ea", '#bf00ea', '#ea0078'],
        "prop": 0
    }

    def construct(self):
        axes_config = {"x_min": -5,
                       "x_max": 5,
                       "y_min": -5,
                       "y_max": 5,
                       "z_axis_config": {},
                       "z_min": -1,
                       "z_max": 1,
                       "z_normal": DOWN,
                       "num_axis_pieces": 20,
                       "light_source": 9 * DOWN + 7 * LEFT + 10 * OUT,
                       "number_line_config": {
                           "include_tip": False,
                       },
                       }

        axes = Axes(**axes_config)
        axes.set_color(PURPLE_D)
        f = VGroup(
            *[self.calc_field_color(x * RIGHT + y * UP, self.vect, prop=0)
              for x in np.arange(-5, 5, 1)
              for y in np.arange(-5, 5, 1)
              ]
        )


        field = VGroup(axes, f)
        circle3=Circle(radius=0.5)
        circle3.set_color(BLUE)
        vect3=np.array([1/np.sqrt(2),1/np.sqrt(2),0])
        circle3.move_to(vect3)
        circle4=Circle(radius=0.5)
        circle4.set_color(BLUE)
        vect4=np.array([-1/np.sqrt(2),-1/np.sqrt(2),0])
        circle4.move_to(vect4)


        circle5=Circle(radius=0.5)
        circle5.set_color(GOLD_B)
        vect5=np.array([-1/np.sqrt(2),1/np.sqrt(2),0])
        circle5.move_to(vect5)
        circle6=Circle(radius=0.5)
        circle6.set_color(GOLD_B)
        vect6=np.array([1/np.sqrt(2),-1/np.sqrt(2),0])
        circle6.move_to(vect6)

        Source1=TextMobject("-SOURCE")
        Source2=TextMobject("-SOURCE")
        Source1.next_to(circle3)
        Source2.next_to(circle4,LEFT)

        Source3=TextMobject("+SOURCE")
        Source4=TextMobject("+SOURCE")
        Source3.next_to(circle5,LEFT)
        Source4.next_to(circle6)

        Gauss=TexMobject("\\vec E =-\\nabla V")
        Gauss.set_color(BLUE)
        Gauss.to_edge(DOWN)
        Poision2 = TexMobject("\\nabla^2V=-\\frac{\\rho}{\\epsilon}","\\vec \\nabla\\cdot\\vec E=-\\frac{\\rho}{\\epsilon}")
        Poision2[0].set_color(RED)
        Poision2[1].set_color(RED)
        Poision2[0].to_edge(DOWN)
        Poision2[1].to_edge(DOWN)





        self.wait(2)
        self.play(ShowCreation(field))
        self.wait(17)
        self.play(Write(circle3),Write(circle4))
        self.wait(5)
        self.play(Write(circle5),Write(circle6))
        self.wait(16)
        self.play(Write(Source1),Write(Source2))
        self.wait(8)
        self.play(Write(Source3),Write(Source4))
        self.wait(55)
        self.play(FadeIn(Gauss))
        self.wait(2)
        self.wait(34)
        self.play(FadeOut(Gauss))
        self.wait(20)
        self.play(Write(Poision2[1]))
        self.play(ReplacementTransform(Poision2[1],Poision2[0]))
        self.wait(37)


    def calc_field_color(self, point, f, prop=0.0, opacity=None):
        x, y = point[:2]
        func = f(x, y)
        magnitude = math.sqrt(func[0] ** 2 + func[1] ** 2)
        func = func / magnitude if magnitude != 0 else np.array([0, 0])
        func = func / 1.7
        v = int(magnitude / 10 ** prop)
        index = len(self.color_list) - 1 if v > len(self.color_list) - 1 else v
        c = self.color_list[index]
        v = Vector(func, color=c).shift(point)
        if opacity:
            v.set_fill(opacity=opacity)
        return v

    @staticmethod
    def vect(x, y):
        return np.array([
            7*y*(1-2*x**2)/np.exp(x**2+y**2),
            7*x*(1-2*y**2)/np.exp(x**2+y**2),
            0
        ])



class Source_term(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            number_line_config={
                "color": RED,
                "include_tip": False,
                "exclude_zero_from_default_numbers": True,
            }
        )
        potential = ParametricSurface(
            lambda u,v: np.array([
                u,
                v,
                0.25+7*u*v/np.exp((u**2 + v**2))]),u_max=2,u_min=-2,v_max=2,v_min=-2,
            checkerboard_colors=[PURPLE_D,PURPLE_E],
            resolution=(10,32)).scale(2)
        plane = ParametricSurface(
            lambda u,v: np.array([
                u,
                v,
                0.25]),u_max=2,u_min=-2,v_max=2,v_min=-2,
            checkerboard_colors=[PURPLE_D,PURPLE_E],
            resolution=(10,32)).scale(2)
        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(0.2)
        self.play(Write(potential),Write(axes))
        self.wait()
        self.wait(10)
        self.play(ReplacementTransform(potential,plane),run_time=5)
        self.wait(5)
        self.wait(2)
        plane_tilt = ParametricSurface(
            lambda u,v: np.array([
                u,
                v,
                0.6*(u+0.01*v)]),u_max=2,u_min=-2,v_max=2,v_min=-2,
            checkerboard_colors=[PURPLE_D,PURPLE_E],
            resolution=(10,32)).scale(2)
        self.play(ReplacementTransform(plane,plane_tilt),run_time=4)
        self.wait(3)
        self.wait(2)



class They_See_Me_Rolling(ThreeDScene):
    CONFIG = {
        "t":4,
        "r": 0.2,
        "R": 4,
        "laps":2*2*np.pi
    }

    def they_hating(self,da):

#try removing da
        ball_1 = ParametricSurface(
            lambda u, v: np.array([
                self.r * np.cos(u) * np.cos(v),
                self.r * np.sin(u) * np.cos(v),
                self.r * np.sin(v)
            ]), v_min=0, v_max=TAU / 2, u_min=0, u_max=TAU / 2, checkerboard_colors=[BLUE_D, BLUE_D],
            resolution=(20, 20))
        ball_2 = ParametricSurface(
            lambda u, v: np.array([
                self.r * np.cos(u) * np.cos(v),
                self.r * np.sin(u) * np.cos(v),
                self.r * np.sin(v)
            ]), v_min=TAU / 2, v_max=TAU, u_min=TAU / 2, u_max=TAU, checkerboard_colors=[RED_D, RED_D],
            resolution=(20, 20))

        ball = VGroup(ball_1, ball_2)

        trajectory = ParametricFunction(
            lambda j: np.array([
                (1/np.sqrt(2)),
                j,
                (7*j/(np.sqrt(2)*np.exp(0.5+(j)**2)))
            ]), j_min=-1/(4*np.sqrt(2)), j_max=1/(4*np.sqrt(2)), color=PURPLE_D
        )

        ball.rotate(self.t*self.R/self.r*da,[1/np.sqrt(2),1/np.sqrt(2),(7)/(2*np.exp(1))])

        position_ball = np.array([
                (1/np.sqrt(2)),
                (1/np.sqrt(2)),
                (7/(np.sqrt(2)*np.exp(0.5+0.5)))*da+self.r ])

        ball.move_to(position_ball)
        group=VGroup(ball,trajectory)

        return group

    def construct(self):


        ball_1 = ParametricSurface(
            lambda u, v: np.array([
                self.r * np.cos(u) * np.cos(v),
                self.r * np.sin(u) * np.cos(v),
                self.r * np.sin(v)
            ]), v_min=0, v_max=TAU / 2, u_min=0, u_max=TAU / 2, checkerboard_colors=[BLUE_D, BLUE_D],
            resolution=(20, 20))
        ball_2 = ParametricSurface(
            lambda u, v: np.array([
                self.r * np.cos(u) * np.cos(v),
                self.r * np.sin(u) * np.cos(v),
                self.r * np.sin(v)
            ]), v_min=TAU / 2, v_max=TAU, u_min=TAU / 2, u_max=TAU, checkerboard_colors=[RED_D, RED_D],
            resolution=(20, 20))

        ball=VGroup(ball_1,ball_2)

        #parabola = ParametricSurface(
            #lambda u,v: np.array([
               # u,
                #v,
                #7*u*v/np.exp((u**2 + v**2))]),u_max=2,u_min=-2,v_max=2,v_min=-2,
            #checkerboard_colors=[PURPLE_D,PURPLE_E])

        Random_Surface = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                7*u*v/np.exp((u**2 + v**2))
            ]), v_min=-1.8*TAU, v_max=TAU, u_min=-1.8*TAU, u_max=TAU, checkerboard_colors=[PURPLE_D, PURPLE_E],
            resolution=(40, 40))

        ball.move_to([1/np.sqrt(2),1/np.sqrt(2),(7)/(2*np.exp(1))+self.r])

        trajectory = ParametricFunction(
            lambda da: np.array([
                0,0,0
            ]), t_min=0, t_max=1, color=RED
        )

        group=VGroup(ball,trajectory)



        def update(iteration,da):
            new_it = self.they_hating(da)
            iteration.become(new_it)
            return iteration

        self.set_camera_orientation(phi=50 * DEGREES, theta=50 * DEGREES, distance=8)
        self.begin_ambient_camera_rotation(rate=0.1)

        self.play(GrowFromCenter(ball),ShowCreation(Random_Surface))
        self.wait(5)
        self.play(UpdateFromAlphaFunc(group,update),run_time=self.t, rate_func=linear)
        self.wait(5)

class Ending(Scene):

    def construct(self):
        title = Title("Laplace's Equation Solution Properties")
        title.set_color(RED)
        title.to_edge(UP)
        PROPERTY1 = TextMobject("1.The Solution tolerates no local maxima or minima.\\\\If is does, then it will become poisson's solution.")
        PROPERTY1.set_color(BLUE)
        PROPERTY2 = TextMobject("2.It represent average around the point of interest.\\\\ i.e., It is a averaging function.")
        PROPERTY2.set_color(BLUE)
        PROPERTY1.next_to(title.get_corner(DOWN),DOWN)
        note1 = TextMobject("The maxima and minima can only exist at the boundaries.")
        note1.set_color(GOLD_B)
        note1.scale(0.70)
        note1.next_to(PROPERTY1.get_corner(DOWN),DOWN)
        note2 = TextMobject("The first points is explained the second one will \\\\ be explaned seperately for different dimensions.")
        note2.set_color(GOLD_B)
        note2.next_to(PROPERTY2.get_corner(DOWN),DOWN)
        note2.scale(0.70)
        PROPERTY2.next_to(note1.get_corner(DOWN),DOWN)
        self.play(Write(title))
        self.wait(3)
        self.play(Write(PROPERTY1),run_time=5)
        self.wait()
        self.play(Write(note1))
        self.wait(3)
        self.play(Write(PROPERTY2),run_time=4)
        self.wait()
        self.play(Write(note2))
        self.wait(3)
        self.remove(title,PROPERTY1,PROPERTY2,note1,note2)
        next1 = TextMobject("In the next video we will see Laplacian in 1D.\\\\ See you next time.")
        next1.set_color(GREEN)
        self.play(Write(next1))
        self.wait(2)
