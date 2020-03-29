package tinysat.base;


public class SolverOption {
    public enum VarChoice {
        INPUT_ORDER,
        MOST_APPEARANCE
    }

    private VarChoice varChoice;
    private boolean solveAll;

    public SolverOption() {
        this(VarChoice.INPUT_ORDER, false);
    }
    public SolverOption(VarChoice varChoice) {
        this(varChoice, false);
    }
    public SolverOption(VarChoice varChoice, boolean solveAll) {
        this.varChoice = varChoice;
        this.solveAll = solveAll;
    }

    public VarChoice getVarChoice() {
        return varChoice;
    }

    public boolean getSolveAll() {
        return solveAll;
    }
}
