package tinysat.solvers;

import tinysat.base.Instance;
import tinysat.base.Propagator;
import tinysat.base.SolverOption;
import tinysat.base.Variable;

import java.util.*;

public class DPLLSolver implements Solver {
    private Instance instance;
    private SolverOption option;
    private List<Variable> assignment;
    private List<List<Variable>> satisfyAssignments;
    private Propagator propagator;

    public DPLLSolver() {
        this(new SolverOption());
    }

    public DPLLSolver(SolverOption option)  {
        this.option = option;
    }

    @Override
    public void solve(Instance instance) {
        this.instance = instance;
        this.assignment = setupBranchOrder(instance);
        this.propagator = new Propagator(instance);
        this.satisfyAssignments = new ArrayList<>();

        dpll(0);
    }

    // Recursive version of dpll
    private boolean dpll(int depth) {
        if (depth == instance.getVarCount()) {
            saveAssignment();
            return true;
        }

        // Pick a variable and try assigning value to it:
        Variable var = assignment.get(depth);
        boolean values[] = pickAssignmentOrder();

        var.assign(values[0]);
        if (propagator.propagate(var.toLit(), this.assignment)) {
            if (dpll(depth + 1)) {
                return true;
            }
        }

        var.assign(values[1]);
        if (propagator.propagate(var.toLit(), this.assignment)) {
            if (dpll(depth + 1)) {
                return true;
            }
        }

        // Could not find solution -> roll back to backtrack:
        var.unassign();
        return false;
    }

    // Iterative version of dpll
    private boolean dpll() {
        int depth = 0;

        // State = -1 means nothing is tried,
        // 0 means False has been tried but True has not,
        // 2 means both value has been tried.
        int[] state = new int[instance.getVarCount()];
        Arrays.fill(state, -1);

        while (true) {
            if (depth == instance.getVarCount()) {
                saveAssignment();
                return true;
            }

            boolean triedSomething = true;
            // Pick a variable and try assigning value to it:
            Variable var = assignment.get(depth);
            switch (state[depth]) {
                case -1:
                    boolean[] values = pickAssignmentOrder();
                    var.assign(values[0]);
                    state[depth] = values[0] ? 1 : 0;
                    break;
                case 0:
                    var.assign(true);
                    state[depth] = 2;
                    break;
                case 1:
                    var.assign(false);
                    state[depth] = 2;
                    break;
                case 2:
                    // Backtrack
                    triedSomething = false;
                    break;
            }
            if (triedSomething) {
                if (propagator.propagate(var.toLit(), this.assignment)) {
                    ++depth;
                } else {
                    var.unassign();
                }
            } else {
                // Backtrack:
                if (depth > 0) {
                    var.unassign();
                    state[depth] = -1;
                    --depth;
                } else {
                    return false;
                }
            }
        }
    }

    private void saveAssignment() {
        List<Variable> assignment = new ArrayList<>();
        for (Variable v : this.assignment) {
            assignment.add(v.clone());
        }
        this.satisfyAssignments.add(assignment);
    }

    @Override
    public List<List<Variable>> getAssignments() {
        return this.satisfyAssignments;
    }

    private List<Variable> setupBranchOrder(Instance instance) {
        List<Variable> branchOrder = new ArrayList<>();
        for (int id = 1; id <= instance.getVarCount(); ++id) {
            branchOrder.add(new Variable(id));
        }

        if (this.option.getVarChoice() == SolverOption.VarChoice.INPUT_ORDER) {
            // Do nothing
        } else {
            // TODO: Change to MostAppearance using statistics
//            branchOrder.addAll(listVars);
        }

        return branchOrder;
    }

    private boolean[] pickAssignmentOrder() {
        Random rnd = new Random();
        boolean value = rnd.nextBoolean();
        return new boolean[] {value, !value};
//        return new boolean[] {true, false};
    }
}
