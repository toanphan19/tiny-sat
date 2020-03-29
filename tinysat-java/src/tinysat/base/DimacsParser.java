package tinysat.base;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

public class DimacsParser {
    public static Instance parseProgram(String program) {
        List<String> lines = Arrays.asList(program.split("\n"));

        // Find the first line with the format: p <varCount> <clauseCount>
        String current = "";
        Iterator<String> iter = lines.iterator();
        while (!current.startsWith("p") && lines.iterator().hasNext()) {
            current = iter.next();
        }
        // TODO: Throw error if !current.startsWith("p")

        String[] tokens = current.split("\\s+");
        int varCount = Integer.parseInt(tokens[2]);
        int clauseCount = Integer.parseInt(tokens[3]);
        List<List<Integer>> clauses = new ArrayList<>();

        while (iter.hasNext() && clauseCount > 0) {
            --clauseCount;
            current = iter.next();
            // TODO: Throw error if the line doesn't end with '0'

            tokens = current.split("\\s+");
            List<Integer> clause = new ArrayList<>();
            for (int i = 0; i < tokens.length - 1; ++i) {
                clause.add(encodeLiteral(Integer.parseInt(tokens[i])));
            }
            clauses.add(clause);
        }

        Instance ins = new Instance(varCount, clauses);
        return ins;
    }

    public static int[] decodeAssignments(List<Variable> assignment) {
        int[] result = new int[assignment.size()];
        for (int i = 0; i < assignment.size(); ++i) {
            result[i] = decodeVariable(assignment.get(i));
        }
        return result;
    }

    private static int encodeLiteral(int x) {
        if (x > 0) {
            return (x - 1) * 2;
        }
        return (-x - 1) * 2 + 1;
    }

    private static int decodeVariable(Variable var) {
        int x = var.getId();
        if (!var.getValue())
            x = -x;
        return x;
    }
}
