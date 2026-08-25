from manim import *
import random

FONT = "DejaVu Sans"
BG = "#0d1120"
INK = "#eef1f7"
SUB = "#94a1b7"
RED_C = "#ff5d6c"
BLUE_C = "#4d96ff"
GREEN_C = "#39d98a"
GOLD = "#ffd35a"
BAD = "#ff6b6b"
OKC = "#7dd97c"
COL_S = "#8fb7ff"
WALL_F = "#151b2b"
WALL_E = "#46536f"
GRID_L = "#3a465f"
PEB = "#aab6cc"

SPAWN = LEFT * 6.6 + DOWN * 3.1


def txt(s, size=30, color=INK, weight=NORMAL, slant=NORMAL):
    return Text(
        s,
        font=FONT,
        font_size=size,
        color=color,
        weight=weight,
        slant=slant,
        line_spacing=1.15,
    )


def mtex(*parts, size=44, color=INK):
    return MathTex(*parts, font_size=size, color=color)


def box_around(m, pad_x=0.35, pad_y=0.25, stroke=WALL_E, sw=2.5, corner=0.18):
    b = RoundedRectangle(
        width=m.width + 2 * pad_x,
        height=m.height + 2 * pad_y,
        corner_radius=corner,
        stroke_color=stroke,
        stroke_width=sw,
    )
    b.move_to(m.get_center())
    return b


class ShareReadout(VGroup):
    def __init__(self, title, accent, frac_color=None):
        self.title = txt(title, 23, SUB)
        self.num = Integer(0, font_size=40, color=accent)
        self.den = Integer(0, font_size=40, color=INK)
        self.bar = Line(ORIGIN, RIGHT * 0.66, stroke_width=3.5, color=INK)
        self.frac = VGroup(self.num, self.bar, self.den).arrange(DOWN, buff=0.13)
        self.dec = DecimalNumber(0.0, num_decimal_places=3, font_size=32, color=accent)
        super().__init__(self.title, self.frac, self.dec)
        self.arrange(DOWN, buff=0.24)

    def wire(self, num_tracker, den_tracker):
        self.num.add_updater(lambda m: m.set_value(int(num_tracker.get_value())))
        self.den.add_updater(lambda m: m.set_value(int(den_tracker.get_value())))
        self.dec.add_updater(
            lambda m: m.set_value(
                num_tracker.get_value() / den_tracker.get_value()
                if den_tracker.get_value() > 0
                else 0.0
            )
        )

    def unwire(self):
        for sm in [*self.family_members_with_points()]:
            sm.clear_updaters()


PIP_LAYOUT = {
    1: [(0, 0)],
    2: [(-1, -1), (1, 1)],
    3: [(-1, -1), (0, 0), (1, 1)],
    4: [(-1, -1), (-1, 1), (1, -1), (1, 1)],
    5: [(-1, -1), (-1, 1), (0, 0), (1, -1), (1, 1)],
    6: [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1)],
}


def die_face(n, size=0.92, hot=False, cold=False):
    face_col = GOLD if hot else (SUB if cold else INK)
    rect = RoundedRectangle(
        corner_radius=size * 0.2,
        width=size,
        height=size,
        stroke_color=face_col,
        stroke_width=3.2,
        fill_color=WALL_F,
        fill_opacity=0.85,
    )
    unit = size * 0.27
    pips = VGroup(
        *[
            Dot(radius=size * 0.075, color=face_col).move_to(
                rect.get_center() + UP * dy * unit + RIGHT * dx * unit
            )
            for (dy, dx) in PIP_LAYOUT[n]
        ]
    )
    return VGroup(rect, pips)


def make_pebbles(rows, cols, colors_grid, rx=0.085, buff=(0.62, 0.55)):
    dots = VGroup()
    for r in range(rows):
        for c in range(cols):
            dots.add(Dot(radius=rx, color=colors_grid[r][c]))
    dots.arrange_in_grid(rows=rows, cols=cols, buff=buff)
    return dots


class NaiveProbability(MovingCameraScene):
    def construct(self):
        self.camera.background_color = BG
        rng = random.Random(20260821)

        self._intro()
        self._act_experiment(rng)
        self._act_pebbles(rng)
        self._act_formula(rng)
        self._act_die()
        self._act_limits(rng)
        self._finale()

    def _kicker(self, s):
        old = getattr(self, "_kick", None)
        k = txt(s, 24, SUB, weight=BOLD).to_corner(UL, buff=0.45)
        if old is not None:
            self.play(FadeOut(old, shift=LEFT * 0.3), FadeIn(k, shift=RIGHT * 0.3), run_time=0.6)
        else:
            self.play(FadeIn(k, shift=RIGHT * 0.3), run_time=0.6)
        self._kick = k
        return k

    def _wipe(self, keep=(), run_time=0.7):
        stray = [m for m in self.mobjects if m not in keep]
        if stray:
            self.play(*[FadeOut(m) for m in stray], run_time=run_time)

    def _intro(self):
        q = txt("What is probability?", 48, INK, weight=BOLD)
        self.play(FadeIn(q, scale=0.86), run_time=0.9)
        self.play(Circumscribe(q, color=GOLD, fade_out=True, time_width=0.7), run_time=1.4)
        self.wait(1.1)
        self.play(FadeOut(q), run_time=0.7)
        self.wait(0.4)

    def _make_wall(self, center=LEFT * 3.25 + UP * 0.1, side=5.3):
        wall = Square(side=side, stroke_color=WALL_E, stroke_width=3)
        wall.set_fill(WALL_F, 1.0)
        wall.move_to(center)
        fracs = [(RED_C, 0.5), (BLUE_C, 0.3), (GREEN_C, 0.2)]
        names = ["red", "blue", "green"]
        strips = VGroup()
        labels = VGroup()
        x = wall.get_left()[0]
        for (col, f), nm in zip(fracs, names):
            w = side * f
            rect = Rectangle(width=w, height=side, stroke_width=0)
            rect.set_fill(col, 0.42)
            rect.move_to(
                [
                    x + w / 2,
                    wall.get_center()[1],
                    0,
                ]
            )
            strips.add(rect)
            lab = VGroup(
                txt(nm, 26, col, weight=BOLD),
                txt(f"{int(f*100)}%", 22, INK),
            ).arrange(DOWN, buff=0.12)
            lab.move_to(rect.get_center())
            labels.add(lab)
            x += w
        dims = VGroup(
            txt("10 m", 20, SUB).next_to(wall, UP, buff=0.18),
            txt("10 m", 20, SUB).rotate(90 * DEGREES).next_to(wall, RIGHT, buff=0.18),
        )
        return wall, strips, labels, dims

    def _act_experiment(self, rng):
        self._kicker("01  ·  an experiment")
        wall, strips, labels, dims = self._make_wall()
        self.play(
            Create(wall),
            LaggedStart(*[FadeIn(s, scale=0.9) for s in strips], lag_ratio=0.15),
            LaggedStart(*[FadeIn(l) for l in labels], lag_ratio=0.15),
            FadeIn(dims),
            run_time=1.6,
        )
        self.wait(0.5)

        prompt = VGroup(
            txt("Blindfolded, you throw stones at this wall.", 29, INK),
            txt("How often do you hit ", 29, INK, ),
        )
        prompt[1] += txt("red?", 29, RED_C, weight=BOLD)
        prompt.arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        prompt.move_to(RIGHT * 4.35 + UP * 2.6)
        self.play(FadeIn(prompt[0], shift=UP * 0.2), run_time=0.7)
        self.play(FadeIn(prompt[1], shift=UP * 0.2), run_time=0.7)
        self.wait(1.2)

        ro = ShareReadout("observed share of red", RED_C)
        ro.move_to(RIGHT * 4.35 + UP * 0.35)
        cnt_r = ValueTracker(0)
        cnt_n = ValueTracker(0)
        ro.wire(cnt_r, cnt_n)
        self.play(FadeIn(ro, shift=LEFT * 0.4), run_time=0.8)

        def land_pt(col, wall=wall, side=5.3):
            lo = {"R": 0.0, "B": 0.5, "G": 0.8}[col]
            hi = {"R": 0.5, "B": 0.8, "G": 1.0}[col]
            u = rng.uniform(lo + 0.02, hi - 0.02)
            v = rng.uniform(0.05, 0.95)
            return np.array(
                [
                    wall.get_left()[0] + u * side,
                    wall.get_bottom()[1] + v * side,
                    0,
                ]
            )

        first8 = ["G", "B", "G", "G", "R", "G", "B", "G"]
        rest = ["R"] * 28 + ["B"] * 17 + ["G"] * 7
        rng.shuffle(rest)
        seq = first8 + rest
        assert seq.count("R") == 29 and seq.count("B") == 19 and seq.count("G") == 12

        ball = (
            Circle(radius=0.14, color=WALL_E, stroke_width=2)
            .set_fill(INK, 0.95)
            .move_to(SPAWN)
        )
        marks = VGroup()

        def throw_slow(col):
            nonlocal ball
            pt = land_pt(col)
            self.play(
                ball.animate.move_to(pt),
                path_arc=rng.uniform(-0.4, 0.4),
                rate_func=ease_in_out_sine,
                run_time=1.0,
            )
            mk = Dot(pt, radius=0.055).set_fill("#10141f", 1.0).set_stroke(DOT_EDGE, 1.0, 0.9)
            anims = [
                FadeOut(ball, scale=0.5),
                FadeIn(mk, scale=2.4),
                cnt_n.animate.increment_value(1),
            ]
            if col == "R":
                anims += [cnt_r.animate.increment_value(1), Flash(pt, color=RED_C, flash_radius=0.28, num_lines=8)]
            self.play(*anims, run_time=0.3)
            marks.add(mk)
            ball = Circle(radius=0.14, color=WALL_E, stroke_width=2).set_fill(INK, 0.95).move_to(SPAWN)
            self.add(ball)

        for i, col in enumerate(seq[:8]):
            throw_slow(col)
            self.wait(0.12)

        shaky = txt("so far, almost everything is green…", 26, GREEN_C)
        shaky.next_to(prompt, DOWN, buff=0.5).align_to(prompt, LEFT)
        self.play(FadeIn(shaky, shift=UP * 0.2), run_time=0.7)
        self.wait(1.0)

        for chunk_start in range(8, len(seq), 13):
            chunk = seq[chunk_start : chunk_start + 13]
            pts = [land_pt(c) for c in chunk]
            balls = VGroup(
                *[
                    Circle(radius=0.12, color=WALL_E, stroke_width=2)
                    .set_fill(INK, 0.95)
                    .move_to(SPAWN + UP * 0.05 * j)
                    for j in range(len(chunk))
                ]
            )
            self.add(balls)
            self.play(
                LaggedStart(
                    *[b.animate.move_to(pt).set_opacity(0.0) for b, pt in zip(balls, pts)],
                    lag_ratio=0.1,
                ),
                run_time=1.5,
            )
            new_marks = VGroup(
                *[
                    Dot(pt, radius=0.055).set_fill("#10141f", 1.0).set_stroke(DOT_EDGE, 1.0, 0.9)
                    for pt in pts
                ]
            )
            n_red = chunk.count("R")
            self.play(
                LaggedStartMap(FadeIn, new_marks, lag_ratio=0.04),
                FadeOut(balls),
                cnt_n.animate.increment_value(len(chunk)),
                cnt_r.animate.increment_value(n_red),
                run_time=0.7,
            )
            marks.add(new_marks)

        ro.unwire()
        settle = txt("…but as n grows, the share settles.", 26, INK)
        self.play(FadeOut(shaky), FadeIn(settle, shift=UP * 0.2).shift, run_time=0.01)
        self.remove(settle)
        settle = txt("…but as n grows, the share settles.", 26, INK)
        settle.next_to(prompt, DOWN, buff=0.5).align_to(prompt, LEFT)
        self.play(FadeOut(shaky), FadeIn(settle, shift=UP * 0.2), run_time=0.8)
        self.play(Indicate(ro.dec, color=RED_C), run_time=0.8)
        self.wait(0.6)

        theo_obs = mtex(
            r"\hat{P}(\text{red}) \;\longrightarrow\; P(\text{red})",
            r"\quad\text{as } n \to \infty",
            size=30,
            color=SUB,
        )
        theo_obs.next_to(ro, DOWN, buff=0.55)
        lln = txt("Law of Large Numbers", 21, GOLD)
        lln.next_to(theo_obs, DOWN, buff=0.18)
        self.play(FadeIn(theo_obs, shift=UP * 0.2), run_time=0.8)
        self.play(FadeIn(lln), run_time=0.5)
        self.wait(1.4)

        pivot = VGroup(
            txt("Here is the secret:", 30, INK),
            VGroup(txt("we could have predicted it ", 30, INK), txt("without throwing", 30, GOLD, weight=BOLD), txt(".", 30, INK)).arrange(RIGHT, buff=0.02),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        pivot.move_to(RIGHT * 4.35 + DOWN * 2.15)
        self.play(FadeIn(pivot, shift=UP * 0.25), run_time=1.0)
        self.wait(1.6)

        self._wipe()

    def _act_pebbles(self, rng):
        self._kicker("02  ·  from area to pebbles")
        wall, strips, labels, dims = self._make_wall()
        self.play(
            FadeIn(wall),
            LaggedStart(*[FadeIn(s) for s in strips], lag_ratio=0.1),
            LaggedStart(*[FadeIn(l) for l in labels], lag_ratio=0.1),
            run_time=1.2,
        )

        grid_lines = VGroup()
        side = 5.3
        for i in range(1, 10):
            gx = wall.get_left()[0] + i * side / 10
            grid_lines.add(
                Line(
                    [gx, wall.get_bottom()[1], 0],
                    [gx, wall.get_top()[1], 0],
                    stroke_color=GRID_L,
                    stroke_width=1.4,
                )
            )
            gy = wall.get_bottom()[1] + i * side / 10
            grid_lines.add(
                Line(
                    [wall.get_left()[0], gy, 0],
                    [wall.get_right()[0], gy, 0],
                    stroke_color=GRID_L,
                    stroke_width=1.4,
                )
            )
        self.play(Create(grid_lines), run_time=1.1)

        cap = txt("chance of red  =  red's share of the wall", 28, INK)
        cap.move_to(RIGHT * 4.3 + UP * 2.7)
        self.play(FadeIn(cap, shift=UP * 0.2), run_time=0.8)

        area_eq = mtex(
            r"P(\text{red})",
            r"=",
            r"\frac{\text{area(red)}}{\text{area(wall)}}",
            r"=",
            r"\frac{50}{100}",
            r"=",
            r"\frac{1}{2}",
            size=36,
        )
        area_eq[0].set_color(RED_C)
        area_eq[4][:2].set_color(RED_C)
        area_eq.next_to(cap, DOWN, buff=0.7)
        self.play(
            LaggedStart(*[Write(p) for p in area_eq], lag_ratio=0.25),
            strips[0].animate.set_fill(opacity=0.75),
            run_time=2.2,
        )
        self.wait(1.0)

        cap2 = txt("now imagine every point of the wall as a “pebble”…", 26, SUB)
        cap2.move_to(RIGHT * 4.3 + DOWN * 0.9)
        self.play(FadeIn(cap2, shift=UP * 0.2), run_time=0.8)

        colors_grid = []
        for r in range(5):
            row = []
            for c in range(6):
                row.append(RED_C if c < 3 else (BLUE_C if c < 5 else GREEN_C))
            colors_grid.append(row)
        pebbles = make_pebbles(5, 6, colors_grid)
        pebbles.move_to(RIGHT * 4.35 + DOWN * 2.35).scale(0.9)

        self.play(
            FadeOut(wall, scale=0.4),
            FadeOut(strips),
            FadeOut(labels),
            FadeOut(grid_lines),
            LaggedStartMap(FadeIn, pebbles, lag_ratio=0.03),
            run_time=1.5,
        )
        self.wait(0.6)

        cap3 = txt("each pebble is one possible outcome,", 25, INK)
        cap4 = VGroup(
            txt("and all pebbles are ", 25, INK),
            txt("equally likely", 25, GOLD, weight=BOLD),
            txt(".", 25, INK),
        ).arrange(RIGHT, buff=0.02)
        cap34 = VGroup(cap3, cap4).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        cap34.move_to(pebbles, aligned_edge=UL).to_edge(LEFT, buff=0.6).align_to(pebbles, UP).shift(UP * 1.05 + LEFT * 0.0)
        self.play(FadeIn(cap3, shift=RIGHT * 0.2), run_time=0.7)
        self.play(FadeIn(cap4, shift=RIGHT * 0.2), run_time=0.7)
        self.wait(0.8)

        red_dots = VGroup(*[d for r, d in enumerate(pebbles) if r % 1 == 0 and (pebbles.index_of(d) % 6) < 3])
        other_dots = VGroup(*[d for d in pebbles if d not in red_dots])

        s_box = box_around(pebbles, 0.45, 0.42, stroke=COL_S, sw=3)
        s_lab = VGroup(
            mtex(r"S", size=50, color=COL_S),
            txt("sample space", 21, SUB),
        ).arrange(DOWN, buff=0.1)
        s_lab.next_to(s_box, UP, buff=0.22)
        self.play(Create(s_box), FadeIn(s_lab), run_time=1.0)

        ell = Ellipse(width=red_dots.width + 0.75, height=red_dots.height + 0.6)
        ell.move_to(red_dots.get_center())
        ell_dashed = DashedVMobject(ell, num_dashes=34).set_stroke(RED_C, 3)
        a_lab = VGroup(
            mtex(r"A", size=50, color=RED_C),
            txt("land on red", 21, RED_C),
        ).arrange(DOWN, buff=0.1)
        a_lab.next_to(ell_dashed, UP, buff=0.18)
        self.play(Create(ell_dashed), FadeIn(a_lab), run_time=1.1)
        self.wait(0.4)

        self._wipe(keep=[getattr(self, "_kick", None)])

        pebbles.move_to(LEFT * 3.1 + DOWN * 0.15)
        red_dots_arranged = VGroup(*[pebbles[i] for i in range(len(pebbles)) if i % 6 < 3])
        other_arranged = VGroup(*[pebbles[i] for i in range(len(pebbles)) if i % 6 >= 3])
        s_box2 = box_around(pebbles, 0.45, 0.42, stroke=COL_S, sw=3)
        ell2 = DashedVMobject(
            Ellipse(width=red_dots_arranged.width + 0.75, height=red_dots_arranged.height + 0.6).move_to(red_dots_arranged.get_center()),
            num_dashes=34,
        ).set_stroke(RED_C, 3)
        s_lab2 = VGroup(mtex(r"S", size=50, color=COL_S), txt("sample space", 21, SUB)).arrange(DOWN, buff=0.1)
        s_lab2.next_to(s_box2, UP, buff=0.22)
        a_lab2 = VGroup(mtex(r"A", size=50, color=RED_C), txt("land on red", 21, RED_C)).arrange(DOWN, buff=0.1)
        a_lab2.next_to(ell2, UP, buff=0.18)

        self.play(FadeIn(pebbles, scale=0.95), Create(s_box2), FadeIn(s_lab2), run_time=1.1)
        self.play(Create(ell2), FadeIn(a_lab2), run_time=1.0)
        self.wait(0.5)

        brace_a = Brace(red_dots_arranged, DOWN, color=RED_C, buff=0.16)
        lab_a = mtex(r"|A| = 15", size=38, color=RED_C).next_to(brace_a, DOWN, buff=0.18)
        brace_s = Brace(s_box2, RIGHT, color=COL_S, buff=0.2)
        lab_s = mtex(r"|S| = 30", size=38, color=COL_S).next_to(brace_s, RIGHT, buff=0.18)
        cnt_cap = txt("|·|  counts the pebbles", 23, SUB)
        cnt_cap.next_to(lab_a, DOWN, buff=0.35).align_to(lab_a, LEFT)
        self.play(GrowFromCenter(brace_a), Write(lab_a), run_time=1.0)
        self.play(GrowFromCenter(brace_s), Write(lab_s), run_time=1.0)
        self.play(FadeIn(cnt_cap), run_time=0.6)
        self.wait(1.0)

        self.pebbles_state = {
            "pebbles": pebbles,
            "red": red_dots_arranged,
            "other": other_arranged,
            "s_box": s_box2,
            "ell": ell2,
            "s_lab": s_lab2,
            "a_lab": a_lab2,
            "brace_a": brace_a,
            "lab_a": lab_a,
            "brace_s": brace_s,
            "lab_s": lab_s,
            "cap": cnt_cap,
        }

    def _act_formula(self, rng):
        st = getattr(self, "pebbles_state")
        pebbles = st["pebbles"]
        red = st["red"]
        other = st["other"]

        self._kicker("03  ·  the naive definition")

        banner = VGroup(
            txt("pick one pebble completely at random —", 27, INK),
            VGroup(txt("no pebble is favored", 27, GOLD, weight=BOLD)).arrange(RIGHT),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        banner.move_to(RIGHT * 4.35 + UP * 2.9)
        self.play(FadeIn(banner[0], shift=UP * 0.2), run_time=0.7)
        self.play(FadeIn(banner[1], shift=UP * 0.2), run_time=0.7)

        orig_pos = [d.get_center().copy() for d in pebbles]
        for _ in range(2):
            perm = list(range(len(pebbles)))
            rng.shuffle(perm)
            self.play(
                *[d.animate.move_to(orig_pos[p]) for d, p in zip(pebbles, perm)],
                run_time=0.75,
                rate_func=smooth,
            )
        self.wait(0.4)

        ro = ShareReadout("picked red so far", RED_C)
        ro.move_to(RIGHT * 4.35 + UP * 0.85)
        cnt_r = ValueTracker(0)
        cnt_n = ValueTracker(0)
        ro.wire(cnt_r, cnt_n)
        self.play(FadeIn(ro, shift=LEFT * 0.4), run_time=0.7)

        red_set = {id(d) for d in red}
        picks = []
        red_pool = [i for i in range(30) if i % 6 < 3]
        other_pool = [i for i in range(30) if i % 6 >= 3]
        rng.shuffle(red_pool)
        rng.shuffle(other_pool)
        for i in range(24):
            if sum(1 for p in picks[:i] if p in red_pool) < 12 and (i % 2 == 0):
                picks.append(red_pool.pop())
            elif other_pool:
                picks.append(other_pool.pop())
        while len(picks) < 24:
            picks.append(red_pool.pop())
        assert sum(1 for p in picks if p in {i for i in range(30) if i % 6 < 3}) == 12

        ring = Circle(radius=0.24, color=WHITE, stroke_width=4)
        for idx in picks:
            d = pebbles[idx]
            is_red = idx % 6 < 3
            ring.move_to(d)
            anims = [FadeIn(ring, scale=0.4)]
            self.play(*anims, run_time=0.16, rate_func=linear)
            inc = [cnt_n.animate.increment_value(1)]
            if is_red:
                inc.append(cnt_r.animate.increment_value(1))
            self.play(
                *inc,
                FadeOut(ring, scale=1.6),
                Flash(d, color=WHITE, flash_radius=0.3, num_lines=6),
                run_time=0.22,
                rate_func=linear,
            )

        ro.unwire()
        approx = mtex(r"\approx \frac{12}{24} = \frac{1}{2}", size=34, color=INK)
        approx.next_to(ro, DOWN, buff=0.5)
        again = txt("the wall said ½ too!", 23, GREEN_C)
        again.next_to(approx, DOWN, buff=0.2)
        self.play(Write(approx), run_time=0.9)
        self.play(FadeIn(again, shift=UP * 0.15), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(ro),
            FadeOut(approx),
            FadeOut(again),
            FadeOut(banner),
            other.animate.set_fill(opacity=0.18),
            st["s_box"].animate.set_stroke(opacity=0.35),
            st["lab_s"].animate.set_opacity(0.35),
            st["brace_s"].animate.set_opacity(0.35),
            run_time=0.9,
        )

        reasons = VGroup(
            txt("one random pick lands on exactly one pebble.", 25, INK),
            VGroup(txt("it lands in ", 25, INK), mtex(r"A", size=30, color=RED_C), txt(" for 15 of the 30 pebbles.", 25, INK)).arrange(RIGHT, buff=0.08),
            VGroup(txt("so the chance of ", 25, INK), mtex(r"A", size=30, color=RED_C), txt(" is the red share of ", 25, INK), mtex(r"S", size=30, color=COL_S), txt(".", 25, INK)).arrange(RIGHT, buff=0.08),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        reasons.to_corner(DL, buff=0.55)
        for r in reasons:
            self.play(FadeIn(r, shift=RIGHT * 0.25), run_time=0.85)
            self.wait(0.55)
        self.wait(0.6)

        row = VGroup(
            mtex(r"P(A)", size=46),
            mtex(r"=", size=46),
            mtex(r"\frac{|A|}{|S|}", size=46),
            mtex(r"=", size=46),
            mtex(r"\frac{15}{30}", size=46),
            mtex(r"=", size=46),
            mtex(r"\frac{1}{2}", size=46, color=GOLD),
        ).arrange(RIGHT, buff=0.2)
        row.move_to(RIGHT * 4.35 + UP * 1.15)
        for p in row:
            p.save_state()

        self.play(
            LaggedStart(*[FadeIn(p, scale=0.7) for p in row[:3]], lag_ratio=0.3),
            run_time=1.4,
        )
        arr_a = CurvedArrow(
            st["lab_a"].get_top() + UP * 0.05,
            row[2].get_corner(UL) + RIGHT * 0.35 + DOWN * 0.15,
            color=RED_C,
            stroke_width=3,
            angle=0.55,
        )
        arr_s = CurvedArrow(
            st["lab_s"].get_right() + RIGHT * 0.05,
            row[2].get_corner(DL) + RIGHT * 0.35 + UP * 0.15,
            color=COL_S,
            stroke_width=3,
            angle=-0.5,
        )
        self.play(GrowFromPoint(arr_a, arr_a.get_end()), run_time=0.8)
        self.play(GrowFromPoint(arr_s, arr_s.get_end()), run_time=0.8)
        self.wait(0.5)
        self.play(
            LaggedStart(*[FadeIn(p, scale=0.7) for p in row[3:]], lag_ratio=0.3),
            run_time=1.4,
        )
        self.wait(1.4)

        share_cap = VGroup(
            txt("probability  =  favorable outcomes  ÷  total outcomes", 24, SUB)
        )
        share_cap.next_to(row, DOWN, buff=0.55)
        self.play(FadeIn(share_cap, shift=UP * 0.2), run_time=0.8)
        self.wait(0.8)

        self.play(
            *[FadeOut(r) for r in reasons],
            FadeOut(arr_a),
            FadeOut(arr_s),
            FadeOut(share_cap),
            FadeOut(st["cap"]),
            run_time=0.7,
        )

        self.play(
            self.camera.frame.animate.scale(0.62).move_to(RIGHT * 4.35 + UP * 0.9),
            run_time=1.3,
        )
        final = mtex(
            r"P_{\mathrm{naive}}(A)",
            r"=",
            r"\frac{|A|}{|S|}",
            size=58,
        )
        fbox = box_around(final, 0.5, 0.38, stroke=INK, sw=3, corner=0.22)
       fcap = txt("the naive definition of probability", 27, GOLD)
        fcap.next_to(fbox, DOWN, buff=0.32)
        cred = txt("after Blitzstein & Hwang, Introduction to Probability", 18, SUB)
        cred.next_to(fcap, DOWN, buff=0.14)

        self.play(
            FadeOut(row),
            FadeIn(final),
            Create(fbox),
            run_time=1.2,
        )
        self.play(FadeIn(fcap, shift=UP * 0.2), run_time=0.7)
        self.play(FadeIn(cred), run_time=0.5)
        self.wait(2.2)

        self.play(
            self.camera.frame.animate.scale(1 / 0.62).move_to(ORIGIN),
            FadeOut(final),
            FadeOut(fbox),
            FadeOut(fcap),
            FadeOut(cred),
            run_time=1.2,
        )
        self.final_formula = (final, fbox, fcap)
        self._wipe(keep=[getattr(self, "_kick", None)] + list(pebbles) + [st["s_box"], st["ell"], st["s_lab"], st["a_lab"], st["brace_a"], st["lab_a"], st["brace_s"], st["lab_s"]])

    def _act_die(self):
        self._kicker("04  ·  putting it to work")
        head = VGroup(
            txt("a fair die — six equally likely faces.", 29, INK),
            VGroup(txt("what is the chance of rolling ", 29, INK), txt("even?", 29, GOLD, weight=BOLD)).arrange(RIGHT, buff=0.03),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        head.move_to(LEFT * 3.3 + UP * 2.85)
        self.play(FadeIn(head[0], shift=DOWN * 0.2), run_time=0.7)
        self.play(FadeIn(head[1], shift=DOWN * 0.2), run_time=0.7)

        faces = VGroup(*[die_face(n, hot=(n % 2 == 0), cold=(n % 2 == 1)) for n in range(1, 7)])
        faces.arrange(RIGHT, buff=0.42).move_to(LEFT * 3.3 + UP * 0.75)

        self.play(
            LaggedStart(*[GrowFromCenter(f) for f in faces], lag_ratio=0.12),
            run_time=1.8,
        )
        self.play(
            *[Indicate(f, scale_factor=1.15, color=GOLD) for f in (faces[1], faces[3], faces[5])],
            run_time=1.1,
        )
        self.wait(0.4)

        brace_e = Brace(VGroup(faces[1], faces[3], faces[5]), UP, color=GOLD, buff=0.14)
        lab_e = mtex(r"|A| = 3", size=34, color=GOLD).next_to(brace_e, UP, buff=0.16)
        brace_t = Brace(faces, DOWN, color=COL_S, buff=0.14)
        lab_t = mtex(r"|S| = 6", size=34, color=COL_S).next_to(brace_t, DOWN, buff=0.16)
        self.play(GrowFromCenter(brace_e), Write(lab_e), GrowFromCenter(brace_t), Write(lab_t), run_time=1.2)

        eq = VGroup(
            mtex(r"P(\text{even})", size=42),
            mtex(r"=", size=42),
            mtex(r"\frac{3}{6}", size=42),
            mtex(r"=", size=42),
            mtex(r"\frac{1}{2}", size=42, color=GOLD),
        ).arrange(RIGHT, buff=0.18)
        eq.move_to(LEFT * 3.3 + DOWN * 1.75)
        self.play(LaggedStart(*[Write(p) for p in eq], lag_ratio=0.25), run_time=1.8)
        self.wait(1.2)

        dot_cols = [SUB, GOLD, SUB, GOLD, SUB, GOLD]
        dots6 = VGroup(*[Dot(radius=0.105, color=c) for c in dot_cols])
        dots6.arrange_in_grid(rows=2, cols=3, buff=(0.66, 0.66))
        dots6.move_to(RIGHT * 4.35 + UP * 0.9)
        order = [0, 2, 4, 1, 3, 5]
        dots_ordered = VGroup(*[dots6[i] for i in order])

        ell6 = DashedVMobject(
            Ellipse(width=dots6.width * 0.78, height=dots6.height * 0.62).move_to(
                VGroup(dots6[1], dots6[3], dots6[5]).get_center()
            ),
            num_dashes=26,
        ).set_stroke(GOLD, 3)
        a6 = mtex(r"A", size=44, color=GOLD).next_to(ell6, DOWN, buff=0.2)
        cap6 = txt("same story, any finite setup", 24, SUB)
        cap6.next_to(dots6, DOWN, buff=1.15)

        self.play(FadeIn(cap6, shift=UP * 0.2), run_time=0.6)
        self.play(
            *[ReplacementTransform(faces[i], dots_ordered[i]) for i in range(6)],
            run_time=1.5,
        )
        self.play(Create(ell6), FadeIn(a6), run_time=0.9)
        self.wait(1.4)

        self._wipe()

    def _act_limits(self, rng):
        self._kicker("05  ·  handle with care")
        head = txt("the naive definition only works when…", 30, INK)
        head.to_edge(UP, buff=0.75)
        self.play(FadeIn(head, shift=DOWN * 0.2), run_time=0.8)

        mw = Rectangle(width=3.5, height=2.6, stroke_color=WALL_E, stroke_width=2.5).set_fill(WALL_F, 1.0)
        mw.move_to(LEFT * 3.5 + UP * 1.35)
        mlab = txt("a dart hits a point of the wall…", 25, INK)
        mlab.next_to(mw, DOWN, buff=0.3)
        self.play(Create(mw), FadeIn(mlab), run_time=1.0)

        n_dart = 320
        dart_pts = VGroup()
        for _ in range(n_dart):
            px = rng.uniform(-1, 1) * (mw.width / 2 - 0.08)
            py = rng.uniform(-1, 1) * (mw.height / 2 - 0.08)
            dart_pts.add(
                Dot(radius=0.024, color=PEB).move_to(mw.get_center() + RIGHT * px + UP * py)
            )
        self.play(LaggedStartMap(FadeIn, dart_pts, lag_ratio=0.008), run_time=2.4)
        self.wait(0.3)

        inf_eq = VGroup(
            mtex(r"P(A)", size=40),
            mtex(r"=", size=40),
            mtex(r"\frac{|A|}{|S|}", size=40),
            mtex(r"=", size=40),
            mtex(r"\frac{\infty}{\infty}", size=40, color=BAD),
        ).arrange(RIGHT, buff=0.16)
        inf_eq.move_to(LEFT * 3.5 + DOWN * 0.95)
        fail = txt("uncountably many points — counting breaks down", 24, BAD)
        fail.next_to(inf_eq, DOWN, buff=0.3)
        cr = Cross(inf_eq[4], stroke_color=BAD, stroke_width=5).scale(1.15)
        self.play(LaggedStart(*[FadeIn(p, scale=0.7) for p in inf_eq], lag_ratio=0.2), run_time=1.5)
        self.play(Create(cr), FadeIn(fail, shift=UP * 0.15), run_time=0.9)
        geo = txt("(geometry takes over: area ratios)", 21, SUB)
        geo.next_to(fail, DOWN, buff=0.16)
        self.play(FadeIn(geo), run_time=0.5)
        self.wait(1.2)

        gq = txt("two fair dice — what is P(sum = 7)?", 26, INK)
        gq.move_to(RIGHT * 3.5 + UP * 3.0)
        cells = VGroup()
        for i in range(6):
            for j in range(6):
                sq = Square(side=0.37, stroke_width=1.6, stroke_color=WALL_E).set_fill(WALL_F, 0.9)
                cells.add(sq)
        cells.arrange_in_grid(rows=6, cols=6, buff=0.055)
        cells.move_to(RIGHT * 3.5 + UP * 1.15)
        ax1 = txt("die 1 →", 20, SUB).next_to(cells, DOWN, buff=0.16)
        ax2 = txt("die 2 ↑", 20, SUB).rotate(90 * DEGREES).next_to(cells, LEFT, buff=0.16)
        self.play(FadeIn(gq, shift=DOWN * 0.2), run_time=0.7)
        self.play(LaggedStartMap(FadeIn, cells, lag_ratio=0.015), FadeIn(ax1), FadeIn(ax2), run_time=1.6)

        sum7 = VGroup(*[cells[i * 6 + (6 - i - 1)] for i in range(6)])
        sum2 = cells[0]
        self.play(
            *[c.animate.set_fill(RED_C, 0.85).set_stroke(RED_C, 2) for c in sum7],
            run_time=1.2,
        )
        lab7 = mtex(r"\text{sum}=7:\; 6 \text{ pairs}", size=30, color=RED_C)
        lab7.next_to(cells, DOWN, buff=0.75).align_to(cells, LEFT)
        self.play(FadeIn(lab7, shift=UP * 0.15), run_time=0.6)
        self.play(sum2.animate.set_fill(BLUE_C, 0.9).set_stroke(BLUE_C, 2.4), run_time=0.5)
        lab2 = mtex(r"\text{sum}=2:\; 1 \text{ pair}", size=30, color=BLUE_C)
        lab2.next_to(lab7, DOWN, buff=0.18).align_to(lab7, LEFT)
        self.play(FadeIn(lab2, shift=UP * 0.15), run_time=0.6)
        self.wait(0.6)

        wrong = VGroup(
            txt("treating the 11 sums as equally likely?", 24, SUB),
            mtex(r"\frac{1}{11}", size=36, color=BAD),
        ).arrange(RIGHT, buff=0.3)
        wrong.move_to(RIGHT * 3.5 + DOWN * 1.55)
        cw = Cross(wrong[1], stroke_color=BAD, stroke_width=5).scale(1.2)
        right = mtex(r"P(7)=\tfrac{6}{36}, \quad P(2)=\tfrac{1}{36}", size=30, color=INK)
        right.move_to(RIGHT * 3.5 + DOWN * 2.45)
        why = txt("the pairs are equally likely — the sums are not.", 24, OKC)
        why.next_to(right, DOWN, buff=0.25)
        self.play(FadeIn(wrong, shift=UP * 0.15), run_time=0.7)
        self.play(Create(cw), run_time=0.6)
        self.play(FadeIn(right, shift=UP * 0.15), run_time=0.8)
        self.play(FadeIn(why, shift=UP * 0.15), run_time=0.6)
        self.wait(1.5)

        self._wipe(keep=[head])
        self.play(FadeOut(head), run_time=0.5)

        title = txt("so the naive definition demands", 28, INK)
        chk1 = VGroup(mtex(r"\checkmark", size=40, color=OKC), txt("a finite sample space", 27, INK)).arrange(RIGHT, buff=0.28)
        chk2 = VGroup(mtex(r"\checkmark", size=40, color=OKC), txt("equally likely outcomes", 27, INK)).arrange(RIGHT, buff=0.28)
        ex = txt("fair coins  ·  shuffled decks  ·  random samples", 22, SUB)
        card_items = VGroup(chk1, chk2).arrange(RIGHT, buff=2.6)
        card_grp = VGroup(title, card_items, ex).arrange(DOWN, buff=0.42)
        card = box_around(card_grp, 0.8, 0.55, stroke=WALL_E, sw=2.5, corner=0.25)
        card_grp.move_to(ORIGIN + DOWN * 0.15)
        card.move_to(card_grp.get_center())

        self.play(FadeIn(title, shift=UP * 0.2), Create(card), run_time=1.0)
        self.play(FadeIn(chk1, shift=UP * 0.15), Flash(chk1[0], color=OKC, flash_radius=0.3), run_time=0.8)
        self.play(FadeIn(chk2, shift=UP * 0.15), Flash(chk2[0], color=OKC, flash_radius=0.3), run_time=0.8)
        self.play(FadeIn(ex), run_time=0.6)
        self.wait(1.8)
        self._wipe()

    def _finale(self):
        final, fbox, fcap = self.final_formula
        grp = VGroup(final, fbox)
        grp.move_to(UP * 1.0)
        fcap.next_to(fbox, DOWN, buff=0.35)

        chk1 = VGroup(mtex(r"\checkmark", size=36, color=OKC), txt("finite ", 25, INK), mtex(r"S", size=34, color=COL_S)).arrange(RIGHT, buff=0.15)
        chk2 = VGroup(mtex(r"\checkmark", size=36, color=OKC), txt("equally likely outcomes", 25, INK)).arrange(RIGHT, buff=0.15)
        chips = VGroup(chk1, chk2).arrange(RIGHT, buff=1.6)
        c1 = box_around(chk1, 0.32, 0.18, stroke=WALL_E, sw=2, corner=0.3)
        c2 = box_around(chk2, 0.32, 0.18, stroke=WALL_E, sw=2, corner=0.3)
        chips_v = VGroup(chk1, chk2)
        chips_v.next_to(fcap, DOWN, buff=0.7)
        c1.move_to(chk1.get_center())
        c2.move_to(chk2.get_center())

        closing = txt(
            "list the possibilities, treat them fairly — and probability becomes counting.",
            29,
            INK,
            slant=ITALIC,
        )
        closing.next_to(chips_v, DOWN, buff=0.85)

        self.play(FadeIn(final), Create(fbox), FadeIn(fcap), run_time=1.2)
        self.play(FadeIn(chk1, scale=0.9), Create(c1), FadeIn(chk2, scale=0.9), Create(c2), run_time=1.0)
        self.wait(0.8)
        self.play(FadeIn(closing, shift=UP * 0.25), run_time=1.1)
        self.wait(2.6)
        self.play(
            *[FadeOut(m) for m in self.mobjects],
            run_time=1.8,
        )
        self.wait(0.6)


def _unused():
    pass
