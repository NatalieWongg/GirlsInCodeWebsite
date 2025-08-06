def modified_fibonacci(n):
    f = [0] * (n + 1)
    f[0] = 7
    f[1] = 9

    for i in range(2, n + 1):
        f[i] = 3 * f[i - 1] + 2 * f[i - 2]

    return f

# Generate and print the sequence up to n = 15
sequence = modified_fibonacci(15)
for i, val in enumerate(sequence):
    print(f"f({i}) = {val}")
