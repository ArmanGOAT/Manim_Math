from manim import *

class DifferentialEquation(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Создание объектов
        title = Text("Problem (d)", font_size=48).set_color(BLUE_E).to_edge(UP * 1.1)
        substitution_text = Text("Let’s make substitutions:", font_size=36).set_color(BLUE_E).to_edge(UP * 1.1)
        substitution_equation = MathTex(r"\frac{x}{y} = t \Rightarrow y = \frac{x}{t}").set_color(BLUE_E).scale(1.0).next_to(substitution_text, DOWN, buff=0.5)
        substitution_equation2 = MathTex(r"\frac{dy}{dx} = \frac{d}{dx}\left(\frac{x}{t}\right)").set_color(BLUE_E).next_to(substitution_equation, DOWN)
        equation = MathTex(r"(d)\quad \frac{dy}{dx} = \frac{-x + \sqrt{x^2 + y^2}}{y}").set_color(BLUE_E).scale(0.8).next_to(title, DOWN, buff=0.5)
        equation1 = MathTex(r"\frac{dy}{dx} = -\frac{x}{y} + \sqrt{\left(\frac{x}{y}\right)^2 + 1}").set_color(BLUE_E).scale(0.8).next_to(equation, DOWN, buff=0.5)
        substitution_equation3 = MathTex(r"\frac{dy}{dx} = \frac{t - \frac{dt}{dx} \cdot x}{t^2}").set_color(BLUE_E).next_to(substitution_equation, DOWN)
        changed_equation1 = MathTex(r"\frac{t - \frac{dt}{dx}\cdot x}{t^{2}} = -t + \sqrt{t^{2}+1}").set_color(BLUE_E)
        changed_equation2 = MathTex(r"t - \frac{dt}{dx}\cdot x = -t^{3}+t^{2}\sqrt{t^{2}+1}").set_color(BLUE_E)

        # Определение функции для замены
        def substitution1():
            self.play(Write(substitution_text))
            self.wait(1)
            self.play(Write(substitution_equation), run_time=3)
            self.wait(1)
            self.play(Write(substitution_equation2))
            self.wait(2)
            self.play(Transform(substitution_equation2, substitution_equation3))
            self.wait(2)

        # Анимации
        self.play(Write(title))
        self.wait(1)

        self.play(Write(equation), run_time=4)
        self.wait(2)

        self.play(FadeOut(title))
        text1 = Text("So let’s solve it", font_size=44).set_color(BLUE_E).to_edge(UP)
        self.play(Write(text1))
        self.wait(2)

        self.play(FadeOut(text1))
        self.play(equation.animate.shift(UP))
        self.wait(2)

        extra_equation = equation.copy()

        # Трансформация уравнения
        self.play(Transform(extra_equation, equation1), run_time=1.3)
        self.wait(2)

        # Удаление лишних уравнений
        self.remove(extra_equation, equation)

        self.play(equation1.animate.shift(DOWN))

        # Вызов замены
        substitution1()

        self.play(
            FadeOut(substitution_text),
            substitution_equation.animate.scale(0.5).shift(LEFT * 5).to_edge(UP),  
            run_time=4
        )

        # Убедитесь, что удаляете корректный объект
        self.remove(substitution_equation2)
        self.play(FadeOut(substitution_equation3))

        # Трансформация уравнений и анимации
        self.play(Transform(equation1, changed_equation1), run_time=2)
        self.wait(1)

        # Удаление объекта, который больше не нужен
        self.remove(equation1)

        changed_equation_copy = changed_equation1.copy()

        self.play(Transform(changed_equation_copy, changed_equation2), run_time=3)
        self.wait(1)

        self.remove(changed_equation_copy)

        # Дальнейшие трансформации
        changed_equation3 = MathTex(r"\frac{dt}{dx}\cdot x = t+t^{3}-t^{2}\sqrt{t^{2}+1}").set_color(BLUE_E)
        self.play(Transform(changed_equation2, changed_equation3))

        changed_equation4 = MathTex(r"\frac{dt}{t+t^{3}-t^{2}\sqrt{t^{2}+1}} = \frac{dx}{x}").set_color(BLUE_E)
        self.remove(changed_equation2)
        self.play(Transform(changed_equation3, changed_equation4), run_time=3)
        self.remove(changed_equation3)
        self.play(changed_equation4.animate.shift(UP * 2))
        self.wait(2)

        # Работа с интегралами
        integrals_text = Text("We get 2 integrals:", font_size=30).set_color(BLUE_E).next_to(changed_equation4, DOWN * 1.3)
        self.play(Write(integrals_text), run_time=2)
        integrals = MathTex(r"I_{1} = \int \frac{dt}{t+t^{3}-t^{2}\sqrt{t^{2}+1}}\quad and \quad I_{2} = \int \frac{dx}{x}").set_color(BLUE_E).next_to(integrals_text, DOWN * 1.3)
        self.play(Write(integrals))
        self.wait(2)

        self.play(Uncreate(changed_equation4), Uncreate(integrals_text), Uncreate(substitution_equation))
        self.play(integrals.animate.to_edge(UP, buff=0.7))

        # Интегралы
        integral_2 = MathTex(r"I_{2}\quad case: \quad \int \frac{dx}{x} = ln|x| + C_{2} = ln(e^{C_{2}}x)").set_color(BLUE_E).scale(0.7)
        self.wait(3)
        self.play(Write(integral_2))

        integral_1 = MathTex(r"I_{1}\quad case: \quad \int \frac{dt}{t+t^{3}-t^{2}\sqrt{t^{2}+1}} = \int \frac{dt}{t\sqrt{t^{2}+1}\left(\sqrt{t^{2}+1}-t\right)}").set_color(BLUE_E).scale(0.7)
        self.play(Uncreate(integrals))
        self.play(integral_2.animate.to_edge(UP, buff=0.6))
        self.wait(1)

        self.play(Write(integral_1), run_time=5)
        self.play(FadeOut(integral_2))
        self.play(integral_1.animate.to_edge(UP, buff=0.6))
        self.wait(2)

        integral_substatution1 = Text("Another Substitution:", font_size=30).set_color(BLUE_E).next_to(integral_1, DOWN, buff=0.5)
        integral_1_0 = MathTex(r"t = tanu \quad dt = d(tanu) = \frac{du}{cos^{2}u}").set_color(BLUE_E).scale(0.7).next_to(integral_substatution1, DOWN, buff=0.5)
        integral_1_1 = MathTex(r"Note: \quad 1+tan^{2}u = \frac{1}{cos^{2}u}").set_color(BLUE_E).scale(0.7).next_to(integral_1_0, DOWN, buff=0.5)

        self.play(Write(integral_substatution1), Write(integral_1_0), Write(integral_1_1), run_time=6)

        self.play(FadeOut(integral_1))
        self.play(integral_substatution1.animate.to_edge(UP, buff=0.6), integral_1_0.animate.shift(UP * 1.5), integral_1_1.animate.shift(UP * 1.6))
        self.wait(3)

        integral_1_2 = MathTex(r"\Rightarrow \quad  \int \frac{\frac{du}{cos^{2}u}}{tanu\cdot\frac{1}{cosu}\cdot\left(\frac{1}{cosu}-tanu\right)}").set_color(BLUE_E).scale(0.7).next_to(integral_1_1, DOWN, buff=0.5)
        self.play(Write(integral_1_2))
        self.wait(2)

        integral_1_3 = MathTex(r" \int \frac{\frac{du}{cos^{2}u}}{\frac{sinu}{cos^{2}u}\cdot\left(\frac{1}{cosu}-tanu\right)}").set_color(BLUE_E).scale(0.7)
        self.play(Transform(integral_1_2, integral_1_3), run_time=3)
        integral_1_4 = MathTex(r"\int \frac{cosudu}{sinu(1-sinu)}").set_color(BLUE_E).scale(0.7)
        integral_1_5 = MathTex(r" \int \frac{dsinu}{sinu(1-sinu)}").set_color(BLUE_E).scale(0.7)
        integral_1_6 = MathTex(r" \int \frac{dsinu}{sinu}+\int \frac{dsinu}{1-sinu}").set_color(BLUE_E).scale(0.7)
        self.wait(2)
        self.remove(integral_1_2)
        self.play(Transform(integral_1_3, integral_1_4), run_time=3)
        self.wait(2)
        self.remove(integral_1_3)
        self.play(Transform(integral_1_4, integral_1_5), run_time=3)
        self.remove(integral_1_4)
        self.wait(2)
        self.play(Transform(integral_1_5, integral_1_6), run_time=3)
        self.wait(2)

        final_integral = MathTex(r"\Rightarrow ln|sinu| - ln|1-sinu| + C_{1}").set_color(BLUE_E).scale(0.7).next_to(integral_1_6, DOWN, buff=0.5)
        self.play(Write(final_integral), run_time=2)
        self.play(FadeOut(integral_1_5))
        self.play(FadeOut(integral_1_6), FadeOut(integral_substatution1), FadeOut(integral_1_0), FadeOut(integral_1_1))
        self.play(final_integral.animate.to_edge(UP, buff=0.7))

        final_sub = MathTex(r"We \quad know \quad that \quad t = tanu,\quad so \quad u = tan^{-1}t \quad \\ and \quad sinu = sin(tan^{-1}t)\quad which\quad equals \quad to \quad \frac{t}{\sqrt{t^{2}+1}}").set_color(BLUE_E).scale(0.7).next_to(final_integral, DOWN, buff=0.5)
        self.play(Write(final_sub), run_time=4)
        final_integral2 = MathTex(r"Therefore,\quad I_{1} = ln\left|\frac{t}{\sqrt{t^{2}+1}}\right| - ln\left|\frac{t}{\sqrt{t^{2}+1}} - 1\right| + lne^{C_{1}} = ln(e^{C_1}\frac{t}{t-\sqrt{t^{2}+1}})").set_color(BLUE_E).scale(0.7).next_to(final_sub, DOWN, buff=0.5)
        self.play(Write(final_integral2), run_time = 3)
        self.wait(2)


        self.play(FadeOut(final_integral), FadeOut(final_integral2), FadeOut(final_sub))

        final_text = MathTex(r"Finally \quad I_{1} = I_{2}: \quad ln(e^{C_1}\frac{t}{t-\sqrt{t^{2}+1}}) = ln(e^{C_{2}}x)").set_color(BLUE_E).scale(0.7).to_edge(UP, buff=0.7)
        log_equation = MathTex(r"e^{C_1}\frac{t}{t-\sqrt{t^{2}+1}} = e^{C_{2}}x \quad let\quad switch\quad back\quad (t = \frac{x}{y})").set_color(BLUE_E).scale(0.7).next_to(final_text, DOWN, buff=0.5)
        last_sub = Text("After putting x/y instead t:").set_color(BLUE_E).scale(0.7).to_edge(UP, buff=0.7)
        basic_equation = MathTex(r"e^{C_1} \cdot \frac{x}{y} = e^{C_2} \cdot x \left( \frac{x}{y} - \sqrt{\left(\frac{x}{y}\right)^2 + 1} \right) ").set_color(BLUE_E).scale(0.7)
        last_text = Text("After basic calculations, we get: ").set_color(BLUE_E).scale(0.7).to_edge(UP, buff=0.7)
        answer = MathTex(r"y^2 = e^{C_1 - 2C_2} \left(e^{C_1} - 2e^{C_2}x \right)").set_color(BLUE_E).scale(0.7).next_to(basic_equation, DOWN, buff=0.7)


        self.play(Write(final_text), run_time = 4)
        self.play(Transform(final_text, log_equation))
        self.wait(2)
        self.play(Write(last_sub))
        self.wait(2)
        self.play(Transform(log_equation, basic_equation))
        self.play(FadeOut(last_sub))
        self.wait(2)
        self.play(Write(last_text))
        self.play(Write(answer))
        self.wait(2)
        self.play(FadeOut(final_text))
        self.play(FadeOut(log_equation))
        self.play(FadeOut(basic_equation))
        self.wait(2)
        self.play(answer.animate.shift(UP*2).scale(1.5), run_time = 2)
        answer_box = SurroundingRectangle(answer, color=BLUE, buff=0.2)
        self.play(Create(answer_box), run_time = 2)
        self.wait(3)



        