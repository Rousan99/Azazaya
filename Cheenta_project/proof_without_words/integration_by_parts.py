from manim import *

class graphs(GraphScene):
    def construct(self):
        logo = Tex("CHEENTA.COM").set_color_by_gradient(RED,ORANGE,YELLOW,GREEN,BLUE)
        logo.scale(0.7);logo.to_corner(DR);logo.shift(0.5*RIGHT+0.3*DOWN)
        self.add(logo)
        self.x_min=0
        self.x_max=10
        self.x_axis_width=10
        self.x_axis_label="u"
        self.y_min=0
        self.y_max=5
        self.y_axis_height=5
        self.y_axis_label="v"
        self.axes_color=GREY
        self.graph_origin = DOWN*2.8+LEFT*5
        self.include_tip=True
        self.x_axis_config={"include_ticks":False}
        self.y_axis_config={"include_ticks":False}
        self.setup_axes(animate=True)
        self.wait(4)

        here_tex = MathTex("u = f(x)"," ; ","v = g(x)").set_color_by_gradient(RED,YELLOW,GREEN).arrange(direction=RIGHT,buff=0.1)
        here_tex.to_edge(UP+RIGHT)
        self.play(Write(here_tex),run_time=2)
        self.wait(3)

        x_min = 2; x_max = 9

        graph = self.get_graph(lambda m: np.sqrt(m), x_min=x_min,x_max=x_max,color=YELLOW,stroke_width=6)
        self.play(Write(graph),run_time=2)
        self.wait(4)

        dot = Dot(radius=0.1,color=GOLD,z_index=2)
        print(graph[-1])
        dot.move_to(graph.get_start())
        self.play(Write(dot))
        self.wait(2)

        begin_point = dot.copy()
        self.add(begin_point)

        coordinate = MathTex("(","f(x)",",","g(x)",")").set_color(GREEN).scale(0.8)
        coordinate[1].set_color(RED);coordinate[3].set_color(PURPLE)

        coordinate.next_to(dot,RIGHT)
        self.play(Write(coordinate),run_time=2)
        self.wait(4)

        coordinate.add_updater(lambda m: m.next_to(dot,RIGHT))
        self.add(coordinate)

        start_hori = self.get_horizontal_line_to_graph(x_min,graph,line_class=DashedLine,color=RED,z_index=-1)

        start_ver = self.get_vertical_line_to_graph(x_min,graph,line_class=DashedLine,color=PURPLE,z_index=-1)
        self.play(Write(VGroup(start_hori,start_ver)),run_time=2)
        self.wait(2)

        start_vals = MathTex("g(a)","f(a)").set_color(YELLOW).scale(0.9)
        start_vals[0].next_to(start_hori,LEFT); start_vals[1].next_to(start_ver,DOWN)
        self.play(Write(start_vals),run_time=2)

        self.wait(3)

        self.play(MoveAlongPath(dot,graph),run_time=3)
        self.wait(2)

        end_point = dot.copy()
        self.add(end_point)

        end_hori = self.get_horizontal_line_to_graph(x_max,graph,line_class=DashedLine,color=RED,z_index=-1)

        end_ver = self.get_vertical_line_to_graph(x_max,graph,line_class=DashedLine,color=PURPLE,z_index=-1)
        self.play(Write(VGroup(end_hori,end_ver)),run_time=2)
        self.wait(2)

        end_vals = MathTex("g(b)","f(b)").set_color(YELLOW).scale(0.9)
        end_vals[0].next_to(end_hori,LEFT); end_vals[1].next_to(end_ver,DOWN)
        self.play(Write(end_vals),run_time=2)
        self.wait(4)


        inverse_graph = self.get_graph(lambda m: m**2, x_min=np.sqrt(x_min),x_max=np.sqrt(x_max))
        a = inverse_graph.get_start()
        b = graph.get_start()
        # inverse_graph.shift(b-a)
        # self.add(inverse_graph)


        
        area1 = self.get_riemann_rectangles(graph,x_min=x_min,x_max=x_max,dx=0.01,stroke_width=0,start_color=RED,end_color=RED,z_index=-1)
        area2 = self.get_riemann_rectangles(inverse_graph,x_min=np.sqrt(x_min),x_max=np.sqrt(x_max),dx=0.01,stroke_width=0,start_color=BLUE,end_color=BLUE,z_index=-1)
        area2.rotate_about_origin(PI/2);area2.flip(axis=UP)
        c = area2[0].point_from_proportion(0)
        area2.shift(b-c)

        self.play(Write(VGroup(area1,area2)),run_time=3)
        self.wait(6)

        vals = Tex("Area","Area").set_color(YELLOW)
        vals[0].to_edge(UP)
        vals[0].shift(6*LEFT+0.2*UP)


        area1_copy = area1.copy()
        area2_copy = area2.copy()

        area1_copy.generate_target()
        area1_copy.target.scale(0.2)
        area1_copy.target.next_to(vals[0],buff=0.2)
        # area1_copy.target.shift(0.2*UP)
        self.play(Write(vals[0]))
        self.play(MoveToTarget(area1_copy))
        self.wait()

        plus = MathTex("+").next_to(area1_copy,RIGHT,buff=0.2)
        self.play(FadeIn(plus))

        vals[1].next_to(plus,RIGHT,buff=0.2)

        area2_copy.generate_target()
        area2_copy.target.scale(0.2)
        area2_copy.target.next_to(vals[1],RIGHT,buff=0.2)

        self.play(Write(vals[1]))
        self.play(MoveToTarget(area2_copy))
        self.wait(3)

        equals = MathTex("=","-").set_color(YELLOW)
        namess = Tex("Area","Area").set_color(YELLOW)
        equals[0].next_to(area2_copy,RIGHT,buff=0.2)
        namess[0].next_to(equals[0],RIGHT,buff=0.2)

        self.play(FadeOut(here_tex),Write(equals[0]),run_time=2)
        self.wait()

        h = x_max
        l = np.sqrt(x_max)

        shi = DOWN*2.8+LEFT*5
        rec1 = Rectangle(height=l,width=h,stroke_width=0,stroke_color=YELLOW,fill_opacity=0.3)
        rec1.shift(shi-(h/2)*LEFT-(l/2)*DOWN)
        
        rec1.generate_target()
        rec1.target.scale(0.2)
        rec1.target.next_to(namess[0],RIGHT,buff=0.2)
        self.play(Write(namess[0]))
        self.wait()
        self.play(MoveToTarget(rec1),run_time=2)
        self.wait(2)

        equals[1].next_to(rec1,RIGHT,buff=0.2)
        self.play(Write(equals))

        namess[1].next_to(equals[1],RIGHT,buff=0.2)


        rec2 = Rectangle(height=np.sqrt(x_min),width=x_min,stroke_width=0,stroke_color=YELLOW,fill_opacity=0.3)
        rec2.shift(shi-(x_min/2)*LEFT-(np.sqrt(x_min)/2)*DOWN)
        
        rec2.generate_target()
        rec2.target.scale(0.5)
        rec2.target.next_to(namess[1],RIGHT,buff=0.2)
        self.play(Write(namess[1]))
        self.wait()
        self.play(MoveToTarget(rec2),run_time=2)
        self.wait(4)

        red_area = MathTex("\\int_{f(a)}^{f(b)}v du","+","\\int_{g(a)}^{g(b)}u dv","=","f(b)\\cdot g(b)","-","f(a)\\cdot g(a)","=","f(x)\\cdot g(x)","|_{a}^{b}").set_color(YELLOW)
        red_area.scale(0.75)
        color = [RED,BLUE]
        for i in range(4):
            red_area[2*i].set_color(color[i%2])
        red_area.next_to(rec1,DOWN)
        red_area.shift(LEFT)
        self.play(Write(red_area))
        self.wait(6)
        blue_area = MathTex("\\int_{a}^{b}g(x) d(f(x))","+","\\int_{a}^{b}f(x) d(g(x))","=","f(x)\\cdot g(x)","|_{a}^{b}").set_color(YELLOW)
        blue_area.scale(0.75)
        blue_area[0].set_color(RED)
        blue_area[2].set_color(BLUE)
        blue_area.next_to(red_area,DOWN)
        self.play(ReplacementTransform(red_area.copy(),blue_area),run_time=2)
        self.wait(5)

        result = MathTex("\\int_{a}^{b}f(x) g'(x)dx","=","f(x)\\cdot g(x)","|_{a}^{b}","-","\\int_{a}^{b}g(x) f'(x)dx").set_color(YELLOW).scale(0.9)
        result.next_to(rec1,DOWN)
        result[0].set_color(BLUE);result[-1].set_color(RED)
        result.shift(0.5*LEFT)
        self.play(ReplacementTransform(VGroup(red_area,blue_area),result),run_time=2)
        self.wait(2)
        ass = SurroundingRectangle(result).set_color(GREEN)
        self.play(Write(ass),run_time=2)
        self.wait(4)
        # self.play(*[FadeOut(i) for i in self.mobjects],run_time=2)
        # self.wait()



        # self.play()

class introduction(Scene):
    def construct(self):
        logo = Tex("CHEENTA.COM").set_color_by_gradient(RED,ORANGE,YELLOW,GREEN,BLUE)
        logo.scale(0.7);logo.to_corner(DR);logo.shift(0.5*RIGHT+0.3*DOWN)
        self.add(logo)
        tt = Title("Integration by Parts : Proof without words").set_color_by_gradient(RED,YELLOW,GREEN,BLUE)
        self.play(Write(tt),run_time=2)
        self.wait(2)
        tod = Tex("Today we will see proof without word (","with-out talk",")"," of this:").set_color(YELLOW)
        tod[1].set_color(BLUE)
        tod.shift(UP)
        self.play(FadeIn(tod),run_time=2)
        self.wait(4)

        result = MathTex("\\int_{a}^{b}f(x) g'(x)dx","=","f(x)\\cdot g(x)","|_{a}^{b}","-","\\int_{a}^{b}g(x) f'(x)dx").set_color(YELLOW).scale(0.9)
        result.next_to(tod,DOWN)
        result[0].set_color(BLUE);result[-1].set_color(RED)
        self.play(Write(result),run_time=2)
        self.wait(5)
        # self.play(*[FadeOut(i) for i in self.mobjects],run_time=2)
        

        




