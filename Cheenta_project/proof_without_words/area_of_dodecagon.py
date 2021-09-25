from manim import *

class Introduction(Scene):
    config.background_color = "#1b1b1b"
    def construct(self):
        title = Title("Area of Dodecagon - Proof without talk").set_color_by_gradient(RED,ORANGE,YELLOW,GREEN,BLUE)
        title.scale(0.7)
        self.play(Write(title))
        self.wait(2)
        mean = Tex("Dodecagon $\\to$ $12$ sided regular polygon").set_color(RED)
        self.play(Write(mean),run_time=2)
        self.wait(5)
        plane = NumberPlane(x_range=[-3.5,3.5],y_range=[-3.3,3.3],background_line_style={
                "stroke_color": TEAL,
                "stroke_opacity": 0.1
            })
        plane.shift(0.5*DOWN)
        SS = SurroundingRectangle(plane,buff=0)
        self.play(ReplacementTransform(mean,VGroup(plane,SS)),run_time=2)
        self.wait(4)
        cir = Circle(radius=3,color=BLUE).move_to(plane.c2p(0,0))
        self.play(Write(cir),run_time=2)
        self.wait(3)
        arrow = DoubleArrow(plane.c2p(0,0),plane.c2p(3,0),buff=0).set_color(GREEN)
        arr_tex = MathTex("r").set_color(YELLOW)
        arr_tex.next_to(arrow,DOWN)
        self.play(Write(VGroup(arrow,arr_tex)),run_time=2)
        self.wait(6)
        radius_val = Tex("radius = r").set_color(YELLOW).to_edge(LEFT).shift(2*UP)
        self.play(ReplacementTransform(VGroup(arr_tex,arrow),radius_val),run_time=2)
        self.wait(3)
        gen_eq = MathTex("x_n = r\\cdot e^{\\frac{2\\pi i k}{12}}").set_color(BLUE)
        con = MathTex("k\\in \\{0,1,2,\cdots ,10,11\\}").scale(0.6)
        gen_eq.next_to(radius_val,DOWN)
        con.next_to(gen_eq,DOWN)
        self.play(FadeIn(VGroup(gen_eq,con)),run_time=2)
        self.wait(4)
        x_cod = [3*np.cos(2*PI*i/12) for i in range(12)]
        y_cod = [3*np.sin(2*PI*i/12) for i in range(12)]
        points = VGroup()
        cen = Dot(radius=0.07, point = plane.c2p(0,0),color=GREEN,z_index=4)
        for i in range(12):
            dot = Dot(radius=0.07, point = plane.c2p(x_cod[i],y_cod[i]),color=YELLOW,z_index=4)
            points.add(dot)
        self.play(ReplacementTransform(VGroup(gen_eq,con),points),FadeIn(cen),run_time=2)
        self.wait(5)
        poly = RegularPolygon(n=12,color=GREEN).move_to(plane.c2p(0,0))
        poly.scale(3)
        self.play(Write(poly),run_time=2)
        self.wait(3)
        self.play(FadeOut(cir))
        self.wait(2)
        direct_line_index = [0,2,3,4,6,7,8,10,11]
        tri_index = [0,2,4,6,8,10]
        dir_lines = VGroup()
        for i in direct_line_index:
            line = Line(plane.c2p(0,0),points[i],color=RED,z_index=2)
            dir_lines.add(line)
        self.play(Write(dir_lines),run_time=5)
        self.wait(5)
        tri_line = VGroup()
        for i in [0,2,4]:
            line = Line(points[tri_index[i]],points[tri_index[i+1]],color=PURPLE,z_index=2)
            tri_line.add(line)
        self.play(Write(tri_line),run_time=3)
        self.wait(8)

class pasrt_2(MovingCameraScene):
    config.background_color = "#1b1b1b"
    def construct(self):
        plane = NumberPlane(x_range=[-3.5,3.5],y_range=[-3.3,3.3],background_line_style={
                "stroke_color": TEAL,
                "stroke_opacity": 0.1
            })
        plane.shift(3.5*LEFT)
        ss = SurroundingRectangle(plane,buff=0)
        self.add(plane,ss)
        x_cod = [3*np.cos(2*PI*i/12) for i in range(12)]
        y_cod = [3*np.sin(2*PI*i/12) for i in range(12)]
        points = VGroup()
        cen = Dot(radius=0.07, point = plane.c2p(0,0),color=GREEN,z_index=4)
        for i in range(12):
            dot = Dot(radius=0.07, point = plane.c2p(x_cod[i],y_cod[i]),color=YELLOW,z_index=4)
            points.add(dot)
        poly = RegularPolygon(n=12,color=GREEN).move_to(plane.c2p(0,0))
        poly.scale(3)
        self.add(points,cen,poly)
        direct_line_index = [0,2,3,4,6,7,8,10,11]
        tri_index = [0,2,4,6,8,10]
        dir_lines = VGroup()
        for i in direct_line_index:
            line = Line(plane.c2p(0,0),points[i],color=RED,z_index=2)
            dir_lines.add(line)
        tri_line = VGroup()
        for i in [0,2,4]:
            line = Line(points[tri_index[i]],points[tri_index[i+1]],color=PURPLE,z_index=2)
            tri_line.add(line)
        self.add(dir_lines,tri_line)
        o = cen.get_center()
        pol1 = Polygon(o,points[0].get_center(),points[2].get_center(),color=RED,fill_opacity=0.2,stroke_width=2)
        pol2 = Polygon(points[0].get_center(),points[1].get_center(),points[2].get_center(),color=PURPLE,fill_opacity=0.2,z_index=3,stroke_width=2)
        pol3 = Polygon(o,points[2].get_center(),points[3].get_center(),color=RED,fill_opacity=0.2,stroke_width=2)
        pol4 = Polygon(o,points[3].get_center(),points[4].get_center(),color=RED,fill_opacity=0.2,stroke_width=2)
        pol5 = Polygon(o,points[4].get_center(),points[6].get_center(),color=RED,fill_opacity=0.2,stroke_width=2)
        pol6 = Polygon(points[4].get_center(),points[5].get_center(),points[6].get_center(),color=PURPLE,fill_opacity=0.2,z_index=3,stroke_width=2)
        pol7 = Polygon(o,points[6].get_center(),points[7].get_center(),color=RED,fill_opacity=0.2,stroke_width=2)
        pol8 = Polygon(o,points[7].get_center(),points[8].get_center(),color=RED,fill_opacity=0.2,stroke_width=2)
        pol9 = Polygon(o,points[8].get_center(),points[10].get_center(),color=RED,fill_opacity=0.2,stroke_width=2)
        pol10 = Polygon(points[8].get_center(),points[9].get_center(),points[10].get_center(),color=PURPLE,fill_opacity=0.2,z_index=3,stroke_width=2)
        pol11 = Polygon(o,points[10].get_center(),points[11].get_center(),color=RED,fill_opacity=0.2,stroke_width=2)
        pol12 = Polygon(o,points[11].get_center(),points[0].get_center(),color=RED,fill_opacity=0.2,stroke_width=2)
        polly = VGroup(pol1,pol2,pol3,pol4,pol5,pol6,pol7,pol8,pol9,pol10,pol11,pol12)
        self.play(Write(polly),run_time=2)
        self.wait(4)
        self.play(Uncreate(VGroup(plane,ss)),FadeOut(points),FadeOut(VGroup(cen,poly)),FadeOut(tri_line),FadeOut(dir_lines),run_time=2)
        self.wait()
        first_shift = VGroup(pol1,pol2,pol7,pol8)
        second_shift = VGroup(pol3,pol4,pol9,pol10)
        self.play(second_shift.animate.shift(4*RIGHT),run_time=2)
        self.wait(4)
        self.play(self.camera.frame.animate.scale(1.3),run_time=2)
        self.play(self.camera.frame.animate.shift(RIGHT),run_time=2)
        self.wait(2)
        self.play(first_shift.animate.shift(9*RIGHT),run_time=2)
        self.wait(5)
        # self.remove(pol12)
        self.play(pol12.animate.shift(dir_lines[4].get_vector()*1.016))
        self.wait(2)
        self.play(pol11.animate.shift(dir_lines[3].get_vector()*1.016))
        self.wait(2)

        small_tri_shift = VGroup(
            Line(points[5].get_center(),o),
            Line(o,points[9].get_center()),
            Line(o,points[1].get_center())
            )
        self.play(pol6.animate.shift(small_tri_shift[0].get_vector()*1.016))
        self.wait(4)

        self.play(pol3.animate.shift(dir_lines[6].get_vector()*1.016),
                    pol4.animate.shift(dir_lines[7].get_vector()*1.016),
                    pol10.animate.shift(small_tri_shift[1].get_vector()*-1),
                    run_time=2)
        self.wait(4)

        self.play(pol7.animate.shift(dir_lines[0].get_vector()*1.016),
                    pol8.animate.shift(dir_lines[1].get_vector()*1.016),
                    pol2.animate.shift(small_tri_shift[2].get_vector()*-1.016),
                    run_time=2)
        self.wait(4)
        # self.add(NumberPlane())
        arr = DoubleArrow([-1,-2.9,0],[2.01,-2.9,0],buff=0).set_color(BLUE)
        arr_tex = Tex("r").set_color(YELLOW)
        arr_tex.next_to(arr,DOWN)
        self.play(Write(arr),FadeIn(arr_tex),run_time=2)
        self.wait(4)
        block1 = VGroup(pol12,pol11,pol6,pol5)
        block2 = VGroup(pol7,pol8,pol2,pol1)
        block3 = VGroup(pol3,pol4,pol10,pol9)

        rot_fact = PI/6

        self.play(Rotating(block1,radians=rot_fact),
                    Rotating(block2,radians=-rot_fact),
        run_time=2)
        self.wait()
        self.play(block1.animate.next_to(block3,LEFT,buff=0),
             block2.animate.next_to(block3,RIGHT,buff=0),run_time=2)
        self.wait(2)
        squ = Rectangle(height=3,width=9.1,z_index=6,stroke_width=5).move_to(block3.get_center())
        self.play(Write(squ),run_time=2)
        self.wait(4)
        arr1 = DoubleArrow(squ.get_vertices()[0],squ.get_vertices()[1],buff=-0.1,color=YELLOW).shift(0.2*UP)
        arr1_val = MathTex("3r").next_to(arr1,UP)
        self.play(Write(VGroup(arr1,arr1_val)),run_time=2)
        self.wait(2)

        arr2 = DoubleArrow(squ.get_vertices()[1],squ.get_vertices()[2],buff=-0.1,color=YELLOW).shift(0.2*LEFT)
        arr2_val = MathTex("r").next_to(arr2,LEFT)
        self.play(Write(VGroup(arr2,arr2_val)),run_time=2)
        self.wait(7)

        eqs = MathTex("=").rotate(PI/2)
        eqs.next_to(arr1_val,UP)
        self.play(Write(eqs))
        self.wait()
        self.play(self.camera.frame.animate.shift(1.5*UP),run_time=2)

        poly = RegularPolygon(n=12,color=GREEN,fill_color=WHITE,fill_opacity=0.4).scale(2).next_to(eqs,UP)
        self.play(Write(poly),run_time=2)
        self.wait(2)
        ras = DoubleArrow(poly.get_center(),poly.get_vertices()[2],buff=0,color=BLUE)
        ras_v = MathTex("r").set_color(RED).next_to(ras,RIGHT).shift(0.2*LEFT+0.1*DOWN)
        self.play(Write(VGroup(ras,ras_v)),Write(Dot(radius=0.09,color=YELLOW,point=poly.get_center())),run_time=2)
        self.wait(3)
        area = Tex("Area(Dodecagon) = Area(Rectangle) = $3r \\times r = 3r^2$").scale(0.8).next_to(eqs)
        area.set_color(YELLOW)
        self.play(Write(area),run_time=2)
        self.wait(10)
