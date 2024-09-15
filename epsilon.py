import numpy as np

def fepsilon():
    D = np.float16(1.0)

    while (np.float16(1.0) + D) > np.float16(1.0):
        D /= np.float16(2.0)

    return D * np.float16(2.0)

epsilon = fepsilon()
print(f"Output: {epsilon}")
