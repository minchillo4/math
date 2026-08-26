"""
Limit visualization helpers for the Calculus study notebooks.

Import from any notebook in this project (no sys.path hacks needed):
    from math_study.plotting.limits import plot_secant_slope
"""

import numpy as np
import matplotlib.pyplot as plt


def plot_secant_slope(f=None, f_label="$f(x) = x^2$", a=3.5, b=3.8,
                      zoom_in=False, ax=None):
    """
    Plot f(x) with two points P (at x=a) and Q (at x=b) together with the
    line through them, so the secant slope can be watched settling toward
    the tangent slope as b slides toward a.

    Args:
        f:        callable; the curve under study (default x -> x**2)
        f_label:  LaTeX label used for the curve in the legend
        a:        x-coordinate of point P
        b:        x-coordinate of point Q
        zoom_in:  if True, frame the axes tightly around P
        ax:       optional existing matplotlib axis to draw on

    Returns:
        The matplotlib axis used.
    """
    if f is None:
        def f(x):
            return x**2

    if ax is None:
        _, ax = plt.subplots(figsize=(9, 5), dpi=100)

    # Slope of the line through P and Q; falls back to a central-difference
    # tangent once b lands on a.
    if abs(b - a) < 1e-9:
        h = 1e-6
        m = (f(a + h) - f(a - h)) / (2 * h)
        secant_label = f"Tangent Line (m = {m:.4f})"
    else:
        m = (f(b) - f(a)) / (b - a)
        secant_label = f"Secant Line (m = {m:.4f})"

    # Range configuration (Zoom view vs Global view)
    if zoom_in:
        # Focus closely around point a
        x_min, x_max = a - 0.05, a + 0.05
        y_min, y_max = f(a) - 0.5, f(a) + 0.5
    else:
        # Full view
        x_min, x_max = -10, 10
        y_min, y_max = -10, 100

    x_vals = np.linspace(x_min, x_max, 1000)

    # Plot f(x)
    ax.plot(x_vals, f(x_vals), label=f_label, color="#1f77b4", lw=2)

    # Plot Secant / Tangent Line: y = f(a) + m*(x - a)
    y_secant = f(a) + m * (x_vals - a)
    ax.plot(x_vals, y_secant, "--", label=secant_label, color="#ff7f0e", lw=1.8)

    # Plot Points P and Q
    ax.plot(a, f(a), "ro", markersize=7, label=f"P = ({a:.4f}, {f(a):.4f})")
    ax.plot(b, f(b), "go", markersize=7, label=f"Q = ({b:.4f}, {f(b):.4f})")

    # Graph Formatting
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.set_title(f"Slope m = {m:.6f} | Δx = {(b - a):.4f}",
                 fontsize=12, fontweight="bold")
    ax.legend(loc="upper left", frameon=True)
    return ax
