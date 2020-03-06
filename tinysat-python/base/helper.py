def lit_to_var(literal):
    return (literal // 2, literal % 2 == 0)

def var_to_lit(variable, value):
    """
    variable: int
    value: boolean
    """
    return variable * 2 + int(value)