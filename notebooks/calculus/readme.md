# Calculus Study Notes

Following Stewart, J. (2021). *Calculus* (9th ed.). Cengage Learning.

## Structure

- One notebook per book section (`chapter_number/0Y_section_name.ipynb`).
- Each notebook follows a fixed 6-step template per concept: **Concept → Notation → Worked example → Code → Visualization → Key question**.
- Shared matplotlib visualizations live in `src/math_study/plotting/calculus.py` (installed as the editable `math_study` package), so they aren't copy-pasted across notebooks. Import with:

  ```python
  from math_study.plotting.calculus import (
      plot_function,
      plot_derivative,
      plot_integral,
      plot_sequence,
      plot_vector_field,
  )
  ```

## Roadmap

> **Note:** Sections 1.1–1.4 (*Four Ways to Represent a Function*, *Mathematical Models*, *New Functions from Old Functions*, *The Tangent and Velocity Problems*) are not included per scope. We start at 1.5.

### Chapter 1 — Functions and Limits
- [x] 1.5 The Limit of a Function
- [ ] 1.6 Calculating Limits Using the Limit Laws
- [ ] 1.7 The Precise Definition of a Limit
- [ ] 1.8 Continuity
- [ ] Review (Chapter 1)
- [ ] Principles of Problem Solving

### Chapter 2 — Derivatives
- [ ] 2.1 Derivatives and Rates of Change
- [ ] writing project • Early Methods for Finding Tangents
- [ ] 2.2 The Derivative as a Function
- [ ] 2.3 Differentiation Formulas
- [ ] applied project • Building a Better Roller Coaster
- [ ] 2.4 Derivatives of Trigonometric Functions
- [ ] 2.5 The Chain Rule
- [ ] applied project • Where Should a Pilot Start Descent?
- [ ] 2.6 Implicit Differentiation
- [ ] discovery project • Families of Implicit Curves
- [ ] 2.7 Rates of Change in the Natural and Social Sciences
- [ ] 2.8 Related Rates
- [ ] 2.9 Linear Approximations and Differentials
- [ ] discovery project • Polynomial Approximations
- [ ] Review (Chapter 2)
- [ ] Problems Plus (Chapter 2)

### Chapter 3 — Applications of Differentiation
- [ ] 3.1 Maximum and Minimum Values
- [ ] applied project • The Calculus of Rainbows
- [ ] 3.2 The Mean Value Theorem
- [ ] 3.3 What Derivatives Tell Us about the Shape of a Graph
- [ ] 3.4 Limits at Infinity; Horizontal Asymptotes
- [ ] 3.5 Summary of Curve Sketching
- [ ] 3.6 Graphing with Calculus and Technology
- [ ] 3.7 Optimization Problems
- [ ] applied project • The Shape of a Can
- [ ] applied project • Planes and Birds: Minimizing Energy
- [ ] 3.8 Newton’s Method
- [ ] 3.9 Antiderivatives
- [ ] Review (Chapter 3)
- [ ] Problems Plus (Chapter 3)

### Chapter 4 — Integrals
- [ ] 4.1 The Area and Distance Problems
- [ ] 4.2 The Definite Integral
- [ ] discovery project • Area Functions
- [ ] 4.3 The Fundamental Theorem of Calculus
- [ ] 4.4 Indefinite Integrals and the Net Change Theorem
- [ ] writing project • Newton, Leibniz, and the Invention of Calculus
- [ ] 4.5 The Substitution Rule
- [ ] Review (Chapter 4)
- [ ] Problems Plus (Chapter 4)

### Chapter 5 — Applications of Integration
- [ ] 5.1 Areas Between Curves
- [ ] applied project • The Gini Index
- [ ] 5.2 Volumes
- [ ] 5.3 Volumes by Cylindrical Shells
- [ ] 5.4 Work
- [ ] 5.5 Average Value of a Function
- [ ] applied project • Calculus and Baseball
- [ ] Review (Chapter 5)
- [ ] Problems Plus (Chapter 5)

### Chapter 6 — Inverse Functions: Exponential, Logarithmic, and Inverse Trigonometric Functions
- [ ] 6.1 Inverse Functions and Their Derivatives
- [ ] 6.2 Exponential Functions and Their Derivatives
- [ ] 6.2* The Natural Logarithmic Function (optional alternative)
- [ ] 6.3 Logarithmic Functions
- [ ] 6.3* The Natural Exponential Function (optional alternative)
- [ ] 6.4 Derivatives of Logarithmic Functions
- [ ] 6.4* General Logarithmic and Exponential Functions (optional alternative)
- [ ] 6.5 Exponential Growth and Decay
- [ ] applied project • Controlling Red Blood Cell Loss During Surgery
- [ ] 6.6 Inverse Trigonometric Functions
- [ ] applied project • Where to Sit at the Movies
- [ ] 6.7 Hyperbolic Functions
- [ ] 6.8 Indeterminate Forms and l’Hospital’s Rule
- [ ] writing project • The Origins of l’Hospital’s Rule
- [ ] Review (Chapter 6)
- [ ] Problems Plus (Chapter 6)

### Chapter 7 — Techniques of Integration
- [ ] 7.1 Integration by Parts
- [ ] 7.2 Trigonometric Integrals
- [ ] 7.3 Trigonometric Substitution
- [ ] 7.4 Integration of Rational Functions by Partial Fractions
- [ ] 7.5 Strategy for Integration
- [ ] 7.6 Integration Using Tables and Technology
- [ ] discovery project • Patterns in Integrals
- [ ] 7.7 Approximate Integration
- [ ] 7.8 Improper Integrals
- [ ] Review (Chapter 7)
- [ ] Problems Plus (Chapter 7)

### Chapter 8 — Further Applications of Integration
- [ ] 8.1 Arc Length
- [ ] discovery project • Arc Length Contest
- [ ] 8.2 Area of a Surface of Revolution
- [ ] discovery project • Rotating on a Slant
- [ ] 8.3 Applications to Physics and Engineering
- [ ] discovery project • Complementary Coffee Cups
- [ ] 8.4 Applications to Economics and Biology
- [ ] 8.5 Probability
- [ ] Review (Chapter 8)
- [ ] Problems Plus (Chapter 8)

### Chapter 9 — Differential Equations
- [ ] 9.1 Modeling with Differential Equations
- [ ] 9.2 Direction Fields and Euler’s Method
- [ ] 9.3 Separable Equations
- [ ] applied project • How Fast Does a Tank Drain?
- [ ] 9.4 Models for Population Growth
- [ ] 9.5 Linear Equations
- [ ] applied project • Which Is Faster, Going Up or Coming Down?
- [ ] 9.6 Predator-Prey Systems
- [ ] Review (Chapter 9)
- [ ] Problems Plus (Chapter 9)

### Chapter 10 — Parametric Equations and Polar Coordinates
- [ ] 10.1 Curves Defined by Parametric Equations
- [ ] discovery project • Running Circles Around Circles
- [ ] 10.2 Calculus with Parametric Curves
- [ ] discovery project • Bézier Curves
- [ ] 10.3 Polar Coordinates
- [ ] discovery project • Families of Polar Curves
- [ ] 10.4 Calculus in Polar Coordinates
- [ ] 10.5 Conic Sections
- [ ] 10.6 Conic Sections in Polar Coordinates
- [ ] Review (Chapter 10)
- [ ] Problems Plus (Chapter 10)

### Chapter 11 — Sequences, Series, and Power Series
- [ ] 11.1 Sequences
- [ ] discovery project • Logistic Sequences
- [ ] 11.2 Series
- [ ] 11.3 The Integral Test and Estimates of Sums
- [ ] 11.4 The Comparison Tests
- [ ] 11.5 Alternating Series and Absolute Convergence
- [ ] 11.6 The Ratio and Root Tests
- [ ] 11.7 Strategy for Testing Series
- [ ] 11.8 Power Series
- [ ] 11.9 Representations of Functions as Power Series
- [ ] 11.10 Taylor and Maclaurin Series
- [ ] discovery project • An Elusive Limit
- [ ] writing project • How Newton Discovered the Binomial Series
- [ ] 11.11 Applications of Taylor Polynomials
- [ ] applied project • Radiation from the Stars
- [ ] Review (Chapter 11)
- [ ] Problems Plus (Chapter 11)

### Chapter 12 — Vectors and the Geometry of Space
- [ ] 12.1 Three-Dimensional Coordinate Systems
- [ ] 12.2 Vectors
- [ ] discovery project • The Shape of a Hanging Chain
- [ ] 12.3 The Dot Product
- [ ] 12.4 The Cross Product
- [ ] discovery project • The Geometry of a Tetrahedron
- [ ] 12.5 Equations of Lines and Planes
- [ ] discovery project • Putting 3D in Perspective
- [ ] 12.6 Cylinders and Quadric Surfaces
- [ ] Review (Chapter 12)
- [ ] Problems Plus (Chapter 12)

### Chapter 13 — Vector Functions
- [ ] 13.1 Vector Functions and Space Curves
- [ ] 13.2 Derivatives and Integrals of Vector Functions
- [ ] 13.3 Arc Length and Curvature
- [ ] 13.4 Motion in Space: Velocity and Acceleration
- [ ] applied project • Kepler’s Laws
- [ ] Review (Chapter 13)
- [ ] Problems Plus (Chapter 13)

### Chapter 14 — Partial Derivatives
- [ ] 14.1 Functions of Several Variables
- [ ] 14.2 Limits and Continuity
- [ ] 14.3 Partial Derivatives
- [ ] discovery project • Deriving the Cobb-Douglas Production Function
- [ ] 14.4 Tangent Planes and Linear Approximations
- [ ] applied project • The Speedo LZR Racer
- [ ] 14.5 The Chain Rule
- [ ] 14.6 Directional Derivatives and the Gradient Vector
- [ ] 14.7 Maximum and Minimum Values
- [ ] discovery project • Quadratic Approximations and Critical Points
- [ ] 14.8 Lagrange Multipliers
- [ ] applied project • Rocket Science
- [ ] applied project • Hydro-Turbine Optimization
- [ ] Review (Chapter 14)
- [ ] Problems Plus (Chapter 14)

### Chapter 15 — Multiple Integrals
- [ ] 15.1 Double Integrals over Rectangles
- [ ] 15.2 Double Integrals over General Regions
- [ ] 15.3 Double Integrals in Polar Coordinates
- [ ] 15.4 Applications of Double Integrals
- [ ] 15.5 Surface Area
- [ ] 15.6 Triple Integrals
- [ ] discovery project • Volumes of Hyperspheres
- [ ] 15.7 Triple Integrals in Cylindrical Coordinates
- [ ] discovery project • The Intersection of Three Cylinders
- [ ] 15.8 Triple Integrals in Spherical Coordinates
- [ ] applied project • Roller Derby
- [ ] 15.9 Change of Variables in Multiple Integrals
- [ ] Review (Chapter 15)
- [ ] Problems Plus (Chapter 15)

### Chapter 16 — Vector Calculus
- [ ] 16.1 Vector Fields
- [ ] 16.2 Line Integrals
- [ ] 16.3 The Fundamental Theorem for Line Integrals
- [ ] 16.4 Green’s Theorem
- [ ] 16.5 Curl and Divergence
- [ ] 16.6 Parametric Surfaces and Their Areas
- [ ] 16.7 Surface Integrals
- [ ] 16.8 Stokes’ Theorem
- [ ] 16.9 The Divergence Theorem
- [ ] 16.10 Summary
- [ ] Review (Chapter 16)
- [ ] Problems Plus (Chapter 16)
```