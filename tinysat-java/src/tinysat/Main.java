package tinysat;

import tinysat.base.DimacsParser;
import tinysat.base.Instance;
import tinysat.base.Variable;
import tinysat.solvers.DPLLSolver;
import tinysat.solvers.Solver;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
//        String filename = "../benchmark/aim/aim-50-1_6-yes1-1.cnf";
        String filename = "../examples/simple2.dimacs";

        String program;
        try {
            program = new String(Files.readAllBytes(Paths.get(filename)));
        } catch (IOException e) {
            e.printStackTrace();
            return;
        }

        Instance ins = DimacsParser.parseProgram(program);

        Solver solver = new DPLLSolver();
        solver.solve(ins);

        List<List<Variable>> assignments = solver.getAssignments();

        if (assignments.size() == 0) {
            System.out.println("UNSATISFIABLE");
        } else {
            System.out.println("SATISFIABLE");
            for (List<Variable> assignment : assignments) {
                int[] result = DimacsParser.decodeAssignments(assignment);
                System.out.println(Arrays.toString(result));
            }

        }
    }
}
