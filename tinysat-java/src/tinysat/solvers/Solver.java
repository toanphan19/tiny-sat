package tinysat.solvers;

import tinysat.base.Instance;
import tinysat.base.SolverOption;
import tinysat.base.Variable;

import java.util.List;

public interface Solver {
    public void solve(Instance instance);
    public List<List<Variable>> getAssignments();
}
