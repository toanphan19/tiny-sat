import copy
import random

from enum import Enum

from base.instance import Instance
from base.propagator import Propagator
from base.helper import lit_to_var, var_to_lit


class DPLLSolver:
    """A SAT solver using DPLL algorithm. 

    Parameters: \\
    `var_choice`: {"input_order", "most_appearance"}, optional.
        Default is "input_order".
    `solve_all`: boolean, optional. Default is False, which means the solver \
        will terminate after having found the first solution.
    """

    def __init__(self, var_choice="input_order", solve_all=False):        
        # TODO: Implement the algorithm to solve all possible assignment.

        self.instance = None
        self.assignment = [] # assignment[v]: {True, False, None}
        self.propagator = None
        self.unassigned_vars = []
        self.satisfy_assignment = [] # list of satisfying assignment found.

        self.var_choice = var_choice

    def solve(self, instance):
        self.instance = instance
        self.assignment = [None for _ in range(instance.var_count)]
        self.propagator = Propagator(instance)
        self.unassigned_vars = self.setup_branch_order(instance)
        
        # print(f"\nBranch order: {[x+1 for x in self.unassigned_vars]}")

        self.dpll(0)
        return len(self.get_assignments()) > 0

    def dpll(self, level):
        """
        `level`: the current decision level. Used for backtracking.
        """
        if level == self.instance.var_count:
            self.save_assignment()
            # print(f"Successful assignment:\n {self.assignment}")

            return True
        
        # Pick a variable & try assigning value to it:
        variable = self.pick_branching_var()
        values = self.pick_assignment_order()

        self.assign(variable, values[0])
        if self.propagator.propagate(var_to_lit(variable, values[0]), self.assignment):
            if self.dpll(level + 1):
                return True
        
        self.assign(variable, values[1])
        if self.propagator.propagate(var_to_lit(variable, values[1]), self.assignment):
            if self.dpll(level + 1):
                return True
                
        # Roll back to backtrack:
        self.unassign(variable)
        return False


    def setup_branch_order(self, instance):
        if self.var_choice == "most_appearance":
            all_literals = [l for clause in instance.clauses for l in clause]

            # Sort variables according to their decreasing number of appearances
            order = copy.copy(instance.variables)
            order.sort(key=lambda v: all_literals.count(var_to_lit(v, True))
                                   + all_literals.count(var_to_lit(v, False)),
                reverse=True                                
            )
        else:
            order = copy.copy(instance.variables)

        return order

    def pick_branching_var(self):
        """ Choose the unassigned variable according to self.var_choice"""
        var = self.unassigned_vars[0]
        return var

    def pick_assignment_order(self):
        """ Randomly choose the order of value to make an assignment """
        if random.random() >= 0.5:
            return (True, False)
        return (False, True)

    def assign(self, variable, value):
        self.assignment[variable] = value
        if variable in self.unassigned_vars:
            self.unassigned_vars.remove(variable)

    def unassign(self, variable):
        self.assignment[variable] = None
        self.unassigned_vars.append(variable)        

    def save_assignment(self):
        self.satisfy_assignment.append(copy.copy(self.assignment))

    def get_assignments(self):
        """ Return the list of satisfying assignments.
        """
        return self.satisfy_assignment
