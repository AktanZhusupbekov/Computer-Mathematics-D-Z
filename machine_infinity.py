import numpy as np

def machineinfi(dtype):
    Inf = dtype(1.0)
    factor = dtype(2.0)

    while True:
        nextI = Inf * factor
        if nextI == Inf:
            break
        Inf = nextI

    return Inf

machineinf_fl16 = machineinfi(np.float16)
machineinf_fl64 = machineinfi(np.float64)

print(f"Float16: {machineinf_fl16}")
print(f"Float64: {machineinf_fl64}")
