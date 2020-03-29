package tinysat.base;

import java.lang.reflect.Array;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

public class Propagator {
    private List<Deque<Integer>> watchlist;
    private Instance instance;

    public Propagator(Instance instance) {
        this.instance = instance;
        initialiseWatchlist(instance);
    }

    private void initialiseWatchlist(Instance instance) {
        // Initialize watchlist by letting each clause watch its first literal:
        List<List<Integer>> clauses = instance.getClauses();
        // this.watchlist[i] is the list of clauses watching literal i:
        this.watchlist = new ArrayList<>();
        for (int i = 0; i < instance.getVarCount() * 2; ++i) {
            this.watchlist.add(new ArrayDeque<Integer>());
        }
        for (int c = 0; c < clauses.size(); ++c) {
            this.watchlist.get(clauses.get(c).get(0)).add(c);
        }
    }

    public boolean propagate(int falseLiteral, List<Variable> assignment) {
        /*
        At least a literal in a clause must be true to satisfy a clause.
        When a literal is assigned false, we make all the clauses watching that
        literal to watch another literal.
        If all other literal are false => clause unsatisfied

        Return: False if cannot update watchlist, which means the formula is
        unsatisfiable; True otherwise.
        */

        Deque<Integer> wachingClauses = watchlist.get(falseLiteral);
        while (!wachingClauses.isEmpty()) {
            Integer c = wachingClauses.getFirst();
            List<Integer> clause = instance.getClause(c);

            boolean foundAlternative = false;
            for (Integer lit : clause) {
                if (lit == falseLiteral)
                    continue;

                Variable correspondVar = Variable.litToVar(lit);
                Variable var = assignment.get(correspondVar.getId());
                // A clause either watch an unassigned literal or a true literal
                if (!var.assigned() || (var.getValue() == correspondVar.getValue())) {
                    foundAlternative = true;
                    makeWatch(c, lit);
                    stopWatch(c, falseLiteral);
                }
            }
            if (!foundAlternative) {
                return false;
            }
        }

        return true;
    }

    private void makeWatch(int clause, int lit) {
        // Make a clause watch a literal
        this.watchlist.get(lit).add(clause);
    }

    private void stopWatch(int clause, int lit) {
        this.watchlist.get(lit).remove(clause);
    }
}
