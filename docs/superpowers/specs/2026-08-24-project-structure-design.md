# Project Structure Design — Shared Plotting Code

Date: 2026-08-24

## Problem

`plot_helpers.py` (2D vector plotting functions) sat at the repo root and was consumed only by
`notebooks/linear_algebra/01/01_vectors_linear_combinations.ipynb` via a fragile
`sys.path.append("../tools")` hack pointing at a directory that did not exist. The import worked
only by accident of the kernel's working directory. As algebra/calculus notebooks grow, they will
need shared plotting too, and the root-level module + path hacks do not scale.

Key existing fact: the project (`pyproject.toml`, uv build backend) is installed **editable** into
`.venv` — `.venv/lib/python*/site-packages/math_study.pth` adds `/home/lucas/math/src` to every
kernel's path. The `src/math_study` package existed but was empty.

## Decision

Shared code lives **inside the installed package**: `src/math_study/plotting/`. Notebooks import
with `from math_study.plotting.vectors import ...` from any subject folder — no sys.path hacks,
works for all current and future subjects. Rejected alternatives: a shared `notebooks/tools/`
folder (keeps cwd-fragile sys.path hacks) and leaving the file at the root (messy as it grows).

## Target structure

```
src/math_study/
  __init__.py
  plotting/
    __init__.py        # re-exports public functions
    vectors.py         # former plot_helpers.py (unchanged logic)
notebooks/{algebra,calculus,linear_algebra,numpy,probability}/
videos/                # manim projects: videos/010_naive_definition/, videos/012-sample-space/
exercises/  assets/
```

## Changes applied

1. Moved `plot_helpers.py` → `src/math_study/plotting/vectors.py` (docstring updated with new
   import pattern; function bodies untouched). Added `plotting/__init__.py` re-exporting the four
   public functions. Deleted the root file.
2. Rewrote the import cell in `01_vectors_linear_combinations.ipynb`: dropped the broken
   `sys.path.append("../tools")`, imports from `math_study.plotting.vectors`.
3. Updated `notebooks/linear_algebra/readme.md`: removed references to nonexistent
   `tools/numpy_primer.ipynb`; documented the package location and import line.
4. Deleted four empty (0-byte, invalid JSON) placeholder notebooks:
   `vectors_matrices.ipynb`, `counting_exercises.ipynb`,
   `calculus/010naive_definition.ipynb`, `calculus/011multiplication_rule.ipynb`.
5. Relocated manim project sources (`script.py`, `plan.md`, `check_stills.sh`, `final.mp4`)
   from `notebooks/probability/manim/012-sample-space/` to `videos/012-sample-space/`, matching
   the existing `videos/` convention. Generated artifacts (`media/`, `__pycache__/`, `concat.txt`)
   stay behind, untracked.
6. Fixed `.gitignore`: the old entry `venv` did not match `.venv/` (the venv was about to be
   committed). Added `.venv/`, `__pycache__/`, packaging outputs, `.ipynb_checkpoints/`, and the
   manim artifact directory.
7. Wrote this design doc and the root `README.md`.

## Extension path

New shared helpers become sibling modules grouped by math topic
(`plotting/functions.py`, `plotting/systems.py`, ...), each re-exported from
`plotting/__init__.py`. No configuration or path changes needed — any notebook imports them
immediately after a kernel restart.

## Verification

- `from math_study.plotting import <all four functions>` succeeds from repo root and from inside
  notebook subfolders using `.venv/bin/python`.
- No remaining `plot_helpers` / `sys.path` references outside `.venv`.
- Edited notebook parses cleanly with `nbformat`.
