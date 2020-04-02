# TinySAT
A basic SAT solver using [DPLL](https://en.wikipedia.org/wiki/DPLL_algorithm) algorithm, available in both Python and Java. A follow-up implementation is soon to be with the superior [Conflict-Driven Clause Learning](https://en.wikipedia.org/wiki/Conflict-driven_clause_learning) algorithm.

## Introduction
### What is a SAT Solver?
A SAT solver is a mathematical solver created to find solutions for Boolean Satisfiability Problems, which is NP-complete. More info can be found on the [wikipedia's page](https://en.wikipedia.org/wiki/Boolean_satisfiability_problem).


## Usage
### Input format
The input format is DIMACS CNF, which is standard for SAT solvers. A brief description can be found [here](https://logic.pdmi.ras.ru/~basolver/dimacs.html).

### Example usage
```
python tinysat.py ../examples/simple.dimacs
```
