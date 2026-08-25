# math-study

Mathematics study notebooks, organized by subject, with shared plotting code in an installable package.

## Layout

```
src/math_study/          Python package (installed editable into .venv)
  └── plotting/          Shared matplotlib helpers, one module per topic
notebooks/
  algebra/               Study notebooks
  calculus/
  linear_algebra/
  numpy/
  probability/
videos/                  Manim video projects (one folder per video)
exercises/               Exercise work by subject
assets/                  Images and other static assets
```

## Getting started

```bash
uv sync
uv run jupyter lab
```

The project is installed editable, so every notebook can import package code directly — no `sys.path` hacks:

```python
from math_study.plotting.vectors import (
    plot_vectors_2d,
    plot_vector_addition,
    plot_scalar_multiplication,
    plot_span_2d,
)
```

## Adding shared code

Anything used by more than one notebook belongs in `src/math_study`. Plotting helpers are grouped by math topic under `math_study.plotting` (e.g. `vectors.py`, later `functions.py`, `systems.py`). Re-export new public functions from `src/math_study/plotting/__init__.py` so both import styles work:

```python
from math_study.plotting.functions import plot_function      # specific module
from math_study.plotting import plot_function                # convenience re-export
```

After adding a module, restart the notebook kernel to pick up changes.

## Conventions

- Notebooks follow a fixed per-concept template: **Concept → Notation → Worked example → Code → Visualization → Key question** (see `notebooks/linear_algebra/readme.md`).
- Manim render sources live in `videos/<video-name>/`; build output (`media/`) is gitignored.
