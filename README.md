# TinySAT
A basic SAT solver using [DPLL](https://en.wikipedia.org/wiki/DPLL_algorithm) algorithm, available in both Python and Java.

## Introduction
### What is a SAT Solver?
A SAT solver is a mathematical solver created to find solutions for Boolean Satisfiability Problems, which is NP-complete. More info can be found on the [wikipedia's page](https://en.wikipedia.org/wiki/Boolean_satisfiability_problem). Many difficult problems can be reduced to a SAT problem and thus can be solved with a SAT solver.

### What are SAT Solvers used for?
Any NP-hard problems can be formulated as SAT formular and be solved by SAT Solvers. 
Some areas where they have been performing well are:
- **Package management system**. Conda, a package manager for Python, explains in [this article](https://www.anaconda.com/understanding-and-improving-condas-performance/) that they have been using [picosat](http://fmv.jku.at/picosat/) in their implementation and is experimenting with other SAT solvers. [Fedora's DNF](https://fedoraproject.org/wiki/Features/DNF) is also solving the dependency resolution problem using SAT Solvers.

## Usage
### Input format
The input format is DIMACS CNF, which is standard for SAT solvers. A brief description can be found [here](https://logic.pdmi.ras.ru/~basolver/dimacs.html).

Example:
```
c A sample input file.
p cnf 3 2
1 -3 0
2 3 -1 0 
```

### Example usage
```
python tinysat.py ../examples/simple.dimacs
```
