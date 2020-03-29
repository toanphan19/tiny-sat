import sys
import time

from enum import Enum

import base.dimacs_parser as parser
from base.instance import Instance
from solvers.dpll_solver import DPLLSolver


class Satisfiability(Enum):
    SAT = 'SATISFIABLE'
    UNSAT = 'UNSATISFIABLE'
    # UNKNOWN = 'UNKNOWN'


def run_solver(program):
    instance = parser.parse_program(program)
    solver = DPLLSolver("input_order")
    is_sat = solver.solve(instance)

    if is_sat:
        assignments = solver.get_assignments()
        assignments = [parser.decode_assignment(a) for a in assignments]
        return Satisfiability.SAT, assignments
    else:
        return Satisfiability.UNSAT, None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("There are not enough arguments!")
        print("Expected: python tinysat.py <input file>")
        sys.exit()

    with open(sys.argv[1], 'r') as f:
        program = f.read()

    start_time = time.time()
    result, assignments = run_solver(program)
    elapsed_time = time.time() - start_time


    print()
    if result == Satisfiability.UNSAT:
        print("UNSAT")
    else:
        print("SAT")
        [print(a) for a in assignments]
    
    print(f"Time elapse: {elapsed_time * 1000 :.2f}ms")
    