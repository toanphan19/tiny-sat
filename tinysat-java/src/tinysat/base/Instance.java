package tinysat.base;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

public class Instance {
    private int varCount;

    private List<List<Integer>> clauses;

    public Instance(int varCount, List<List<Integer>> clauses) {
        this.varCount = varCount;
        this.clauses = clauses;
    }

    public int getVarCount() {
        return varCount;
    }

    public List<List<Integer>> getClauses() {
        return clauses;
    }

    public List<Integer> getClause(Integer i) {
        return clauses.get(i);
    }
}
