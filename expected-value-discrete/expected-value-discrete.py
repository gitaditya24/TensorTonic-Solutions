import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    res = 0
    if sum(p) != 1:
        raise ValueError("invalid values")
    else:
        for i in range(len(x)):
            res += x[i]*p[i]
    return res
