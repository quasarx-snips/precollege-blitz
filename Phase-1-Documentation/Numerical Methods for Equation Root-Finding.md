# Engineering Lab Report: Computational Root-Finding Algorithms

**Author:** Bibhab  
**Date:** June 2026  
**Course Reference:** Advanced Computational Logic / Phase-1 Documentation
**Language:** $\LaTeX$ 
---

## 1. Executive Summary
This document serves as a technical benchmark for implementing root-finding algorithms without relying on external mathematical libraries. In engineering and software design, locating the roots of a non-linear continuous function $f(x) = 0$ is foundational for predicting system stability parameters.

---

## 2. Mathematical Frameworks & LaTeX Implementations

### A. The Quadratic Baseline
For any standard second-order polynomial equation, the roots are calculated analytical via the classic quadratic formula.

The general form of the equation is:
$$ax^2 + bx + c = 0$$

The mathematical solution for the roots $x_1$ and $x_2$ is represented as:
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

Where the structural state of the system is governed by the Discriminant ($D$):
$$D = b^2 - 4ac$$

### B. The Newton-Raphson Iterative Method
For transcendental or higher-order non-linear equations where analytical solutions do not exist, we employ the Newton-Raphson iterative matrix framework. Given an initial guess $x_n$, the next approximation $x_{n+1}$ is structurally mapped as:

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

---

## 3. Algorithm State & Logic Matrix

The table below outlines how the system's runtime execution shifts based on the properties of the Discriminant ($D$) processed during execution:

| Discriminant Condition | Root Typology | Execution Pipeline Route | System Status |
| :--- | :---: | :--- | :---: |
| $D > 0$ | Real & Distinct | Split computation into two independent float streams |  Optimal |
| $D = 0$ | Real & Equal | Compute single execution path: $x = \frac{-b}{2a}$ |  Converged |
| $D < 0$ | Complex / Imaginary | Invoke complex number structure: $x = \alpha \pm i\beta$ |  Complex Mode |

---

## 4. Multi-Variable State Vector Matrix
In multi-dimensional spaces, the convergence criteria for tracking error fields across a structural coordinate plane can be modeled using the following boundary matrix:

$$
M = \begin{pmatrix}
x^2 & \frac{\partial f}{\partial x} & 0 \\
\frac{\partial f}{\partial y} & y^2 & 1 \\
0 & 1 & \epsilon
\end{pmatrix}
$$

