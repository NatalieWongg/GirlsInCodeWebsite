def compute_Tn(n):
    if n % 2 == 1:  # n is odd
        result = (n + 3) / 2 + n**2
    else:  # n is even
        result = (n + 4) / 2 + 0.25 * n**2

    return int(result)  # Convert to integer (removes .0)

# Example usage
n = 1
print("Output:", compute_Tn(n))
