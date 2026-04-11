import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
    def sigma(y):
        return 1/(1+np.exp(-y))
    x = np.asarray(x , dtype = float)
    result = []
    for val in x:
        result.append(val*sigma(val))
    return result
