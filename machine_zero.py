import numpy as np

def machine_zero(dtype):
    Zero = dtype(1.0)

    while (dtype(2.0) * Zero) > Zero:
        Zero /= dtype(2.0)

    return Zero

machine_zero_f16 = machine_zero(np.float16)
machine_zero_f64= machine_zero(np.float64)

print(f"Float16: {machine_zero_f16}")
print(f"Float64: {machine_zero_f64}")
