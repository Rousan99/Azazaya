from manim import *

config.background_color = "#1b1b1b"

class graphs(GraphScene):
    def construct(self):
        logo = Tex("CHEENTA.COM").set_color_by_gradient(RED,ORANGE,YELLOW,GREEN,BLUE)
        logo.scale(0.6);logo.to_corner(DR);logo.shift(0.4*RIGHT+0.3*DOWN)
        self.add(logo)
        self.x_min=0
        self.x_max=7
        self.x_axis_width=6.5
        self.x_axis_label="x"
        self.y_min=0
        self.y_max=5
        self.y_axis_height=5
        self.y_axis_label="f(x,t)"
        self.axes_color=GREY

        self.graph_origin = DOWN*3.1+LEFT*6.2
        self.include_tip=True
        self.x_axis_config={"include_ticks":True}
        self.y_axis_config={"include_ticks":True}
        # self.x_axis_label_mob.set_color(RED)
        self.setup_axes(animate=False)
        self.wait(2)

        a = 0.5
        b = 0.5; c = 2*PI-0.5
        graphf = self.get_graph(lambda m: np.sin(m)+0.6+0.01*m**3+a, x_min=0,x_max=2*PI,color=YELLOW,stroke_width=6)
        self.play(Write(graphf),run_time=2)
        self.wait(2)
        graphf_lab = self.get_graph_label(graphf,"f(x,t)",x_val=2*PI,color=YELLOW)
        self.play(Write(graphf_lab),run_time=2)
        self.wait(2)
        
        
        b_mark = self.coords_to_point(b-0.2,-0.2); c_mark = self.coords_to_point(c+0.3,-0.2)
        b_tex = Tex("a",color=YELLOW).scale(0.8);c_tex = Tex("b",color=YELLOW).scale(0.8)
        b_tex.move_to(b_mark); c_tex.move_to(c_mark)

        self.play(FadeIn(VGroup(b_tex,c_tex)),run_time=2)
        self.wait(2)
        
        
        b_line = self.get_vertical_line_to_graph(b,graphf,line_class=DashedLine,z_index=-1).set_color(RED)
        c_line = self.get_vertical_line_to_graph(c+0.21,graphf,line_class=DashedLine,z_index=-1).set_color(RED)
        self.play(Write(VGroup(b_line,c_line)))
        self.wait(2)

        area_f = self.get_riemann_rectangles(graphf,x_min=b,x_max=c,dx=0.5,input_sample_type="left",stroke_width=3,fill_opacity=0.5,
        start_color=BLUE,
        end_color=BLUE,
        z_index=-3)

        self.play(Write(area_f),run_time=2)
        self.wait(3)

        area1 = MathTex("A","=","\\sum_{a}^{b}","f(x,t)","\\Delta x").set_color(GREEN);area1[0].set_color(BLUE);area1[-2].set_color(YELLOW)
        area1.to_corner(UL);area1.shift(-0.4*RIGHT+0.35*UP)
        self.play(Write(area1),run_time=2)
        self.wait(4)

        dx_val_br = BraceBetweenPoints(self.coords_to_point(1.5,0),self.coords_to_point(2,0),direction=DOWN).set_color(YELLOW)
        self.play(Write(dx_val_br),run_time=2)
        self.wait(2)
        dx_val = MathTex("\\Delta x").set_color(RED)
        dx_val.next_to(dx_val_br,buff=0.1)
        self.play(FadeIn(dx_val))
        self.wait(2)

        fx_val_br = BraceBetweenPoints(self.coords_to_point(1.5,0),self.input_to_graph_point(1.5,graphf),direction=RIGHT).set_color(YELLOW)
        self.play(Write(fx_val_br),run_time=2)
        self.wait(2)
        f_h = MathTex("f(x,t)").set_color(YELLOW).scale(0.7).set_stroke(None,4)
        f_h.rotate(PI/2); f_h.next_to(fx_val_br,RIGHT,buff=0.1)
        self.play(FadeIn(f_h))
        self.wait(2)

        #_____________________________________________________________________________________________________________________________
        a1 = ValueTracker(1.5)
        graphf_a = self.get_graph(lambda m: np.sin(m+0.01*a1.get_value())+1+0.01*m**3+a1.get_value(), x_min=0,x_max=2*PI,color="#6FFF00",stroke_width=6)
        self.play(Write(graphf_a),run_time=2)
        self.wait(2)
        graphf_a.add_updater(lambda k: k.become(self.get_graph(lambda m: np.sin(m+0.01*a1.get_value())+1+0.01*m**3+a1.get_value(), x_min=0,x_max=2*PI,color="#6FFF00",stroke_width=6)))
        self.add(graphf_a)

        graphf_a_lab = self.get_graph_label(graphf_a,"f(x,t+\\Delta t)",x_val=2*PI,color="#6FFF00",direction=LEFT)
        self.play(Write(graphf_a_lab),run_time=2)
        self.wait(2)
        graphf_a_lab.add_updater(lambda m:m.become(self.get_graph_label(graphf_a,"f(x,t+\\Delta t)",x_val=2*PI,color="#6FFF00",direction=LEFT)))
        self.add(graphf_a_lab)

        b_line_a = self.get_vertical_line_to_graph(b,graphf_a,line_class=DashedLine,z_index=-2).set_color(YELLOW)
        c_line_a = self.get_vertical_line_to_graph(c+0.21,graphf_a,line_class=DashedLine,z_index=-2).set_color(YELLOW)
        self.play(Write(VGroup(b_line_a,c_line_a)))
        self.wait(2)

        area_f_a = self.get_riemann_rectangles(graphf_a,x_min=b,x_max=c,dx=0.5,input_sample_type="left",stroke_width=3,fill_opacity=0.5,
        start_color=RED,
        end_color=RED,
        bounded_graph=graphf,
        z_index=-3)

        self.play(Write(area_f_a),run_time=2)
        self.wait(4)

        fxa_val_br = BraceBetweenPoints(self.coords_to_point(1.5,0),self.input_to_graph_point(1.5,graphf_a),direction=LEFT,buff=0).set_color("#6FFF00")
        self.play(Write(fxa_val_br),run_time=2)
        self.wait(2)
        f_ha = MathTex("f(x,t+\\Delta t)").set_color("#6FFF00").scale(0.7).set_stroke(None,4)
        f_ha.rotate(PI/2); f_ha.next_to(fxa_val_br,LEFT,buff=0.1)
        self.play(FadeIn(f_ha))

        self.wait(6)

        area2 = MathTex("A","+","\\Delta A","=","\\sum_{a}^{b}","f(x,t + \\Delta t)","\\Delta x").set_color(GREEN);area2[0].set_color(BLUE)
        area2[-2].set_color("#6FFF00")
        area2[2].set_color(RED)
        area2.next_to(area1,buff=2.5)
        self.play(Write(area2),run_time=2)
        self.wait(4)

        dela_a = MathTex("\\Delta A","=","\\sum_{a}^{b}","(","f(x,t + \\Delta t)","-","f(x,t)",")","\\Delta x").set_color(GREEN)
        dela_a[0].set_color(RED);dela_a[4].set_color("#6FFF00");dela_a[6].set_color(YELLOW)
        dela_a.to_corner(UL);dela_a.shift(-0.4*RIGHT+0.34*UP)
        


        area11 = area_f_a[2].copy()
        self.play(area11.animate.shift(6*RIGHT+2.2*UP),run_time=2)
        self.wait(4)


        fdiff = BraceBetweenPoints(area11.get_points()[3],area11.get_points()[8],direction=RIGHT,buff=0).set_color(YELLOW)
        self.play(Write(fdiff),run_time=2)
        self.wait(4)

        cal_1 = MathTex("f(x,t+\\Delta t)","-","f(x,t)").scale(0.8)
        cal_1[0].set_color("#6FFF00");cal_1[-1].set_color(YELLOW)
        cal_1.next_to(fdiff)
        self.play(Write(cal_1),run_time=2)
        self.wait(4)

        self.play(ReplacementTransform(VGroup(area1,area2),dela_a),area_f.animate.set_opacity(0.1),run_time=2)
        self.wait(4)

        cal_2 = MathTex("f(x,t+\\Delta t)","=","f(x,t)","+","(\\Delta t)","\\cdot","\\frac{\\partial}{\\partial t}f(x,t)","+","\\cdots").scale(0.7)
        cal_2[0].set_color("#6FFF00")
        cal_2[2].set_color(YELLOW);cal_2[4].set_color(YELLOW);cal_2[-3].set_color("#6FFF00")
        cal_2.next_to(cal_1,DOWN,buff=2)
        cal_2.shift(0.9*LEFT)
        self.play(Write(cal_2),run_time=2)
        self.wait(6)

        cal_3 = MathTex("\\approx","(","\\Delta t",")","\\cdot","\\frac{\\partial}{\\partial t}f(x,t)").set_color(RED)
        cal_3[-1].set_color("#6FFF00");cal_3[2].set_color(YELLOW)
        cal_3.scale(0.9)
        cal_3.next_to(fdiff)
        self.play(ReplacementTransform(VGroup(cal_1,cal_2),cal_3))
        self.wait(5)

        area = MathTex("Area_{(rectangle)}","\\approx","\\frac{\\partial}{\\partial t}f(x,t)","\\Delta t","\\Delta x").set_color(RED)
        area[-2].set_color(YELLOW);area[2].set_color("#6FFF00")
        area.next_to(cal_3,DOWN,buff=1.5)
        area.shift(0.5*LEFT)
        self.play(Write(area),run_time=2)
        self.wait(6)

        total_area = MathTex("\\Delta A","=","\\sum_{a}^{b}","\\frac{\\partial}{\\partial t}f(x,t)","\\Delta t","\\Delta x").set_color(GREEN)
        total_area[0].set_color(RED);total_area[3].set_color("#6FFF00");total_area[4].set_color(YELLOW);total_area[-1].set_color(RED)
        total_area.next_to(area,DOWN)
        total_area.shift(0.4*LEFT)
        self.play(Write(total_area),run_time=2)
        self.wait(6)
        self.play(FadeOut(dela_a),run_time=2)
        self.wait(2)

        damn_time = Tex("Rate of Change of area:").set_color_by_gradient(RED,ORANGE,YELLOW,GREEN,BLUE)
        damn_time.scale(0.9)
        damn_time.move_to(area)
        self.play(ReplacementTransform(area,damn_time),total_area.animate.shift(0.2*UP),run_time=2)
        self.wait(3)
        total_area_change = MathTex("{","\\Delta A","\\over","\\Delta t","}","=","\\sum_{a}^{b}","\\frac{\\partial}{\\partial t}f(x,t)","\\Delta x")
        total_area_change.set_color(GREEN)
        total_area_change[1].set_color(RED);total_area_change[3].set_color(YELLOW);total_area_change[-1].set_color(RED)
        total_area_change[-2].set_color("#6FFF00")
        total_area_change.move_to(total_area)
        self.play(ReplacementTransform(total_area,total_area_change),run_time=2)
        self.wait(7)

        self.play(FadeOut(VGroup(damn_time,fdiff,cal_3,area11,dx_val,dx_val_br,fx_val_br,f_h,fxa_val_br,f_ha,b_line_a,c_line_a)),total_area_change.animate.shift(5*UP),run_time=2)
        self.wait(3)

        as_t = Tex("As $\\Delta$ x $\\to$ 0 :").set_color(YELLOW)
        as_t.next_to(total_area_change,DOWN,buff=2)
        as_t.shift(0.3*RIGHT)
        self.play(Write(as_t),run_time=2)
        self.wait(2)
        print(total_area_change.get_center())
        print(as_t.get_center())


        area_b = self.get_riemann_rectangles(graphf,x_min=b,x_max=c,dx=0.06,input_sample_type="left",stroke_width=0,fill_opacity=0.5,
        start_color=BLUE,
        end_color=BLUE,
        z_index=-3)

        area_r = self.get_riemann_rectangles(graphf_a,x_min=b,x_max=c,dx=0.06,input_sample_type="left",stroke_width=0,fill_opacity=0.5,
        start_color=RED,
        end_color=RED,
        bounded_graph=graphf,
        z_index=-2)

        c_linee = self.get_vertical_line_to_graph(c+0.06,graphf,line_class=DashedLine,z_index=-1).set_color(RED)

        self.play(ReplacementTransform(area_f,area_b),ReplacementTransform(area_f_a,area_r),Transform(c_line,c_linee))
        self.wait()

        # self.play(a1.animate.set_value(0.7),run_time=2)
        # self.wait(3)

        # total_area_change1 = MathTex("{","\\Delta A","\\over","\\Delta t","}","=","\\int_{a}^{b}","\\frac{\\partial}{\\partial t}f(x,t)","d x")
        # total_area_change1.set_color(GREEN)
        # total_area_change1[1].set_color(RED);total_area_change1[3].set_color(YELLOW);total_area_change1[-1].set_color(RED)
        # total_area_change1[-2].set_color("#6FFF00")
        # total_area_change1.next_to(as_t,DOWN)
        # self.play(Write(total_area_change1),run_time=2)
        # self.wait(3)




        


        # feynman = MathTex("\\frac{d}{dt}","\\int_{a}^{b}","f(x,t)","dx = ","\\int_{a}^{b}","\\frac{\\partial}{\\partial t}","f(x,t)","dx").set_color(GREEN)
        # feynman[0].set_color(BLUE);feynman[5].set_color(BLUE)
        # feynman[2].set_color(YELLOW);feynman[-2].set_color("#6FFF00")
        # feynman.next_to(logo,UP,buff=1.5).shift(2.7*LEFT)
        # self.add(feynman)
        # ss = SurroundingRectangle(feynman).set_color(YELLOW)
        # self.add(ss)

        # ch = ImageMobject("cheenta_logo")
        # ch.next_to(feynman,UP)
        # self.add(ch)
class graphs2(GraphScene):
    def construct(self):
        logo = Tex("CHEENTA.COM").set_color_by_gradient(RED,ORANGE,YELLOW,GREEN,BLUE)
        logo.scale(0.6);logo.to_corner(DR);logo.shift(0.4*RIGHT+0.3*DOWN)
        self.add(logo)
        self.x_min=0
        self.x_max=7
        self.x_axis_width=6.5
        self.x_axis_label="x"
        self.y_min=0
        self.y_max=5
        self.y_axis_height=5
        self.y_axis_label="f(x,t)"
        self.axes_color=GREY

        self.graph_origin = DOWN*3.1+LEFT*6.2
        self.include_tip=True
        self.x_axis_config={"include_ticks":True}
        self.y_axis_config={"include_ticks":True}
        # self.x_axis_label_mob.set_color(RED)
        self.setup_axes(animate=False)

        a = 0.5
        b = 0.5; c = 2*PI-0.5
        graphf = self.get_graph(lambda m: np.sin(m)+0.6+0.01*m**3+a, x_min=0,x_max=2*PI,color=YELLOW,stroke_width=6)
        self.add(graphf)
        
        
        b_mark = self.coords_to_point(b-0.2,-0.2); c_mark = self.coords_to_point(c+0.3,-0.2)
        b_tex = Tex("a",color=YELLOW).scale(0.8);c_tex = Tex("b",color=YELLOW).scale(0.8)
        b_tex.move_to(b_mark); c_tex.move_to(c_mark)

        self.add(b_tex,c_tex)

        graphf_lab = self.get_graph_label(graphf,"f(x,t)",x_val=2*PI,color=YELLOW)
        self.add(graphf_lab)


        a1 = ValueTracker(1.5)
        graphf_a = self.get_graph(lambda m: np.sin(m+0.01*a1.get_value())+1+0.01*m**3+a1.get_value(), x_min=0,x_max=2*PI,color="#6FFF00",stroke_width=6)
        graphf_a.add_updater(lambda k: k.become(self.get_graph(lambda m: np.sin(m+0.01*a1.get_value())+1+0.01*m**3+a1.get_value(), x_min=0,x_max=2*PI,color="#6FFF00",stroke_width=6)))
        self.add(graphf_a)

        graphf_a_lab = self.get_graph_label(graphf_a,"f(x,t+\\Delta t)",x_val=2*PI,color="#6FFF00",direction=LEFT)
        graphf_a_lab.add_updater(lambda m:m.become(self.get_graph_label(graphf_a,"f(x,t+\\Delta t)",x_val=2*PI,color="#6FFF00",direction=LEFT)))
        self.add(graphf_a_lab)

        b_line = self.get_vertical_line_to_graph(b,graphf,line_class=DashedLine,z_index=-1).set_color(RED)
        c_linee = self.get_vertical_line_to_graph(c+0.06,graphf,line_class=DashedLine,z_index=-1).set_color(RED)
        self.add(b_line,c_linee)

        total_area_change = MathTex("{","\\Delta A","\\over","\\Delta t","}","=","\\sum_{a}^{b}","\\frac{\\partial}{\\partial t}f(x,t)","\\Delta x")
        total_area_change.set_color(GREEN)
        total_area_change[1].set_color(RED);total_area_change[3].set_color(YELLOW);total_area_change[-1].set_color(RED)
        total_area_change[-2].set_color("#6FFF00")
        total_area_change.move_to([2.50460417,3.14407641,0])
        self.add(total_area_change)

        as_x = Tex("As $\\Delta$ x $\\to$ 0 :").set_color(YELLOW)
        as_x.move_to([2.80460417,0.23976491,0])
        self.add(as_x)

        area_b = self.get_riemann_rectangles(graphf,x_min=b,x_max=c,dx=0.06,input_sample_type="left",stroke_width=0,fill_opacity=0.5,
        start_color=BLUE,
        end_color=BLUE,
        z_index=-3)

        area_r = self.get_riemann_rectangles(graphf_a,x_min=b,x_max=c,dx=0.06,input_sample_type="left",stroke_width=0,fill_opacity=0.5,
        start_color=RED,
        end_color=RED,
        bounded_graph=graphf,
        z_index=-2)

        self.add(area_b,area_r)
        self.add(graphf_a)

        total_area_change1 = MathTex("{","\\Delta A","\\over","\\Delta t","}","=","\\int_{a}^{b}","\\frac{\\partial}{\\partial t}f(x,t)","dx")
        total_area_change1.set_color(GREEN)
        total_area_change1[1].set_color(RED);total_area_change1[3].set_color(YELLOW);total_area_change1[-1].set_color(RED)
        total_area_change1[-2].set_color("#6FFF00")
        total_area_change1.next_to(as_x,DOWN)
        self.play(FadeIn(total_area_change1),run_time=2)
        self.wait(5)
        self.play(FadeOut(total_area_change),total_area_change1.animate.move_to(total_area_change),lag_ratio=0.7)
        self.wait()

        as_t = Tex("As $\\Delta$ t $\\to$ 0 :").set_color(YELLOW)
        as_t.move_to([2.80460417,0.23976491,0])
        self.play(ReplacementTransform(as_x,as_t))
        self.wait(1.5)

        area_r.add_updater(lambda k: k.become(self.get_riemann_rectangles(graphf_a,x_min=b,x_max=c,dx=0.06,input_sample_type="left",stroke_width=0,fill_opacity=0.5,
        start_color=RED,
        end_color=RED,
        bounded_graph=graphf,
        z_index=-2)))
        self.add(area_r)
        self.play(a1.animate.set_value(0.7),run_time=2)
        self.wait()

        total_area_change2 = MathTex("{","dA","\\over","dt","}","=","\\int_{a}^{b}","\\frac{\\partial}{\\partial t}f(x,t)","dx")
        total_area_change2.set_color(GREEN)
        total_area_change2[1].set_color(RED);total_area_change2[3].set_color(YELLOW);total_area_change2[-1].set_color(RED)
        total_area_change2[-2].set_color("#6FFF00")
        total_area_change2.next_to(as_t,DOWN)
        self.play(FadeInFrom(total_area_change2,UP),run_time=2)
        self.wait(2)
        self.play(FadeOut(total_area_change1))
        aaa = SurroundingRectangle(total_area_change2,buff=0.05).set_color(YELLOW)
        self.play(Write(aaa),run_time=1.5)
        A_val = MathTex("A","=","\\int_{a}^{b}","f(x,t)","dx").set_color("#6FFF00")
        A_val[0].set_color(RED);A_val[3].set_color(YELLOW)
        A_val.to_edge(UP);A_val.shift(RIGHT)
        aaaaa = Tex("Leibniz Rule"," ","(","Feynman Trick",")").set_color(GREEN).scale(0.8)
        aaaaa[0].set_color("#6FFF00");aaaaa[-2].set_color(BLUE)
        aaaaa.next_to(aaa,DOWN)
        self.play(FadeIn(VGroup(aaaaa,A_val)))
        self.wait(2.5)
        # self.play(*[FadeOut(i) for i in self.mobjects])
