from manim import *


class AUCPairCountScene(Scene):
    def construct(self):
        title = Text("Why does AUC equal pair wins?", font_size=40).to_edge(UP)
        self.play(Write(title))

        axes = Axes(
            x_range=[0, 1, 0.5],
            y_range=[0, 1, 0.5],
            x_length=5.5,
            y_length=5.5,
            tips=False,
        ).to_edge(LEFT, buff=0.8).shift(0.4 * DOWN)
        axis_labels = axes.get_axis_labels(
            Text("FPR", font_size=30),
            Text("TPR", font_size=30),
        )

        self.play(Create(axes), FadeIn(axis_labels))

        roc_points = [
            (0.0, 0.0),
            (0.0, 1 / 3),
            (0.0, 2 / 3),
            (1 / 2, 2 / 3),
            (1 / 2, 1.0),
            (1.0, 1.0),
        ]

        roc_segments = VGroup()
        for start, end in zip(roc_points, roc_points[1:]):
            roc_segments.add(
                Line(axes.c2p(*start), axes.c2p(*end), color=BLUE, stroke_width=6)
            )

        self.play(LaggedStart(*[Create(seg) for seg in roc_segments], lag_ratio=0.25))

        formula = MathTex(r"AUC = \frac{\text{wins}}{P\times N}", font_size=42)
        formula.to_corner(UR).shift(0.2 * LEFT)
        self.play(Write(formula))

        data_text = VGroup(
            Text("Pos scores: 0.95, 0.80, 0.40", font_size=24),
            Text("Neg scores: 0.70, 0.30", font_size=24),
            Text("Total pairs: 3 × 2 = 6", font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        data_text.next_to(formula, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(FadeIn(data_text, shift=0.2 * DOWN))

        # Each right-step rectangle area corresponds to one negative.
        rect1 = Rectangle(
            width=axes.x_axis.n2p(0.5)[0] - axes.x_axis.n2p(0.0)[0],
            height=axes.y_axis.n2p(2 / 3)[1] - axes.y_axis.n2p(0.0)[1],
            stroke_width=0,
            fill_opacity=0.35,
            color=YELLOW,
        ).move_to(axes.c2p(0.25, 1 / 3))

        rect2 = Rectangle(
            width=axes.x_axis.n2p(1.0)[0] - axes.x_axis.n2p(0.5)[0],
            height=axes.y_axis.n2p(1.0)[1] - axes.y_axis.n2p(0.0)[1],
            stroke_width=0,
            fill_opacity=0.35,
            color=GREEN,
        ).move_to(axes.c2p(0.75, 0.5))

        note1 = Text("For neg 0.70: 2 positives above it", font_size=24, color=YELLOW).next_to(
            data_text, DOWN, aligned_edge=LEFT, buff=0.25
        )
        note2 = Text("For neg 0.30: 3 positives above it", font_size=24, color=GREEN).next_to(
            note1, DOWN, aligned_edge=LEFT, buff=0.16
        )

        self.play(FadeIn(rect1), Write(note1))
        self.play(FadeIn(rect2), Write(note2))

        wins = MathTex(r"\text{wins} = 2 + 3 = 5", font_size=38).next_to(note2, DOWN, aligned_edge=LEFT, buff=0.35)
        auc_value = MathTex(r"AUC = \frac{5}{6} \approx 0.833", font_size=42, color=GOLD).next_to(
            wins, DOWN, aligned_edge=LEFT, buff=0.25
        )
        self.play(Write(wins))
        self.play(Write(auc_value))

        takeaway = Text("AUC = chance a random positive outranks a random negative", font_size=26)
        takeaway.to_edge(DOWN)
        self.play(FadeIn(takeaway, shift=0.2 * UP))
        self.wait(2)
