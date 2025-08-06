def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Example usage
n = 5432
print("Output:", sum_of_digits(n))
