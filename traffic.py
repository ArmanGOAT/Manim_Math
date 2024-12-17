from manim import *

class TrafficFlow(Scene):
    def construct(self):
        
        heading = Text("Network flow of Baltimore streets").to_edge(UP)
        point_A = LEFT * 1.5 + DOWN * 3
        point_B = LEFT * 1.5  # B
        point_C = RIGHT * 1.5  # C
        point_D = RIGHT * 1.5 + DOWN * 3

        dot_A = Dot(point_A)
        dot_B = Dot(point_B)
        dot_C = Dot(point_C)
        dot_D = Dot(point_D)

        label_A = Text("A").move_to([-1,-1,0]).scale(0.7)
        label_B = Text("B").move_to([-1,2,0]).scale(0.7)
        label_C = Text("C").move_to([2,2,0]).scale(0.7)
        label_D = Text("D").move_to([2,-1,0]).scale(0.7)


        nodes = VGroup(dot_A, dot_B, dot_C, dot_D).move_to(ORIGIN)
        labels = VGroup(label_A, label_B, label_C, label_D)

        hor_out_B = Line(start = np.array([4.5,1.5,0]), end = np.array([-4.5,1.5,0]), color = WHITE)
        hor_out_D = Line(start = np.array([4.5,-1.5,0]), end = np.array([-4.5,-1.5,0]), color = WHITE)
        vert_out_B = Line(start = np.array([-1.5,-3.5,0]), end = np.array([-1.5,3.5,0]), color = WHITE)
        vert_out_D = Line(start = np.array([1.5,3.5,0]), end = np.array([1.5,-3.5,0]), color = WHITE)

        x1_arrow = Arrow(start = np.array([-1.5,-1.5,0]), end = np.array([0,-1.5,0]), color = WHITE, buff=-0.5)
        x2_arrow = Arrow(start = np.array([-1.5,-1.5,0]), end = np.array([-1.5,0,0]), color = WHITE, buff=-0.5)
        x3_arrow = Arrow(start = np.array([-1.5,2,0]), end = np.array([-1.5,3.5,0]), color = WHITE, buff=0)
        x4_arrow = Arrow(start = np.array([1.5,1.5,0]), end = np.array([0,1.5,0]), color = WHITE, buff=-0.5)
        x5_arrow = Arrow(start = np.array([1.5,1.5,0]), end = np.array([1.5,0,0]), color = WHITE, buff=-0.5)
        arrow300out = Arrow(start = np.array([-2, 1.5, 0]), end = np.array([-4,1.5,0]), color = WHITE, buff=0)
        arrow300in = Arrow(start = np.array([-4.5, -1.5, 0]), end = np.array([-3,-1.5,0]), color = WHITE, buff=0)
        arrow500in = Arrow(start = np.array([-1.5,-3.5,0]), end = np.array([-1.5, -2, 0]), color = WHITE, buff=0)
        arrow100in = Arrow(start = np.array([1.5, 3.5, 0]), end = np.array([1.5, 2, 0]), color = WHITE, buff=0)
        arrow400in = Arrow(start = np.array([4.5, 1.5, 0]), end = ([3, 1.5, 0]), color = WHITE, buff=0)
        arrow600out = Arrow(start = np.array([3, -1.5, 0]), end = ([4.5, -1.5, 0]), color = WHITE, buff=0)

        number_300 = Text("300").move_to([-4, 2, 0]).scale(0.6)
        number_300_2 = Text("300").move_to([-3, -1, 0]).scale(0.6)
        number_100 = Text("100").move_to([2, 3, 0]).scale(0.6)
        number_400 = Text("400").move_to([4, 2, 0]).scale(0.6)
        number_600 = Text("600").move_to([4,-1, 0]).scale(0.6)
        number_500 = Text("500").move_to([-1, -2.5, 0]).scale(0.6)

        var_x1 = MathTex(r"x_{1}").move_to([0, -2, 0])
        var_x2 = MathTex(r"x_{2}").move_to([-2, 0, 0])
        var_x3 = MathTex(r"x_{3}").move_to([-1, 3, 0])
        var_x4 = MathTex(r"x_{4}").move_to([0, 1, 0])
        var_x5 = MathTex(r"x_{5}").move_to([2, 0, 0])

        numbers_variables = VGroup(number_300, number_300_2, number_100, number_400, number_500, number_600, var_x1, var_x2, var_x3, var_x4, var_x5)

        variable_arrow = VGroup(x1_arrow, x2_arrow, x3_arrow, x4_arrow, x5_arrow, arrow300out, arrow300in, arrow500in, arrow400in, arrow100in, arrow600out)

        diagram = VGroup(nodes, labels, hor_out_B, hor_out_D, vert_out_B, vert_out_D, variable_arrow, numbers_variables)

        diagram.scale(0.6).shift(LEFT * 3)

        self.play(Write(heading))
        self.play(Write(dot_A),  Write(dot_B),  Write(dot_C),  Write(dot_D), run_time = 1.5)
        self.play(Write(hor_out_B), Write(hor_out_D), Write(vert_out_B), Write(vert_out_D))
        self.play(Write(labels), Write(variable_arrow), Write(numbers_variables))
        self.wait(2)

        text_rule1 = Text("A network consist of 4 points, which \nare called 'Junctions' or 'Nodes'.").scale(0.5).next_to(number_100, RIGHT, buff=2)
        text_rule2 = Text("The main assumption of network is:").scale(0.5).next_to(text_rule1, DOWN, buff=1)
        text_rule3 = MathTex(r"\sum flow\ in = \sum flow\ out").scale(0.6).next_to(text_rule2, DOWN ,buff=0.5)
        boxed_rule = SurroundingRectangle(text_rule3, color=YELLOW_E, buff=0.2)
        
        self.play(Write(text_rule1), run_time = 2)
        self.play(text_rule1.animate.set_color(YELLOW), nodes.animate.set_color(YELLOW_E), labels.animate.scale(1).set_color(YELLOW_E), run_time = 3)
        self.play(text_rule1.animate.set_color(WHITE), nodes.animate.set_color(WHITE), labels.animate.scale(1).set_color(WHITE))
        self.wait(2)
        self.play(Write(text_rule2), Write(text_rule3))
        self.play(Create(boxed_rule), run_time= 2)
        self.wait(2)

        rule = VGroup(boxed_rule, text_rule3)

        self.play(rule.animate.next_to(diagram, DOWN), FadeOut(text_rule1), FadeOut(text_rule2), run_time = 2)
        self.wait(1)

        solution_text = Text("Solution:").to_edge(UP)

        self.play(Uncreate(heading))
        self.play(Write(solution_text))
        self.wait(1)

        node_a = MathTex("Node \ A: \ ","300+500", "=", "x_{1}+x_{2}").scale(0.7).next_to(number_100, RIGHT, buff = 2.5)
        nodeA = VGroup(dot_A, label_A, arrow300in, arrow500in, number_300_2, number_500)
        nodeA2 = VGroup(dot_A, label_A, x1_arrow, x2_arrow, var_x1, var_x2)

        node_b = MathTex("Node \ B: \ ","x_{2}+x_{4}", "=", "300+x_{3}").scale(0.7).next_to(node_a, DOWN, buff = 0.6)
        nodeB = VGroup(dot_B, label_B, x2_arrow, x4_arrow, var_x2, var_x4)
        nodeB2 = VGroup(dot_B, label_B, number_300, arrow300out, var_x3, x3_arrow)

        node_c = MathTex("Node \ C: \ ","100+400", "=", "x_{4}+x_{5}").scale(0.7).next_to(node_b, DOWN, buff = 0.6)
        nodeC = VGroup(dot_C, label_C, arrow400in, arrow100in, number_400, number_100)
        nodeC2 = VGroup(dot_C, label_C, x4_arrow, x5_arrow, var_x4, var_x5)

        node_d = MathTex("Node \ D: \ ","x_{1}+x_{5}", "=", "600").scale(0.7).next_to(node_c, DOWN, buff = 0.6)
        nodeD = VGroup(dot_D, label_D, x1_arrow, x5_arrow, var_x1, var_x5)
        nodeD2 = VGroup(dot_D, label_D, number_600, arrow600out)

        node_b.align_to(node_a, LEFT)
        node_c.align_to(node_a, LEFT)
        node_d.align_to(node_a, LEFT)

        total_text = Text("Also, the total flow: ").scale(0.7).next_to(node_d, DOWN, buff=0.6)
        total_equation = MathTex("500+300+100+400", "=", "300+x_{3}+600").scale(0.7).next_to(total_text, DOWN)
        total_in = VGroup(number_500, number_300, number_100, number_400, arrow500in, arrow400in, arrow100in, arrow300in)
        total_out = VGroup(number_300_2, number_600, var_x3, arrow300out, arrow600out, x3_arrow)
        total_text.align_to(node_a, LEFT)

        self.play(Write(node_a[0]),dot_A.animate.set_color(YELLOW_E), label_A.animate.set_color(YELLOW_E), run_time = 2)
        self.play(dot_A.animate.set_color(WHITE), label_A.animate.set_color(WHITE))
        self.wait(1)
        self.play(nodeA.animate.set_color(YELLOW_E), Write(node_a[1]), run_time = 3)
        self.play(nodeA.animate.set_color(WHITE), Write(node_a[2]))
        self.play(nodeA2.animate.set_color(YELLOW_E), Write(node_a[3]), run_time = 2)
        self.play(nodeA2.animate.set_color(WHITE))
        self.wait(1)
        

        self.play(Write(node_b[0]),dot_B.animate.set_color(YELLOW_E), label_B.animate.set_color(YELLOW_E), run_time = 2)
        self.play(dot_B.animate.set_color(WHITE), label_B.animate.set_color(WHITE))
        self.wait(1)
        self.play(nodeB.animate.set_color(YELLOW_E), Write(node_b[1]), run_time = 3)
        self.play(nodeB.animate.set_color(WHITE), Write(node_b[2]))
        self.play(nodeB2.animate.set_color(YELLOW_E), Write(node_b[3]), run_time = 2)
        self.play(nodeB2.animate.set_color(WHITE))
        self.wait(1)


        self.play(Write(node_c[0]),dot_C.animate.set_color(YELLOW_E), label_C.animate.set_color(YELLOW_E), run_time = 2)
        self.play(dot_C.animate.set_color(WHITE), label_C.animate.set_color(WHITE))
        self.wait(1)
        self.play(nodeC.animate.set_color(YELLOW_E), Write(node_c[1]), run_time = 3)
        self.play(nodeC.animate.set_color(WHITE), Write(node_c[2]))
        self.play(nodeC2.animate.set_color(YELLOW_E), Write(node_c[3]), run_time = 2)
        self.play(nodeC2.animate.set_color(WHITE))
        self.wait(1)


        self.play(Write(node_d[0]),dot_D.animate.set_color(YELLOW_E), label_D.animate.set_color(YELLOW_E), run_time = 2)
        self.play(dot_D.animate.set_color(WHITE), label_D.animate.set_color(WHITE))
        self.wait(1)
        self.play(nodeD.animate.set_color(YELLOW_E), Write(node_d[1]), run_time = 3)
        self.play(nodeD.animate.set_color(WHITE), Write(node_d[2]))
        self.play(nodeD2.animate.set_color(YELLOW_E), Write(node_d[3]), run_time = 2)
        self.play(nodeD2.animate.set_color(WHITE))
        self.wait(1)


        self.play(Write(total_text), run_time = 2)
        self.play(Write(total_equation[0]), total_in.animate.set_color(YELLOW_E), run_time = 2)
        self.play(total_in.animate.set_color(WHITE), Write(total_equation[1]))
        self.play(Write(total_equation[2]), total_out.animate.set_color(YELLOW), run_time = 3)
        self.play(total_out.animate.set_color(WHITE))
        self.wait(4)

        x3_solution = MathTex("x_{3} = 400").scale(0.7).next_to(total_text, DOWN)
        x3_solution.align_to(node_a, LEFT)
        self.play(ReplacementTransform(total_equation, x3_solution))


        # system = VGroup(node_a[1:],node_b[1:], node_c[1:], node_d[1:], x3_solution)
        # system.arrange(DOWN, aligned_edge = LEFT)

        system_r1 = MathTex("x_{1}+x_{2}"," = ", "800").scale(0.7).to_edge(UP+LEFT, buff=1)
        system_r2 = MathTex("x_{2}-x_{3}+x_{4}", " = ", "300").scale(0.7).next_to(system_r1, DOWN)
        system_r3 = MathTex("x_{4}+x_{5}", "=", "500").scale(0.7).next_to(system_r2, DOWN)
        system_r4 = MathTex("x_{1}+x_{5}", "=", "600").scale(0.7).next_to(system_r3, DOWN)
        system_r5 = MathTex("x_{3}", "=", "400").scale(0.7).next_to(system_r4, DOWN)

        system_r2.align_to(system_r1, LEFT)
        system_r3.align_to(system_r1, LEFT)
        system_r4.align_to(system_r1, LEFT)
        system_r5.align_to(system_r1, LEFT)


        self.play(FadeOut(node_a[0]), FadeOut(node_b[0]), FadeOut(node_c[0]), FadeOut(node_d[0]), FadeOut(total_text), FadeOut(diagram), FadeOut(rule), FadeOut(solution_text), x3_solution.animate.align_to(node_a[1], LEFT))
    
        self.wait(2)
        # self.play(system.animate.to_edge(UP + LEFT, buff=1))
        self.play(ReplacementTransform(node_a[1:], system_r1))
        self.play(ReplacementTransform(node_b[1:], system_r2))
        self.play(ReplacementTransform(node_c[1:], system_r3))
        self.play(ReplacementTransform(node_d[1:], system_r4))
        self.play(ReplacementTransform(x3_solution, system_r5))

        system = VGroup(system_r1, system_r2, system_r3, system_r4, system_r5).to_edge(UP+LEFT, buff=1)
        
        augmented_matrix = Matrix([[1, 1, 0, 0, 0, 800], [0, 1, -1, 1, 0, 300], [0, 0, 0, 1, 1, 500], [1, 0, 0, 0, 1, 600], [0, 0, 1, 0, 0, 400]]).scale(0.7).next_to(system, RIGHT, buff=1)
        self.play(ReplacementTransform(system.copy(), augmented_matrix), run_time=2)
        self.wait(2)
        self.play(FadeOut(system))
        self.play(augmented_matrix.animate.to_edge(UP+LEFT, buff=1))

        rightArrow = MathTex("\Rightarrow").scale(1.2).next_to(augmented_matrix.get_rows()[2], RIGHT*1.5)

        self.play(Write(rightArrow))

        matrix = augmented_matrix.next_to(rightArrow, RIGHT)

        self.play(ReplacementTransform(augmented_matrix.copy(), matrix))

        row_op1 = MathTex("R_{4} = R_{4}-R_{1}").to_edge(DOWN, buff = 2)
        row_op2 = MathTex("R_{1} = R_{1}-R_{2}").to_edge(DOWN, buff = 2)
        row_op3 = MathTex("R_{4} = R_{4}+R_{2}").to_edge(DOWN, buff = 2)
        row_op4 = MathTex("R_{3} \leftrightarrow R_{4}").to_edge(DOWN, buff = 2)
        row_op5 = MathTex("R_{3} = -R_{3}").to_edge(DOWN, buff = 2)
        row_op6 = MathTex("R_{1} = R_{1}-R_{3}").to_edge(DOWN, buff = 2)
        row_op7 = MathTex("R_{2} = R_{2}+R_{3}").to_edge(DOWN, buff = 2)
        row_op8 = MathTex("R_{5} = R_{5}-R_{3}").to_edge(DOWN, buff = 2)
        row_op9 = MathTex("R_{3} = R_{3}+R_{4}").to_edge(DOWN, buff = 2)
        row_op10 = MathTex("R_{5} = R_{5}-R_{4}").to_edge(DOWN, buff = 2)

        new_row4 = Matrix([[0, -1, 0, 0, 1, 200]]).scale(0.7)
        left_bracket = new_row4.get_brackets()[0]  # левая скобка
        left_bracket.set_opacity(0)
        right_bracket = new_row4.get_brackets()[1]  
        right_bracket.set_opacity(0)
        new_row4.move_to(matrix.get_rows()[3])


        new_row1 = Matrix([[1, 0, 1, -1, 0, 500]]).scale(0.7)
        left_bracket = new_row1.get_brackets()[0]
        left_bracket.set_opacity(0)
        right_bracket = new_row1.get_brackets()[1]  
        right_bracket.set_opacity(0)
        new_row1.move_to(matrix.get_rows()[0])


        new_row4_2 = Matrix([[0, 0, -1, 1, 1, 100]]).scale(0.7)
        left_bracket = new_row4_2.get_brackets()[0]
        left_bracket.set_opacity(0)
        right_bracket = new_row4_2.get_brackets()[1]  
        right_bracket.set_opacity(0)
        new_row4_2.move_to(matrix.get_rows()[3])



        self.play(Write(row_op1))
        self.wait(1)
        self.play(ReplacementTransform(matrix.get_rows()[3], new_row4))
        self.wait(2)

        self.play(ReplacementTransform(row_op1, row_op2))
        self.wait(1)
        self.play(ReplacementTransform(matrix.get_rows()[0], new_row1))
        self.wait(2)

        #R4 = R4+R2
        self.play(ReplacementTransform(row_op2, row_op3))
        self.wait(1)
        self.play(ReplacementTransform(new_row4, new_row4_2))
        self.wait(2)

        #R3 = R4 interchange
        new_row3 = Matrix([[0, 0, -1, 1, 1, 100]]).scale(0.7)
        new_row4_3 = Matrix([[0, 0, 0, 1, 1, 500]]).scale(0.7)
        left_bracket = new_row4_3.get_brackets()[0]
        left_bracket.set_opacity(0)
        right_bracket = new_row4_3.get_brackets()[1]  
        right_bracket.set_opacity(0)
        left_bracket = new_row3.get_brackets()[0]
        left_bracket.set_opacity(0)
        right_bracket = new_row3.get_brackets()[1]  
        right_bracket.set_opacity(0)
        new_row3.move_to(matrix.get_rows()[2])
        new_row4_3.move_to(matrix.get_rows()[3])
        self.play(ReplacementTransform(row_op3, row_op4))
        self.wait(1)
        self.play(ReplacementTransform(matrix.get_rows()[2], new_row3), ReplacementTransform(new_row4_2, new_row4_3))
        self.wait(2)

        #R3 = -R3
        new_row3_2 = Matrix([[0,0,1,-1,-1,-100]]).scale(0.7)
        left_bracket = new_row3_2.get_brackets()[0]
        left_bracket.set_opacity(0)
        right_bracket = new_row3_2.get_brackets()[1]  
        right_bracket.set_opacity(0)
        new_row3_2.move_to(matrix.get_rows()[2])
        self.play(ReplacementTransform(row_op4, row_op5))
        self.wait(1)
        self.play(ReplacementTransform(new_row3, new_row3_2))
        self.wait(2)


        #R1 = R1 - R3
        new_row1_2 = Matrix([[1, 0, 0, 0, 1, 600]]).scale(0.7)
        left_bracket = new_row1_2.get_brackets()[0]
        left_bracket.set_opacity(0)
        right_bracket = new_row1_2.get_brackets()[1]  
        right_bracket.set_opacity(0)
        new_row1_2.move_to(matrix.get_rows()[0])
        self.play(ReplacementTransform(row_op5, row_op6))
        self.wait(1)
        self.play(ReplacementTransform(new_row1, new_row1_2))
        self.wait(2)

        #R2 = R2 + R3
        new_row2 = Matrix([[0,1,0,0,-1,200]]).scale(0.7)
        left_bracket = new_row2.get_brackets()[0]
        left_bracket.set_opacity(0)
        right_bracket = new_row2.get_brackets()[1]  
        right_bracket.set_opacity(0)
        new_row2.move_to(matrix.get_rows()[1])
        self.play(ReplacementTransform(row_op6, row_op7))
        self.wait(1)
        self.play(ReplacementTransform(matrix.get_rows()[1], new_row2))
        self.wait(2)

        #R5 = R5-R3
        new_row5 = Matrix([[0,0,0,1,1,500]]).scale(0.7)
        left_bracket = new_row5.get_brackets()[0]
        left_bracket.set_opacity(0)
        right_bracket = new_row5.get_brackets()[1]  
        right_bracket.set_opacity(0)
        new_row5.move_to(matrix.get_rows()[4])
        self.play(ReplacementTransform(row_op7, row_op8))
        self.wait(1)
        self.play(ReplacementTransform(matrix.get_rows()[4], new_row5))
        self.wait(2)

        #R3 = R3+R4
        new_row3_3 = Matrix([[0,0,1,0,0,400]]).scale(0.7)
        left_bracket = new_row3_3.get_brackets()[0]
        left_bracket.set_opacity(0)
        right_bracket = new_row3_3.get_brackets()[1]  
        right_bracket.set_opacity(0)
        new_row3_3.move_to(matrix.get_rows()[2])
        self.play(ReplacementTransform(row_op8, row_op9))
        self.wait(1)
        self.play(ReplacementTransform(new_row3_2, new_row3_3))
        self.wait(2)

        #R5 = R5 - R4
        new_row5_1 = Matrix([[0,0,0,0,0,0]]).scale(0.7)
        left_bracket = new_row5_1.get_brackets()[0]
        left_bracket.set_opacity(0)
        right_bracket = new_row5_1.get_brackets()[1]  
        right_bracket.set_opacity(0)
        new_row5_1.move_to(matrix.get_rows()[4])
        self.play(ReplacementTransform(row_op9, row_op10))
        self.wait(1)
        self.play(ReplacementTransform(new_row5, new_row5_1))
        self.wait(2)

        final_text = Text("Finally, we got rref").scale(0.8).to_edge(DOWN, buff=2)
        self.play(FadeOut(row_op10))
        self.play(Write(final_text))

        boxed_matrix = SurroundingRectangle(matrix, color=YELLOW_E, buff=0.2)
        self.play(Create(boxed_matrix))

        self.play(Uncreate(rightArrow), Uncreate(boxed_matrix))
        self.wait(1)

        answer_text = Text("Therefore, the answer is: ").scale(0.8).to_edge(DOWN, buff=2)
        answer = MathTex(r"x_{1} &= 600 - x_{5} \\ x_{2} &= 200 + x_{5} \\ x_{3} &= 400 \\ x_{4} &= 500 - x_{5} \\ x_{5} \quad &\text{is free}, \quad x_{5} \leq 500").scale(0.7).to_edge(UP + LEFT, buff=1)


        self.play(Uncreate(final_text))
        self.play(Write(answer_text), Write(answer))

        boxed_answer = SurroundingRectangle(answer, color=YELLOW_E, buff=0.6)

        self.play(Write(boxed_answer))



        