# Sample Space & Events

## Overview
- **Topic**: Sample space (Ω) and events as subsets — dartboard analogy → formal definition
- **Hook**: Where *can* a thrown dart land?
- **Aha moment**: "Event A occurred" simply means the actual outcome landed inside region A ⊆ S
- **Target audience**: Intro probability students
- **Source**: `notebooks/probability/01/lessons/012-sample-space.ipynb` (Analogy, Diagram, Plain English, Technical sections)
- **Length**: ~2.5 min
- **Resolution**: 480p15 draft / 1080p60 final

## Color Palette
- Background: #191919
- Primary: #2D4263 -- sample space board / set S fill (structural)
- Secondary: #C84B31 -- event region A, highlights, final box
- Accent: #ECDBBA -- all text, labels, equations, outcome dots

## On-Screen Text Layers
- Scene 1 title block: "SAMPLE SPACE & EVENTS" / "the building blocks of probability" (replaces header)
- Definition lines under labels: Ω = "all possible outcomes", A = "a subset of outcomes"
- Bottom step lines (Scene 2): S definition → A ⊆ S via ReplacementTransform
- Takeaway line bottom (Scene 1): dart lands in A ⟹ event occurred
- Scene 2: "each dot = one possible outcome" caption above rect (fades with blob)
- Scene 3: Ω explainer ("Omega denotes the sample space: ALL possible outcomes");
  event named in words: E = {2,4,6} ⊆ Ω "(rolling an even number)"
- Scene 4: "one complete history of 10 flips = one outcome"; C-beat = slow sequential
  T→H morph (~3.5s) + "every A_j must occur" note; restore original string before D;
  lead-in "events are combined with set operations:" before OR↔∪ / AND↔∩ box
- Scene 5: "every possible P/L sequence is one outcome in Omega" under boxed Ω

## Arc: Discovery

## Scene 1: DartboardAnalogy (~30s)
**Purpose**: Build the intuition — whole board = sample space, red region = event.
**Layout**: FULL_CENTER → LEFT_RIGHT (board shifts left when labeled)

### Visual elements
- Board: Circle r≈2.2, PRIMARY fill @0.45, ACCENT stroke; 2 concentric rings @0.2 opacity
- Darts: small ACCENT dots at scattered points
- Labels right side: Ω / "Sample Space" (ACCENT), A / "Event" (SECONDARY) + arrow to sector
- Event region: annulus band r=1.5→2.2 (Difference of circles), SECONDARY fill @0.85

### Animation sequence
1. GrowFromCenter board + Create rings (~3s) — "Imagine throwing a dart at a board."
2. LaggedStart FadeIn of 4 darts (~5s) — "It could land anywhere."
3. Indicate board + Write Ω label, board shifts left (~7s) — "The whole board is the sample space."
4. FadeIn sector + Event label + arrow (~6s) — "An event is a particular region."
5. Dart flies into sector, Flash, checkmark (~8s) — "Land in the red — the event occurred."
6. Clean FadeOut exit

## Scene 2: FormalDefinition (~30s)
**Purpose**: Formalize — S set of outcomes, A ⊆ S, occurrence criterion, indicator function.
**Layout**: LEFT_RIGHT (set picture left, equations right)

### Visual elements
- RoundedRectangle S (PRIMARY fill @0.12) with ~9 ACCENT outcome dots
- Blob region A: stretched Circle, SECONDARY fill @0.45; inside dots tinted SECONDARY
- s_actual dot ringed in ACCENT + label + arrow
- Equations: `s_actual ∈ A ⟹ A occurred`; piecewise I_A(s); SurroundingRectangle finale

### Animation sequence
1. GrowFromEdge rect + LaggedStart dots (~7s) — "Formally: S is the set of all possible outcomes."
2. FadeIn blob, tint inside dots, Write A label (~7s) — "An event A is any subset of S."
3. Ring s_actual, Write implication equation (~9s) — "The event occurs iff the actual outcome lies in A."
4. FadeIn indicator cases equation (~5s) — "One if it's in A, zero otherwise."
5. Box implication, hold, clean exit (~2s)

## Scene 3: DieExample (~28s)
**Purpose**: First concrete sample space — die roll Ω := {1,…,6}, mutual exclusivity, event as subset.
### Animation sequence
1. Header + six die faces grow in; Ω equation Write
2. "Mutually exclusive" note bottom
3. Even faces {2,4,6} tinted SECONDARY; E = {2,4,6} ⊆ Ω

## Scene 4: CoinFlipEvents (~45s)
**Purpose**: Events built from A_j via ∪/∩ (Blitzstein): B, C, D; OR↔∪, AND↔∩.
### Animation sequence
1. 10-slot H/T outcome + s = (s₁,…,s₁₀)
2. A₁ highlighted on slot 1
3. B = ∪A_j — Heads slots tinted
4. C = ∩A_j — all slots pulse
5. D = ∪(A_j∩A_{j+1}) — consecutive-HH pairs boxed
6. Boxed mapping: OR ↔ ∪, AND ↔ ∩

## Scene 5: TraderScaleUp (~35s)
**Purpose**: Notebook's trading example — Ω = {P,L}^576, |Ω| = 2^576 exponential blowup.
### Animation sequence
1. Header + trade-rate arithmetic → 576 trades
2. P/L strip builds with ellipsis
3. Boxed Ω = {P,L}^576
4. Exponent chain 2¹ → 2¹⁰ → 2¹⁰⁰ → 2⁵⁷⁶
5. Comparison: ≈2.5×10¹⁷³ ≫ 10⁸⁰ atoms

## Pipeline
1. `manim -ql script.py Scene1_DartboardAnalogy Scene2_FormalDefinition` (draft, via WSL)
2. Preview stills (`--format=png -s`) → visual review
3. `manim -qh ...` production renders
4. ffmpeg concat → `final.mp4`
