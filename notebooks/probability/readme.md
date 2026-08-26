# Probability Study Notes

Following Blitzstein, J. K., & Hwang, J. (2019). *Introduction to Probability* (2nd ed.). CRC Press.

## Structure

- One notebook per book section (`chapter_number/0Y_section_name.ipynb`).
- Shared matplotlib visualizations live in `src/math_study/plotting/probability.py` (installed as the editable `math_study` package), so they aren't copy-pasted across notebooks. Import with:

  ```python
  from math_study.plotting.probability import (
      plot_pmf,
      plot_cdf,
      plot_histogram,
      plot_joint_distribution,
  )
  ```

## Roadmap

### Chapter 1 — Probability and Counting
- [ ] 1.1 Why study probability?
- [x] 1.2 Sample spaces and Pebble World
- [x] 1.3 Naive definition of probability
- [ ] 1.4 How to count
- [ ] 1.5 Story proofs
- [ ] 1.6 Non-naive definition of probability
- [ ] 1.7 Recap
- [ ] 1.8 R
- [ ] 1.9 Exercises

### Chapter 2 — Conditional Probability
- [ ] 2.1 The importance of thinking conditionally
- [ ] 2.2 Definition and intuition
- [ ] 2.3 Bayes' rule and the law of total probability
- [ ] 2.4 Conditional probabilities are probabilities
- [ ] 2.5 Independence of events
- [ ] 2.6 Coherency of Bayes' rule
- [ ] 2.7 Conditioning as a problem-solving tool
- [ ] 2.8 Pitfalls and paradoxes
- [ ] 2.9 Recap
- [ ] 2.10 R
- [ ] 2.11 Exercises

### Chapter 3 — Random Variables and Their Distributions
- [ ] 3.1 Random variables
- [ ] 3.2 Distributions and probability mass functions
- [ ] 3.3 Bernoulli and Binomial
- [ ] 3.4 Hypergeometric
- [ ] 3.5 Discrete Uniform
- [ ] 3.6 Cumulative distribution functions
- [ ] 3.7 Functions of random variables
- [ ] 3.8 Independence of r.v.s
- [ ] 3.9 Connections between Binomial and Hypergeometric
- [ ] 3.10 Recap
- [ ] 3.11 R
- [ ] 3.12 Exercises

### Chapter 4 — Expectation
- [ ] 4.1 Definition of expectation
- [ ] 4.2 Linearity of expectation
- [ ] 4.3 Geometric and Negative Binomial
- [ ] 4.4 Indicator r.v.s and the fundamental bridge
- [ ] 4.5 Law of the unconscious statistician (LOTUS)
- [ ] 4.6 Variance
- [ ] 4.7 Poisson
- [ ] 4.8 Connections between Poisson and Binomial
- [ ] 4.9 \*Using probability and expectation to prove existence
- [ ] 4.10 Recap
- [ ] 4.11 R
- [ ] 4.12 Exercises

### Chapter 5 — Continuous Random Variables
- [ ] 5.1 Probability density functions
- [ ] 5.2 Uniform
- [ ] 5.3 Universality of the Uniform
- [ ] 5.4 Normal
- [ ] 5.5 Exponential
- [ ] 5.6 Poisson processes
- [ ] 5.7 Symmetry of i.i.d. continuous r.v.s
- [ ] 5.8 Recap
- [ ] 5.9 R
- [ ] 5.10 Exercises

### Chapter 6 — Moments
- [ ] 6.1 Summaries of a distribution
- [ ] 6.2 Interpreting moments
- [ ] 6.3 Sample moments
- [ ] 6.4 Moment generating functions
- [ ] 6.5 Generating moments with MGFs
- [ ] 6.6 Sums of independent r.v.s via MGFs
- [ ] 6.7 \*Probability generating functions
- [ ] 6.8 Recap
- [ ] 6.9 R
- [ ] 6.10 Exercises

### Chapter 7 — Joint Distributions
- [ ] 7.1 Joint, marginal, and conditional
- [ ] 7.2 2D LOTUS
- [ ] 7.3 Covariance and correlation
- [ ] 7.4 Multinomial
- [ ] 7.5 Multivariate Normal
- [ ] 7.6 Recap
- [ ] 7.7 R
- [ ] 7.8 Exercises

### Chapter 8 — Transformations
- [ ] 8.1 Change of variables
- [ ] 8.2 Convolutions
- [ ] 8.3 Beta
- [ ] 8.4 Gamma
- [ ] 8.5 Beta-Gamma connections
- [ ] 8.6 Order statistics
- [ ] 8.7 Recap
- [ ] 8.8 R
- [ ] 8.9 Exercises

### Chapter 9 — Conditional Expectation
- [ ] 9.1 Conditional expectation given an event
- [ ] 9.2 Conditional expectation given an r.v.
- [ ] 9.3 Properties of conditional expectation
- [ ] 9.4 \*Geometric interpretation of conditional expectation
- [ ] 9.5 Conditional variance
- [ ] 9.6 Adam and Eve examples
- [ ] 9.7 Recap
- [ ] 9.8 R
- [ ] 9.9 Exercises

### Chapter 10 — Inequalities and Limit Theorems
- [ ] 10.1 Inequalities
- [ ] 10.2 Law of large numbers
- [ ] 10.3 Central limit theorem
- [ ] 10.4 Chi-Square and Student-t
- [ ] 10.5 Recap
- [ ] 10.6 R
- [ ] 10.7 Exercises

### Chapter 11 — Markov Chains
- [ ] 11.1 Markov property and transition matrix
- [ ] 11.2 Classification of states
- [ ] 11.3 Stationary distribution
- [ ] 11.4 Reversibility
- [ ] 11.5 Recap
- [ ] 11.6 R
- [ ] 11.7 Exercises

### Chapter 12 — Markov Chain Monte Carlo
- [ ] 12.1 Metropolis-Hastings
- [ ] 12.2 Gibbs sampling
- [ ] 12.3 Recap
- [ ] 12.4 R
- [ ] 12.5 Exercises

### Chapter 13 — Poisson Processes
- [ ] 13.1 Poisson processes in one dimension
- [ ] 13.2 Conditioning, superposition, and thinning
- [ ] 13.3 Poisson processes in multiple dimensions
- [ ] 13.4 Recap
- [ ] 13.5 R
- [ ] 13.6 Exercises
