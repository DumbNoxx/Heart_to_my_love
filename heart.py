from manim import *
import numpy as np
from pydub.playback import play
from pydub import AudioSegment

class Corazon(Scene):
    def construct(self):
        ejes_graph = Axes(
            x_range=[-2,2,0.1],
            y_range=[-1,2,0.1],
            axis_config={"color":WHITE},
            x_length=7,
            y_length=6,
            x_axis_config={
                "tick_size":0.05,
            },
            y_axis_config={
                "tick_size":0.05
            }
        )
        ejes_graph.shift(UP * 1)

        k_kracker = ValueTracker(0.00)
        titulo = Text("¿Quieres volver a intentarlo, Yeickelly?",
                      font_size=48,
                      color=RED)        
        titulo.move_to(ejes_graph.get_bottom()).shift(DOWN * 0.5)
        division_symbol = Text("/", font_size=8).scale(1.5)
        
       
        part1 = Text("(x²)¹", font_size=28, color=WHITE)
        part2 = division_symbol  
        part3 = Text("³ + 0.7 ⋅ sin(k ⋅ x) ⋅ √(3 - x²) = 0", font_size=28, color=WHITE)
        division_symbol.shift(UP * 0.25)
        
        exp = VGroup(part1, part2, part3)
        exp.arrange(RIGHT,buff=0.1)
        exp.move_to(titulo.get_bottom()).shift(DOWN * 0.4)

        k_value_ltx = Text(
            "k = ",
            font_size=38,
            color=WHITE)
        k_value_ltx.move_to(exp.get_bottom()).shift(DOWN * 0.4)
        k_texto = always_redraw(
            lambda: Text(
                f"{k_kracker.get_value():.2f}",
            font_size=28,
            color=WHITE
            ).move_to(k_value_ltx.get_right()).shift(RIGHT * 0.8)
        )
        graph = always_redraw(
            lambda: ejes_graph.plot(
                lambda x: (x**2)**(1/3) + 0.7 * np.sin(k_kracker.get_value() * x) * np.sqrt(3 - x**2),
                x_range=[-np.sqrt(3),np.sqrt(3)],
                color=RED
            )
        )
        self.add_sound("song.mp3")
        for _ in range(2):
            self.play(DrawBorderThenFill(ejes_graph))
            self.play(Create(graph))
            self.play(Write(titulo))
            self.play(Write(exp))
            self.play(Write(k_value_ltx))
            self.play(Write(k_texto))
            self.play(k_kracker.animate.set_value(100.00),run_time=10)
        self.wait(2)

