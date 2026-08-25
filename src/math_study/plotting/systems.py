"""
Linear system visualization helpers for the study notebooks.

Import from any notebook in this project (no sys.path hacks needed):
    from math_study.plotting.systems import plot_lines
"""

import numpy as np
import matplotlib.pyplot as plt


def _equation_label(row):
    """Format one row of an augmented matrix as a LaTeX equation string."""
    sign = "+" if row[1] >= 0 else "-"
    return f"${row[0]:g}x_1 {sign} {abs(row[1]):g}x_2 = {row[2]:g}$"


def plot_lines(M, ax=None):
    """
    Plot each equation of a 2x3 augmented matrix as a line in the plane,
    marking the intersection point when the system has exactly one solution.

    Args:
        M: augmented matrix with shape (2, 3). Row i holds the two
           coefficients of equation i and its right-hand side, so each row
           describes the line  M[i,0]*x1 + M[i,1]*x2 = M[i,2].
           The x2 coefficients must be nonzero (vertical lines unsupported).
        ax: optional existing matplotlib axis to draw on

    Returns:
        The matplotlib axis used.
    """
    if M.shape != (2, 3):
        raise ValueError("plot_lines expects an augmented matrix of shape (2, 3)")
    if ax is None:
        _, ax = plt.subplots(figsize=(7, 7))

    x_1 = np.linspace(-10, 10, 100)
    colors = ["#0075ff", "#ff7300"]
    for row, color in zip(M, colors):
        x_2 = (row[2] - row[0] * x_1) / row[1]
        ax.plot(x_1, x_2, linewidth=2, color=color, label=_equation_label(row))

    A = M[:, :2]
    b = M[:, 2]
    if abs(np.linalg.det(A)) > 1e-12:
        solution = np.linalg.solve(A, b)
        ax.plot(solution[0], solution[1], "o", mfc="none", markersize=12,
                markeredgecolor="#ff0000", markeredgewidth=2)
        ax.annotate(f"solution ({solution[0]:g}, {solution[1]:g})",
                    (solution[0], solution[1]), textcoords="offset points",
                    xytext=(12, 10), fontsize=11, color="#ff0000")

    ax.axhline(y=0, color="black", linewidth=0.8, alpha=0.4)
    ax.axvline(x=0, color="black", linewidth=0.8, alpha=0.4)
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.grid(True, alpha=0.3)
    ax.set_aspect("equal")
    ax.set_xlabel("$x_1$", fontsize=12)
    ax.set_ylabel("$x_2$", fontsize=12)
    ax.legend(loc="upper right", fontsize=10)
    return ax
