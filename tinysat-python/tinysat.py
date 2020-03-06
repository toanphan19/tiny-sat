import sys
import time

from enum import Enum

import base.parser as parser
from base.instance import Instance
from solvers.dpll_solver import DPLLSolver


class Satisfiability(Enum):
    SAT = 'SAT'
    UNSAT = 'UNSAT'
    UNKNOWN = 'UNKNOWN'

def run_solver(program):
    # program = input_file.read()
    instance = parser.parse_program(program)
    solver = DPLLSolver()
    is_sat = solver.solve(instance)

    if is_sat:
        assignment = solver.get_assignment()
        result = parser.decode_assignment(assignment)
        return Satisfiability.SAT, result
    else:
        return Satisfiability.UNSAT, None


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("There are not enough arguments!")
        print("Expected: ./tinysat.py <input file> <output file>")
        sys.exit()

    with open(sys.argv[1], 'r') as f:
        program = f.read()

    start_time = time.time()
    result, assignment = run_solver(program)
    elapsed_time = time.time() - start_time

    with open(sys.argv[2], 'w') as f:
        f.write(result.name + "\n")
        if result == Satisfiability.SAT:
            f.write(assignment)

    print()
    if result == Satisfiability.UNSAT:
        print("UNSAT")
    else:
        print("SAT")
        print(assignment)
    
    print(f"Time elapse: {elapsed_time * 1000 :.4f}ms")
    