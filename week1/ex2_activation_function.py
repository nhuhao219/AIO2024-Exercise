# activation functions
import math

def activation_functions(x, function_name):
    if function_name == "sigmoid":
        sigmoid = 1 / (1 + math.exp(-x))
        return f"sigmoid: f({x}) = {sigmoid}"

    elif function_name == "relu":
        if x<=0:
            return f"relu: f({x}) = {0}"
        else:
            return f"relu: f({x}) = {x}"

    elif function_name == "elu":
        if x<=0:
            alpha = 0.001
            elu = alpha * (math.exp(x) - 1)
            return f"elu: f({x}) = {elu}"
        else:
            return f"elu: f({x}) = {x}"

    else:
        return f"{function_name} is not supported"

def is_number(x):
    return isinstance(x, (int, float))
    
if __name__ == "__main__":
    x = -5
    function_name = "elu"

    if is_number(x):
        result = activation_functions(x, function_name)
        print(result)
    else:
        raise ValueError("x must be a number")
