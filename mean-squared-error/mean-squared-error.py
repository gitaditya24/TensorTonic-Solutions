import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    y_p = np.array(y_pred , dtype = float)
    y_t = np.array(y_true , dtype = float)
    n = len(y_p)
    sum = 0.0
    for i in range(0,n):
        sum += (y_p[i] - y_t[i])**2

    return sum/n
