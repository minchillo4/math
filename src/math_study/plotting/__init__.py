"""Shared plotting helpers for all math-study notebooks."""

from math_study.plotting.systems import plot_lines
from math_study.plotting.three_d import plot_plane_span_3d, plot_vectors_3d
from math_study.plotting.vectors import (
    plot_scalar_multiplication,
    plot_span_2d,
    plot_vector_addition,
    plot_vectors_2d,
)

__all__ = [
    "plot_vectors_2d",
    "plot_vector_addition",
    "plot_scalar_multiplication",
    "plot_span_2d",
    "plot_lines",
    "plot_vectors_3d",
    "plot_plane_span_3d",
]
