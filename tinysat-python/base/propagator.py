from base.helper import lit_to_var, var_to_lit

class Propagator:
    def __init__(self, instance):
        self.instance = instance
        self.watchlist = self.setup_watchlist(instance)

    def setup_watchlist(self, instance):
        watchlist = [[] for x in range(2 * instance.var_count)]
        for idx, clause in enumerate(instance.clauses):
            watchlist[clause[0]].append(idx)

        return watchlist

    def propagate(self, false_literal, assignment):
        """
        At least a literal in a clause must be true to satisfy a clause.
        When a literal is assigned false, we make all the clauses watching that
        literal to watch another literal.
        If all other literal are false => clause unsatisfied

        Return: False if cannot update watchlist, which means the formula is
        unsatisfiable; True otherwise.
        """
        watchlist = self.watchlist
        while len(watchlist[false_literal]) > 0:
            clause_id = watchlist[false_literal][0]
            found_another = False
            for literal in self.instance.clauses[clause_id]:
                if literal == false_literal: 
                    continue
                variable, is_positive = lit_to_var(literal)

                if assignment[variable] is None \
                or assignment[variable] == is_positive:
                    found_another = True
                    watchlist[literal].append(clause_id)
                    watchlist[false_literal].remove(clause_id)
                    break

            if not found_another:
                return False

        return True