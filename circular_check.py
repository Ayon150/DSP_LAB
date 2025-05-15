import numpy as np

# Circular correlation function with correct wrapping
def circular_correlation(x, y):
    N = len(x)  # Assuming equal length signals
    result = np.zeros(N)  # Output array
    
    for m in range(N):  # Iterate through shifts
        sum_value = 0
        for n in range(N):  # Compute sum for each shift
            wrapped_index = (n - m) % N  # Ensure circular behavior
            sum_value += x[n] * y[wrapped_index]  # Multiply & accumulate
        result[m] = sum_value
    
    return result

# Example signals
x = np.array([1, 3, -2, 4])
y = np.array([2, 3, -1, 3])

# Compute corrected circular correlation
r_xy_circ = circular_correlation(x, y)

print("Circular Correlation:", r_xy_circ)