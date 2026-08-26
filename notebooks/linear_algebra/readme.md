# Linear Algebra Study Notes

Following Strang, G. (2023). *Introduction to Linear Algebra* (6th ed.). Wellesley-Cambridge Press.

## Structure

- One notebook per book section (`chapter_number`/0Y_section_name.ipynb`).
- NumPy is not a separate track. Code that translates a mathematical statement lives inline, next to that statement; generic Python/NumPy mechanics with no linear-algebra meaning stay out of the notebooks.
- Shared matplotlib visualizations live in `src/math_study/plotting/vectors.py` (installed as the editable `math_study` package), so they aren't copy-pasted across notebooks. Import with:

  ```python
  from math_study.plotting.vectors import (
      plot_vectors_2d,
      plot_vector_addition,
      plot_scalar_multiplication,
      plot_span_2d,
  )
  ```

## Roadmap

### Chapter 1 — Vectors and Matrices
- [x] 1.1 Vectors and Linear Combinations
- [ ] 1.2 Lengths and Angles from Dot Products
- [ ] 1.3 Matrices and Their Column Spaces
- [ ] 1.4 Matrix Multiplication AB and CR

### Chapter 2 — Solving Linear Equations Ax = b
- [ ] 2.1 Elimination and Back Substitution
- [ ] 2.2 Elimination Matrices and Inverse Matrices
- [ ] 2.3 Matrix Computations and A = LU
- [ ] 2.4 Permutations and Transposes
- [ ] 2.5 Derivatives and Finite Difference Matrices

### Chapter 3 — The Four Fundamental Subspaces
- [ ] 3.1 Vector Spaces and Subspaces
- [ ] 3.2 Computing the Nullspace by Elimination A = CR
- [ ] 3.3 The Complete Solution to Ax = b
- [ ] 3.4 Independence, Basis, and Dimension
- [ ] 3.5 Dimensions of the Four Subspaces

### Chapter 4 — Orthogonality
- [ ] 4.1 Orthogonality of Vectors and Subspaces
- [ ] 4.2 Projections onto Lines and Subspaces
- [ ] 4.3 Least Squares Approximations
- [ ] 4.4 Orthonormal Bases and Gram-Schmidt
- [ ] 4.5 The Pseudoinverse of a Matrix

### Chapter 5 — Determinants
- [ ] 5.1 – 5.3

### Chapter 6 — Eigenvalues and Eigenvectors
- [ ] 6.1 – 6.5

