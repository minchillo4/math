"""
2D vector visualization helpers for the Linear Algebra study notebooks.

Import from any notebook in this project (no sys.path hacks needed):
    from math_study.plotting.vectors import plot_vectors_2d, plot_linear_combinations_2d
"""

import numpy as np
import matplotlib.pyplot as plt


def plot_vectors_2d(vectors, labels=None, colors=None, title="", ax=None):
    """
    Plot one or more 2D vectors as arrows from the origin.

    Args:
        vectors: list of [x, y] vectors
        labels:  optional list of strings, one per vector
        colors:  optional list of matplotlib colors, one per vector
        title:   plot title
        ax:      optional existing matplotlib axis to draw on

    Returns:
        The matplotlib axis used.
    """
    if ax is None:
        _, ax = plt.subplots(figsize=(6, 6))

    n = len(vectors)
    if labels is None:
        labels = [f"v{i+1}" for i in range(n)]
    if colors is None:
        default_colors = ["blue", "red", "green", "purple", "orange"]
        colors = [default_colors[i % len(default_colors)] for i in range(n)]

    all_x = [0] + [v[0] for v in vectors]
    all_y = [0] + [v[1] for v in vectors]
    max_val = max(abs(min(all_x)), abs(max(all_x)), abs(min(all_y)), abs(max(all_y))) + 1

    for v, label, color in zip(vectors, labels, colors):
        ax.arrow(0, 0, v[0], v[1],
                  head_width=0.15, head_length=0.15,
                  fc=color, ec=color, length_includes_head=True, linewidth=2)
        ax.text(v[0] + 0.15, v[1] + 0.15, f"{label} = {v}", color=color, fontsize=11)

    ax.set_xlim(-max_val, max_val)
    ax.set_ylim(-max_val, max_val)
    ax.axhline(y=0, color="black", linewidth=0.8, alpha=0.4)
    ax.axvline(x=0, color="black", linewidth=0.8, alpha=0.4)
    ax.grid(True, alpha=0.3)
    ax.set_aspect("equal")
    ax.set_title(title, fontsize=13)
    return ax


def plot_vector_addition(v, w, ax=None):
    """Visualize v + w via the parallelogram law."""
    v, w = np.array(v), np.array(w)
    v_plus_w = v + w

    if ax is None:
        _, ax = plt.subplots(figsize=(6, 6))

    plot_vectors_2d(
        [v.tolist(), w.tolist(), v_plus_w.tolist()],
        labels=["v", "w", "v + w"],
        colors=["blue", "red", "green"],
        title=f"v + w = {v_plus_w.tolist()}",
        ax=ax,
    )
    # dashed parallelogram sides
    ax.arrow(v[0], v[1], w[0], w[1], head_width=0.08, head_length=0.08,
              fc="red", ec="red", linestyle="dashed", alpha=0.4)
    ax.arrow(w[0], w[1], v[0], v[1], head_width=0.08, head_length=0.08,
              fc="blue", ec="blue", linestyle="dashed", alpha=0.4)
    return ax


def plot_scalar_multiplication(v, scalars, ax=None):
    """Overlay v and several scaled versions c*v on one plot."""
    v = np.array(v)
    if ax is None:
        _, ax = plt.subplots(figsize=(7, 7))

    vectors = [v.tolist()] + [(c * v).tolist() for c in scalars]
    labels = ["v"] + [f"{c}v" for c in scalars]
    colors = ["black"] + list(plt.cm.viridis(np.linspace(0, 1, len(scalars))))

    plot_vectors_2d(vectors, labels=labels, colors=colors,
                     title=f"Scalar multiplication of v = {v.tolist()}", ax=ax)
    return ax


def plot_span_2d(v, w, num_points=400, seed=42, ax=None):
    """
    Scatter many random linear combinations c*v + d*w to show whether
    they fill a plane (independent) or collapse onto a line (dependent).
    """
    v, w = np.array(v, dtype=float), np.array(w, dtype=float)
    rng = np.random.default_rng(seed)
    c_vals = rng.uniform(-3, 3, num_points)
    d_vals = rng.uniform(-3, 3, num_points)
    points = np.array([c * v + d * w for c, d in zip(c_vals, d_vals)])

    if ax is None:
        _, ax = plt.subplots(figsize=(7, 7))

    ax.scatter(points[:, 0], points[:, 1], c="purple", alpha=0.25, s=8,
               label="c·v + d·w")
    plot_vectors_2d([v.tolist(), w.tolist()], labels=["v", "w"],
                     colors=["red", "blue"], ax=ax)

    is_dependent = abs(v[0] * w[1] - v[1] * w[0]) < 1e-10
    shape = "LINE (dependent)" if is_dependent else "PLANE (independent)"
    ax.set_title(f"Span of v and w → {shape}", fontsize=13)
    ax.legend(loc="upper left", fontsize=9)
    return ax
