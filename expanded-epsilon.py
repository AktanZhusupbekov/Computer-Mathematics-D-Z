import numpy as np

def fepsilon(dtype):
    D = dtype(1.0)

    while (dtype(1.0) + D) > dtype(1.0):
        D /= dtype(2.0)

    return D * dtype(2.0)

epsilon_float64 = fepsilon(np.float64)

print(f"Output: {epsilon_float64}")
