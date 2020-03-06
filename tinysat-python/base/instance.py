class Instance:
    def __init__(self, variables, clauses):
        """
        self.variables: [1, 2, 3, 4]
        self.clauses: [(0, 2, 5), (3, 4, 5)]
        """
        self.var_count = len(variables)
        self.clause_count = len(clauses)
        self.variables = variables
        self.clauses = clauses

    def __str__(self):
        text = f"Variables: {self.var_count}\n{self.variables}\n"
        text += f"Clauses: {self.clause_count}\n{self.clauses}\n"
        return text
    