#!/usr/bin/python3
def minOperations(n):
    if n == 1:
        return 0

    # Initialize a list to store the minimum number of operations needed for each index
    min_ops = [0] * (n + 1)

    for i in range(2, n + 1):
        min_ops[i] = i  # Initialize with the maximum possible value

        for j in range(2, i):
            if i % j == 0:
                # If j is a divisor of i, we can copy the content from (i//j) and paste it j times
                min_ops[i] = min(min_ops[i], min_ops[i // j] + j)

    return min_ops[n]  # Return the minimum number of operations for n

# Example usage
n = 9
print(minOperations(n))

