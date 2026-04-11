import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
    def sigma(y):
        return 1 / (1 + np.exp(-y))
    
    x = np.asarray(x, dtype=float)

    if x.ndim == 1:
        result = []
        for val in x:
            result.append(val * sigma(val))
        return result
    
    elif x.ndim == 2:
        result = []
        for row in x:
            new_row = []
            for val in row:
                new_row.append(val * sigma(val))
            result.append(new_row)
        return result