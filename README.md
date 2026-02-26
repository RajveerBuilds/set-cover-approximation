# Set Cover: Greedy Approximation vs Bounded Exact Search (NP-hard)

This project explores the Set Cover problem, a classic NP-hard optimization problem, by comparing a fast greedy approximation algorithm with a bounded exact search on small instances.

## What this shows
- Why Set Cover is NP-hard and why exact solutions become infeasible as input size grows.
- How greedy approximation scales efficiently but may sacrifice optimality.
- The trade-off between runtime and solution quality in practice.

## Problem statement
Given a universe of elements and a collection of subsets, the goal is to select the smallest number of subsets whose union covers the entire universe.

## Approach
Two solvers are implemented:

- Greedy approximation: Iteratively selects the subset that covers the maximum number of currently uncovered elements. Fast and scalable, but not always optimal.
- Bounded exact search: Explores combinations of subsets to find an optimal solution for small instances, with a hard cap on the number of combinations checked to avoid exponential blow-ups.

## Experiments
Random Set Cover instances are generated for increasing problem sizes.  
For small instances, both greedy and bounded exact solutions are evaluated.  
For larger instances, only the greedy algorithm is run due to the exponential cost of exact search.

The experiments produce two plots:
- `solution_quality.png` compares the number of sets selected by greedy vs optimal (when available).
- `runtime_comparison.png` compares how runtime grows with problem size for both methods.

## Observations
As the problem size increases, the bounded exact search quickly becomes impractically slow due to exponential growth in the number of combinations explored, while the greedy algorithm continues to run efficiently. In small instances, greedy often matches the optimal solution, but as instances grow, greedy may select more sets than the optimal solution. This highlights the practical trade-off between optimality and computational efficiency in NP-hard optimization problems.

## Why this project
This project was built to demonstrate how approximation algorithms are used to handle NP-hard problems in real-world settings where exact solutions are computationally infeasible. By empirically comparing greedy approximation with bounded exact search, the project highlights the importance of algorithmic trade-offs between solution quality and scalability, a core idea in optimization, theoretical computer science, and performance-critical systems.

## How to run
```bash
pip install -r requirements.txt
python main.py --max_n 12