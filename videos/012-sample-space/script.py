from manim import *
import numpy as np

BG = "#191919"
PRIMARY = "#2D4263"
SECONDARY = "#C84B31"
ACCENT = "#ECDBBA"

MONO = "DejaVu Sans Mono"

TITLE_SIZE = 48
LABEL_SIZE = 28
CAPTION_SIZE = 22


class Scene1_DartboardAnalogy(Scene):
    def construct(self):
        self.camera.background_color = BG

        board_center = ORIGIN

        title = Text("SAMPLE SPACE & EVENTS", font_size=34, font=MONO, color=ACCENT, weight=BOLD)
        subtitle = Text("the building blocks of probability", font_size=22, font=MONO, color=ACCENT)
        subtitle.set_opacity(0.75)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.2).to_edge(UP, buff=0.4)

        board = Circle(radius=2.2, color=ACCENT, stroke_width=2)
        board.set_fill(PRIMARY, opacity=0.45).move_to(board_center)

        ring1 = Circle(radius=1.5, color=ACCENT, stroke_width=1.2, stroke_opacity=0.25)
        ring1.move_to(board_center)
        ring2 = Circle(radius=0.8, color=ACCENT, stroke_width=1.2, stroke_opacity=0.2)
        ring2.move_to(board_center)

        self.add_subcaption("Imagine throwing a dart at a board.", duration=5.0)
        self.play(GrowFromCenter(board), run_time=1.5)
        self.play(Create(ring1), Create(ring2), FadeIn(title_group), run_time=1.0)
        self.wait(1.5)

        dart_offsets = [np.array([-1.2, 0.8, 0]), np.array([0.5, -1.3, 0]),
                        np.array([-0.4, -0.2, 0]), np.array([1.3, 1.1, 0])]
        darts = VGroup(*[Dot(board_center + off, radius=0.07, color=ACCENT) for off in dart_offsets])

        self.add_subcaption("It could land anywhere.", duration=6.0)
        self.play(LaggedStart(*[FadeIn(d, scale=0.3) for d in darts], lag_ratio=0.25), run_time=2.0)
        self.wait(2.0)

        omega_label = MathTex(r"\Omega", font_size=TITLE_SIZE, color=ACCENT)
        omega_text = Text("Sample Space", font_size=LABEL_SIZE, font=MONO, color=ACCENT)
        omega_def = MathTex(r"\text{all possible outcomes}", font_size=26, color=ACCENT)
        omega_def.set_opacity(0.85)
        omega_group = VGroup(omega_label, omega_text, omega_def).arrange(DOWN, buff=0.3)
        omega_group.move_to(RIGHT * 3.6 + UP * 1.1)

        self.add_subcaption("The whole board is the sample space.", duration=8.0)
        self.play(Indicate(board, scale_factor=1.06, color=ACCENT), run_time=1.0)
        self.play(
            board.animate.shift(LEFT * 2.3),
            ring1.animate.shift(LEFT * 2.3),
            ring2.animate.shift(LEFT * 2.3),
            darts.animate.shift(LEFT * 2.3),
            run_time=1.2,
        )
        self.play(Write(omega_group), run_time=1.5)
        self.wait(2.5)

        sector = Difference(
            Circle(radius=2.2), Circle(radius=1.5)
        ).move_to(board.get_center())
        sector.set_fill(SECONDARY, opacity=0.85)
        sector.set_stroke(ACCENT, width=1.5, opacity=0.6)

        event_label = MathTex(r"A", font_size=TITLE_SIZE, color=SECONDARY)
        event_text = Text("Event", font_size=LABEL_SIZE, font=MONO, color=ACCENT)
        event_def = MathTex(r"\text{a subset of outcomes}", font_size=26, color=ACCENT)
        event_def.set_opacity(0.85)
        event_group = VGroup(event_label, event_text, event_def).arrange(DOWN, buff=0.3)
        event_group.move_to(RIGHT * 3.6 + DOWN * 1.2)

        arrow_to_sector = Arrow(
            event_group.get_left() + LEFT * 0.15,
            board.get_center() + np.array([1.7, -0.55, 0]),
            buff=0.15, color=SECONDARY, stroke_width=3, max_tip_length_to_length_ratio=0.25,
        )

        self.add_subcaption("An event is a particular region.", duration=7.5)
        self.play(FadeIn(sector), run_time=1.2)
        self.play(FadeIn(event_group), Create(arrow_to_sector), run_time=1.2)
        self.wait(2.0)

        target_point = board.get_center() + np.array([1.85 * np.cos(10 * DEGREES),
                                                      1.85 * np.sin(10 * DEGREES), 0])
        final_dart = Dot(color=ACCENT, radius=0.09).move_to(board.get_top() + UP * 0.6)

        check = MathTex(r"\checkmark", font_size=44, color=SECONDARY)
        check.next_to(event_text, RIGHT, buff=0.3)

        takeaway = MathTex(
            r"\text{dart lands in } A \;\Longrightarrow\; \text{event occurred}",
            font_size=28, color=ACCENT,
        )
        takeaway.to_edge(DOWN, buff=0.5)

        self.add_subcaption("Land in the red — the event occurred.", duration=9.0)
        self.play(FadeIn(final_dart, scale=0.3), run_time=0.5)
        self.play(final_dart.animate.move_to(target_point), run_time=1.2)
        self.play(
            Flash(target_point, color=ACCENT, flash_radius=0.45, num_lines=10),
            sector.animate.set_fill(SECONDARY, opacity=1.0),
            FadeIn(check, scale=0.5),
            run_time=1.0,
        )
        self.play(FadeIn(takeaway), run_time=1.0)
        self.wait(2.5)

        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.wait(0.3)


class Scene2_FormalDefinition(Scene):
    def construct(self):
        self.camera.background_color = BG

        rect_center = LEFT * 2.7 + DOWN * 0.2

        header = Text("DEFINITION", font_size=28, font=MONO, color=ACCENT, weight=BOLD)
        header.to_edge(UP, buff=0.5)

        rect = RoundedRectangle(corner_radius=0.15, width=5.2, height=3.4, color=ACCENT, stroke_width=2)
        rect.set_fill(PRIMARY, opacity=0.12).move_to(rect_center)

        s_label = MathTex(r"S", font_size=40, color=ACCENT)
        s_label.next_to(rect.get_corner(UL), DR, buff=0.15)

        dot_offsets = [np.array([-1.8, 1.0, 0]), np.array([-0.9, -0.6, 0]),
                       np.array([0.2, -0.1, 0]), np.array([1.6, 0.0, 0]),
                       np.array([-1.5, -0.9, 0]), np.array([1.1, -0.9, 0]),
                       np.array([0.5, -0.75, 0]), np.array([2.0, -0.4, 0]),
                       np.array([-0.3, 0.1, 0])]
        dots = VGroup(*[Dot(rect_center + off, radius=0.06, color=ACCENT) for off in dot_offsets])

        self.add_subcaption("Formally: S is the set of all possible outcomes.", duration=8.0)
        self.play(GrowFromEdge(rect, LEFT), FadeIn(s_label), FadeIn(header), run_time=1.2)
        self.play(LaggedStart(*[FadeIn(d, scale=0.3) for d in dots], lag_ratio=0.12), run_time=1.5)

        dots_caption = Text("each dot = one possible outcome", font_size=22, font=MONO, color=ACCENT)
        dots_caption.set_opacity(0.8)
        dots_caption.next_to(rect, UP, buff=0.25)
        self.play(FadeIn(dots_caption), run_time=0.8)

        step1 = MathTex(r"S \text{ : the set of all possible outcomes}", font_size=28, color=ACCENT)
        step1.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(step1), run_time=0.8)
        self.wait(2.5)

        blob_center = rect_center + np.array([0.9, -0.35, 0])
        blob = Circle(radius=1.05, color=SECONDARY, stroke_width=2)
        blob.set_fill(SECONDARY, opacity=0.45).stretch(1.25, 0).stretch(0.85, 1).move_to(blob_center)

        a_label = MathTex(r"A", font_size=36, color=SECONDARY)
        a_label.move_to(blob.get_corner(UL) + UL * 0.25)

        inside_indices = [2, 3, 5, 6, 7]

        self.add_subcaption("An event A is any subset of S.", duration=8.0)
        self.play(FadeIn(blob), FadeIn(a_label), FadeOut(dots_caption), run_time=1.2)
        self.play(
            *[dots[i].animate.set_color(SECONDARY).set_fill(SECONDARY, opacity=1.0)
              for i in inside_indices],
            run_time=1.0,
        )

        step2 = MathTex(r"A \subseteq S \text{ : an event is any subset}", font_size=28, color=ACCENT)
        step2.to_edge(DOWN, buff=0.5)
        self.play(ReplacementTransform(step1, step2), run_time=1.0)
        self.wait(2.5)

        actual_index = 5
        ring = Circle(radius=0.16, color=ACCENT, stroke_width=3).move_to(dots[actual_index])

        s_actual_label = MathTex(r"s_{\text{actual}}", font_size=30, color=ACCENT)
        s_actual_label.move_to(blob_center + DOWN * 1.65)
        arrow_to_dot = Arrow(
            s_actual_label.get_top(), dots[actual_index].get_bottom(),
            buff=0.12, color=ACCENT, stroke_width=2.5, max_tip_length_to_length_ratio=0.3,
        )

        implication = MathTex(
            r"s_{\text{actual}} \in A \;\Longrightarrow\; A \text{ occurred}",
            font_size=34, color=ACCENT,
        )
        implication.move_to(RIGHT * 3.1 + UP * 1.3)

        self.add_subcaption("The event occurs iff the actual outcome lies in A.", duration=9.5)
        self.play(Create(ring), FadeIn(s_actual_label), Create(arrow_to_dot), run_time=1.2)
        self.play(Write(implication), run_time=2.0)
        self.wait(3.0)

        indicator = MathTex(
            r"I_A(s) = \begin{cases} 1 & s \in A \\ 0 & s \notin A \end{cases}",
            font_size=32, color=ACCENT,
        )
        indicator.move_to(RIGHT * 3.1 + DOWN * 1.0)

        self.add_subcaption("One if it's in A, zero otherwise.", duration=6.5)
        self.play(FadeIn(indicator), run_time=1.2)
        self.wait(2.0)

        box = SurroundingRectangle(implication, color=SECONDARY, buff=0.18, stroke_width=2.5)

        self.add_subcaption("Sample space: all outcomes. Event: a subset. Occurs iff the outcome is in it.", duration=5.0)
        self.play(Create(box), run_time=1.0)
        self.wait(2.0)

        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.wait(0.3)


class Scene3_DieExample(Scene):
    def construct(self):
        self.camera.background_color = BG

        header = Text("EXAMPLE : DIE ROLL", font_size=28, font=MONO, color=ACCENT, weight=BOLD)
        header.to_edge(UP, buff=0.5)

        faces = VGroup()
        for lab in ["1", "2", "3", "4", "5", "6"]:
            sq = RoundedRectangle(corner_radius=0.12, width=0.95, height=0.95,
                                  color=ACCENT, stroke_width=2)
            sq.set_fill(PRIMARY, opacity=0.35)
            num = Text(lab, font_size=36, font=MONO, color=ACCENT)
            faces.add(VGroup(sq, num))
        faces.arrange(RIGHT, buff=0.35).move_to(UP * 1.2)

        self.add_subcaption("Roll a six-sided die: six possible results.", duration=7.0)
        self.play(FadeIn(header), run_time=0.8)
        self.play(LaggedStart(*[GrowFromCenter(f) for f in faces], lag_ratio=0.15), run_time=2.0)
        self.wait(1.5)

        omega_eq = MathTex(r"\Omega := \{1,\,2,\,3,\,4,\,5,\,6\}", font_size=40, color=ACCENT)
        omega_eq.move_to(DOWN * 0.35)

        self.add_subcaption("These six outcomes form the sample space.", duration=7.0)
        self.play(Write(omega_eq), run_time=1.5)

        omega_note = VGroup(
            Text('Ω ("Omega") denotes the sample space:', font_size=22, font=MONO, color=ACCENT),
            Text("the set of ALL possible outcomes", font_size=22, font=MONO, color=ACCENT),
        ).arrange(DOWN, buff=0.12)
        omega_note.set_opacity(0.85)
        omega_note.next_to(omega_eq, DOWN, buff=0.25)
        self.play(FadeIn(omega_note), run_time=0.8)
        self.wait(3.0)

        mutex = MathTex(r"\text{mutually exclusive: the die never lands on two faces at once}",
                        font_size=26, color=ACCENT)
        mutex.set_opacity(0.85)
        mutex.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(mutex), run_time=0.8)
        self.wait(2.0)

        even_indices = [1, 3, 5]
        event_eq = MathTex(
            r"E = \{2,\,4,\,6\} \;\subseteq\; \Omega \quad \text{(rolling an even number)}",
            font_size=36, color=SECONDARY,
        )
        event_eq.move_to(DOWN * 2.35)

        self.add_subcaption("An event: 'the roll is even' — a subset of Omega.", duration=8.0)
        self.play(
            *[faces[i][0].animate.set_fill(SECONDARY, opacity=0.65) for i in even_indices],
            *[faces[i][1].animate.set_color(SECONDARY) for i in even_indices],
            FadeOut(omega_note),
            run_time=1.0,
        )
        self.play(LaggedStart(*[Indicate(faces[i], scale_factor=1.1, color=ACCENT)
                                for i in even_indices], lag_ratio=0.15), run_time=1.2)
        self.play(Write(event_eq), run_time=1.5)
        self.wait(3.0)

        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.wait(0.3)


class Scene4_CoinFlipEvents(Scene):
    def construct(self):
        self.camera.background_color = BG

        header = Text("EXAMPLE : TEN COIN FLIPS", font_size=28, font=MONO, color=ACCENT, weight=BOLD)
        header.to_edge(UP, buff=0.5)

        seq = ["H", "H", "T", "H", "T", "T", "H", "H", "T", "H"]
        slots = VGroup()
        for ch in seq:
            sq = RoundedRectangle(corner_radius=0.08, width=0.62, height=0.62,
                                  color=ACCENT, stroke_width=1.5)
            sq.set_fill(PRIMARY, opacity=0.3)
            letter = Text(ch, font_size=26, font=MONO, color=ACCENT)
            slots.add(VGroup(sq, letter))
        slots.arrange(RIGHT, buff=0.18).move_to(UP * 2.1)

        s_def = MathTex(r"s = (s_1,\, s_2,\, \ldots,\, s_{10}), \quad s_j \in \{H,\, T\}",
                        font_size=30, color=ACCENT)
        s_def.move_to(UP * 0.9)

        self.add_subcaption("Flip a coin ten times: one outcome is a string of H's and T's.", duration=8.0)
        self.play(FadeIn(header), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(sl, scale=0.4) for sl in slots], lag_ratio=0.08), run_time=1.8)
        self.play(Write(s_def), run_time=1.5)

        s_note = Text("one complete history of 10 flips = one outcome",
                      font_size=22, font=MONO, color=ACCENT)
        s_note.set_opacity(0.8)
        s_note.next_to(s_def, DOWN, buff=0.25)
        self.play(FadeIn(s_note), run_time=0.8)
        self.wait(2.5)

        a1_rect = SurroundingRectangle(slots[0], color=SECONDARY, buff=0.06, stroke_width=2.5)
        a1_eq = MathTex(r"A_1 = \text{event that the } 1^{\text{st}} \text{ flip is Heads}",
                        font_size=28, color=ACCENT)
        a1_eq.move_to(UP * 0.0)

        self.add_subcaption("A_j is the event: the j-th flip came up Heads.", duration=7.0)
        self.play(FadeOut(s_note), Create(a1_rect), Write(a1_eq), run_time=1.5)
        self.wait(2.0)

        heads_indices = [i for i, ch in enumerate(seq) if ch == "H"]
        step_b = MathTex(
            r"B = A_1 \cup A_2 \cup \cdots \cup A_{10} \;\; \text{: at least one Heads}",
            font_size=30, color=ACCENT,
        )
        step_b.to_edge(DOWN, buff=0.5)

        self.add_subcaption("B — at least one Heads — is the union of all A_j.", duration=8.0)
        self.play(
            *[slots[i][0].animate.set_fill(SECONDARY, opacity=0.55) for i in heads_indices],
            *[slots[i][1].animate.set_color(SECONDARY) for i in heads_indices],
            FadeOut(a1_rect),
            run_time=1.0,
        )
        self.play(FadeOut(a1_eq), Write(step_b), run_time=1.5)
        self.wait(2.5)

        step_c = MathTex(
            r"C = A_1 \cap A_2 \cap \cdots \cap A_{10} \;\; \text{: all Heads}",
            font_size=30, color=ACCENT,
        )
        step_c.to_edge(DOWN, buff=0.5)

        c_note = MathTex(
            r"\text{every } A_j \text{ must occur} \;\Longrightarrow\; \text{the outcome becomes all Heads}",
            font_size=26, color=ACCENT,
        )
        c_note.set_opacity(0.85)
        c_note.move_to(UP * 0.0)

        t_indices = [i for i, ch in enumerate(seq) if ch == "T"]
        new_letters = {}
        for i in t_indices:
            nl = Text("H", font_size=26, font=MONO, color=SECONDARY)
            nl.move_to(slots[i][1])
            new_letters[i] = nl

        self.add_subcaption("C — all Heads — is the intersection of all A_j.", duration=8.0)
        self.play(ReplacementTransform(step_b, step_c), FadeIn(c_note), run_time=1.0)
        self.play(
            LaggedStart(*[ReplacementTransform(slots[i][1], new_letters[i]) for i in t_indices],
                        lag_ratio=0.12),
            *[slots[i][0].animate.set_fill(SECONDARY, opacity=0.55) for i in t_indices],
            run_time=3.5,
        )
        self.wait(3.0)

        original_letters = []
        for i in range(len(seq)):
            ol = Text(seq[i], font_size=26, font=MONO, color=ACCENT)
            ol.move_to(slots[i][0])
            original_letters.append(ol)
        back_note = Text("back to our original outcome", font_size=22, font=MONO, color=ACCENT)
        back_note.set_opacity(0.8)
        back_note.move_to(c_note)

        self.add_subcaption("Back to our original outcome.", duration=4.0)
        self.play(
            LaggedStart(
                *[ReplacementTransform(new_letters.get(i, slots[i][1]), original_letters[i])
                  for i in range(len(seq))],
                lag_ratio=0.05,
            ),
            *[slots[i][0].animate.set_fill(PRIMARY, opacity=0.3) for i in range(len(seq))],
            ReplacementTransform(c_note, back_note),
            run_time=1.5,
        )
        self.wait(1.5)

        step_d = MathTex(
            r"D = \bigcup_{j=1}^{9} \left(A_j \cap A_{j+1}\right) \;\; \text{: two Heads in a row}",
            font_size=30, color=ACCENT,
        )
        step_d.to_edge(DOWN, buff=0.5)
        pair_rects = VGroup(
            SurroundingRectangle(VGroup(slots[0], slots[1]), color=SECONDARY, buff=0.06, stroke_width=2.5),
            SurroundingRectangle(VGroup(slots[6], slots[7]), color=SECONDARY, buff=0.06, stroke_width=2.5),
        )

        self.add_subcaption("D — at least two consecutive Heads.", duration=7.0)
        self.play(ReplacementTransform(step_c, step_d), Create(pair_rects), run_time=1.5)
        self.wait(2.0)

        mapping = MathTex(
            r"\text{OR} \;\longleftrightarrow\; \cup \qquad\qquad \text{AND} \;\longleftrightarrow\; \cap",
            font_size=34, color=SECONDARY,
        )
        mapping.move_to(DOWN * 1.5)
        map_box = SurroundingRectangle(mapping, color=SECONDARY, buff=0.2, stroke_width=2.5)

        self.add_subcaption("In set notation: OR is union, AND is intersection.", duration=7.0)
        lead = Text("events are combined with set operations:",
                    font_size=22, font=MONO, color=ACCENT)
        lead.set_opacity(0.85)
        lead.next_to(mapping, UP, buff=0.3)
        self.play(FadeOut(step_d, pair_rects, back_note), FadeIn(lead), run_time=0.8)
        self.play(Write(mapping), Create(map_box), run_time=1.5)
        self.wait(2.5)

        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.wait(0.3)


class Scene5_TraderScaleUp(Scene):
    def construct(self):
        self.camera.background_color = BG

        header = Text("SCALE-UP : 576 TRADES", font_size=28, font=MONO, color=ACCENT, weight=BOLD)
        header.to_edge(UP, buff=0.5)

        intro = MathTex(r"\text{one trade every } 10 \text{ min}, \quad 24\text{ h} \times 4 \text{ days}",
                        font_size=30, color=ACCENT)
        intro.move_to(UP * 2.2)
        n_eq = MathTex(r"\frac{4 \times 24 \times 60}{10} = 576 \text{ trades}",
                       font_size=34, color=ACCENT)
        n_eq.move_to(UP * 1.25)

        self.add_subcaption("A trader makes one trade every ten minutes, continuously for four days.",
                            duration=8.0)
        self.play(FadeIn(header), Write(intro), run_time=1.5)
        self.play(Write(n_eq), run_time=1.5)
        self.wait(2.0)

        pattern = ["P", "P", "L", "P", "L", "P", "P", "L", "P", "L", "L", "P"]
        tiles = VGroup()
        for ch in pattern:
            t = Text(ch, font_size=22, font=MONO,
                     color=ACCENT if ch == "P" else SECONDARY)
            tiles.add(t)
        dots = Text("...", font_size=22, font=MONO, color=ACCENT)
        strip = VGroup(*tiles, dots).arrange(RIGHT, buff=0.22).move_to(UP * 0.1)
        strip_label = MathTex(r"s_i = P \text{ (profit)} \;\text{ or }\; L \text{ (loss)}",
                              font_size=26, color=ACCENT)
        strip_label.set_opacity(0.85)
        strip_label.move_to(DOWN * 0.65)

        self.add_subcaption("Each trade is either a profit P or a loss L.", duration=7.0)
        self.play(LaggedStart(*[FadeIn(t, scale=0.4) for t in strip], lag_ratio=0.08), run_time=1.8)
        self.play(FadeIn(strip_label), run_time=0.8)
        self.wait(2.0)

        omega = MathTex(r"\Omega = \{P,\, L\}^{576}", font_size=44, color=ACCENT)
        omega.move_to(DOWN * 1.6)
        omega_box = SurroundingRectangle(omega, color=SECONDARY, buff=0.2, stroke_width=2.5)

        self.add_subcaption("The sample space: every possible profit/loss history.", duration=7.0)
        self.play(Write(omega), run_time=1.5)
        self.play(Create(omega_box), run_time=1.0)

        omega_note = Text("every possible P/L sequence is one outcome in Omega",
                          font_size=22, font=MONO, color=ACCENT)
        omega_note.set_opacity(0.8)
        omega_note.next_to(omega_box, DOWN, buff=0.25)
        self.play(FadeIn(omega_note), run_time=0.8)
        self.wait(2.0)

        count = MathTex(r"|\Omega| = 2^{1}", font_size=36, color=ACCENT)
        count.move_to(DOWN * 2.9)
        self.add_subcaption("The number of possible histories explodes exponentially.", duration=9.0)
        self.play(FadeIn(count), FadeOut(strip_label, omega_note), run_time=0.8)
        for exp in [r"2^{10}", r"2^{100}", r"2^{576}"]:
            nxt = MathTex(r"|\Omega| = " + exp, font_size=36, color=ACCENT)
            nxt.move_to(DOWN * 2.9)
            self.play(ReplacementTransform(count, nxt), run_time=0.9)
            count = nxt
        self.wait(1.0)

        compare = MathTex(r"2^{576} \approx 2.5 \times 10^{173} \;\gg\; 10^{80} \text{ atoms in the universe}",
                          font_size=28, color=SECONDARY)
        compare.next_to(count, DOWN, buff=0.35)

        self.add_subcaption("Far more possible outcomes than atoms in the observable universe.",
                            duration=7.0)
        self.play(Write(compare), run_time=1.5)
        self.wait(2.5)

        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.wait(0.3)
