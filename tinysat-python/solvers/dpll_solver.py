import copy
import random

from base.instance import Instance
from base.helper import lit_to_var, var_to_lit


class DPLLSolver:

    def __init__(self, solve_all=False):
        # TODO: Implement the algorithm to solve all possible assignment.

        self.instance = None
        self.assignment = [] # True, False, or None
        self.watchlist = []
        self.unassigned_vars = []

        self.satisfy_assignment = None

        self.node_travesed = 0


    def dpll(self, watchlist, level):
        """
        level: the level of the current node. Used for backtracking.
        """

        # self.node_travesed += 1
        # if self.node_travesed % 1000000 == 0:
        #     print(f"Node travesed: {self.node_travesed}")
        #     print("Current Assignment: ", self.assignment)


        if level == self.instance.var_count:
            self.remember_assignment()
            # print(f"Successful assignment:\n {self.assignment}")

            return True
        
        # Pick a variable:
        variable = self.get_unassigned_var()

        # Try assigning value to it:
        values = self.get_assignment_values()
        self.assign(variable, values[0])

        # new_watchlist = copy.deepcopy(watchlist)
        new_watchlist = watchlist
        if self.propagate(new_watchlist, var_to_lit(variable, values[0])):
            if self.dpll(new_watchlist, level + 1):
                return True
        
        self.assign(variable, values[1])
        # new_watchlist = copy.deepcopy(watchlist)
        new_watchlist = watchlist
        if self.propagate(new_watchlist, var_to_lit(variable, values[1])):
            if self.dpll(new_watchlist, level + 1):
                return True
                
        # Roll back to backtrack:
        self.unassign(variable)
        return False

    def solve(self, instance):
        self.instance = instance
        self.unassigned_vars = copy.copy(instance.variables)
        self.assignment = [None for _ in range(instance.var_count)]
        watchlist = self.setup_watchlist(instance)
        
        result = self.dpll(watchlist, 0)
        return result

    #
    # === Helper methods ====
    #

    def setup_watchlist(self, instance):
        watchlist = [[] for x in range(2 * instance.var_count)]
        for idx, clause in enumerate(instance.clauses):
            watchlist[clause[0]].append(idx)

        return watchlist

    def propagate(self, watchlist, false_literal):
        """
        At least a literal in a clause must be true to satisfy a clause.
        When a literal is assigned false, we make all the clauses watching that
        literal to watch another literal.
        If all other literal are false => clause unsatisfied

        Return: False if cannot update watchlist, which means the formula is
        unsatisfiable; True otherwise.
        """
        while len(watchlist[false_literal]) > 0:
            clause_id = watchlist[false_literal][0]
            found_another = False
            for literal in self.instance.clauses[clause_id]:
                if literal == false_literal: 
                    continue
                variable, is_positive = lit_to_var(literal)

                if self.assignment[variable] is None \
                or self.assignment[variable] == is_positive:
                    found_another = True
                    watchlist[literal].append(clause_id)
                    watchlist[false_literal].remove(clause_id)
                    break

            if not found_another:
                # print(f"Pruned {len(self.unassigned_vars)} levels. Backtracking...")
                return False

        return True

    def get_unassigned_var(self):
        """ Randomly choose an unassigned variable """
        var = random.choice(self.unassigned_vars)
        # Or just choose the 1st one:
        # var = self.unassigned_vars[0]
        return var

    def get_assignment_values(self):
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

    def remember_assignment(self):
        self.satisfy_assignment = copy.copy(self.assignment)

    def get_assignment(self):
        return self.satisfy_assignment
