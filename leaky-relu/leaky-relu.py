import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Write code here
    x = np.asarray(x)
    output = []
    for val in x :
        if val >= 0:
            output.append(val)
        else :
            output.append(alpha*val)
    return np.asarray(output)