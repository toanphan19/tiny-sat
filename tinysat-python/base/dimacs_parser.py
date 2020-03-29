from base.instance import Instance

"""
Parse Input/Output in DIMACS format.
"""


def __encode_literal(x):
    return (x-1) * 2 if x > 0 else (-x - 1) * 2 + 1


def __parse_clause(line):
    """
    Converting a clause to an array of literals.
    """        
    literals = [int(x) for x in line.split()]
    if literals[-1] != 0:
        raise Exception("Parsing error: All clauses must end with 0.")
    
    literals = [__encode_literal(x) for x in literals[:-1]]
    return literals


def parse_program(program):
    """
    Parse a program (of type string) and return an Instance
    """
    # TODO: Check number of vars and clauses to see if they match

    lines = program.split("\n")

    # Ignore comments at the beginning of the file:
    start_i = 0
    while lines[start_i][0] != "p":
        start_i += 1
    lines = lines[start_i:]

    var_count, clause_count = lines[0].split()[2:4]
    var_count, clause_count = int(var_count), int(clause_count)

    variables = list(range(var_count))
    clauses = []
    for i in range(1, clause_count + 1):
        clauses.append(__parse_clause(lines[i]))

    return Instance(variables, clauses)


def decode_assignment(assignment):
    result = [i + 1 if assignment[i] else -(i + 1) for i in range(len(assignment))]
    return " ".join([str(x) for x in result])
