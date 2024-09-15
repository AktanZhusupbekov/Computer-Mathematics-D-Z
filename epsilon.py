import numpy as np

def fepsilon():
    D = np.float16(1.0)

    while (np.float16(1.0) + D) > np.float16(1.0):
        D /= np.float16(2.0)

    return delta * np.float16(2.0)

epsilon = f_epsilon()
print(f"Output: {epsilon}")
