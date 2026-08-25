"""
Three-dimensional vector visualization helpers for the study notebooks.

Import from any notebook in this project (no sys.path hacks needed):
    from math_study.plotting.three_d import plot_vectors_3d, plot_plane_span_3d
"""

import numpy as np
import matplotlib.pyplot as plt

_DEFAULT_COLORS = ["blue", "red", "green", "purple", "orange"]


def plot_vectors_3d(vectors, labels=None, colors=None, title="", ax=None):
    """
    Plot one or more 3D vectors as arrows from the origin.

    When no axis is given, a new figure with a 3D axis is created and the
    limits are set symmetrically around the origin. When an existing axis
    is passed, limits are left untouched.

    Args:
        vectors: list of [x, y, z] vectors
        labels:  optional list of strings, one per vector
        colors:  optional list of matplotlib colors, one per vector
        title:   plot title
        ax:      optional existing 3D matplotlib axis to draw on

    Returns:
        The matplotlib axis used.
    """
    created_ax = ax is None
    if ax is None:
        _, ax = plt.subplots(figsize=(7, 7), subplot_kw={"projection": "3d"})

    n = len(vectors)
    if labels is None:
        labels = [f"v{i+1}" for i in range(n)]
    if colors is None:
        colors = [_DEFAULT_COLORS[i % len(_DEFAULT_COLORS)] for i in range(n)]

    for v, label, color in zip(vectors, labels, colors):
        v = np.asarray(v, dtype=float)
        ax.quiver(0, 0, 0, v[0], v[1], v[2], color=color, linewidth=2,
                  arrow_length_ratio=0.08)
        ax.text(v[0], v[1], v[2], f"  {label}", color=color, fontsize=11)

    if created_ax:
        max_val = max(abs(x) for v in vectors for x in v) + 1
        ax.set_xlim(-max_val, max_val)
        ax.set_ylim(-max_val, max_val)
        ax.set_zlim(-max_val, max_val)

    ax.set_xlabel("$x$", fontsize=11)
    ax.set_ylabel("$y$", fontsize=11)
    ax.set_zlabel("$z$", fontsize=11)
    ax.set_title(title, fontsize=13)
    return ax


def plot_plane_span_3d(v, w, extent=1.0, num_points=20, alpha=0.25,
                       color="gray", title="", ax=None):
    """
    Shade the plane spanned by two 3D vectors: all points c*v + d*w with
    both coefficients running over [-extent, extent].

    Args:
        v, w:       the two spanning [x, y, z] vectors
        extent:     half-width of the shaded patch along each direction
        num_points: grid resolution per axis
        alpha:      surface opacity
        color:      surface color
        title:      plot title
        ax:         optional existing 3D matplotlib axis to draw on

    Returns:
        The matplotlib axis used.
    """
    if ax is None:
        _, ax = plt.subplots(figsize=(7, 7), subplot_kw={"projection": "3d"})

    v, w = np.asarray(v, dtype=float), np.asarray(w, dtype=float)
    c_vals = np.linspace(-extent, extent, num_points)
    d_vals = np.linspace(-extent, extent, num_points)
    C, D = np.meshgrid(c_vals, d_vals)

    ax.plot_surface(C * v[0] + D * w[0],
                    C * v[1] + D * w[1],
                    C * v[2] + D * w[2],
                    alpha=alpha, color=color)
    ax.set_title(title, fontsize=13)
    return ax
