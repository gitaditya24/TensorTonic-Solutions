

def elu(x, alpha):
    """ 
    Apply ELU activation to each element.
    """
    # Write code here
    output = []

    for val in x :
        if val > 0:
            output.append(val)
        else :
            res = alpha * (math.exp(val)-1)
            output.append(res)
    return output