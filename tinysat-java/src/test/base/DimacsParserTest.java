package base;

import org.junit.jupiter.api.Test;
import tinysat.base.DimacsParser;
import tinysat.base.Instance;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;


class DimacsParserTest {

    @Test
    void parseProgram() {
        String program =
            "c  simple_v3_c2.cnf\n" +
            "c\n" +
            "p cnf 3 2\n" +
            "1 -3 0\n" +
            "2 3 -1 0";
        Instance ins = DimacsParser.parseProgram(program);

        assertEquals(ins.getVarCount(), 3);

        List<List<Integer>> clauses = ins.getClauses();
        assertEquals(clauses.get(0).size(), 2);
        assertEquals(clauses.get(1).size(), 3);
    }
}