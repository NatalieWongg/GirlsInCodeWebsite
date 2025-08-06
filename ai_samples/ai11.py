def minimum_adjustment_cost(n, values):
    # Step 1: Sort the values
    values.sort()
    
    # Step 2: Find the median
    median = values[n // 2]  # This works for both odd and even n (can use lower median for even)
    
    # Step 3: Calculate total adjustment cost
    total_cost = sum(abs(x - median) for x in values)
    
    return total_cost

# Example usage
n = 6
values = [55000, 60000, 62000, 75000, 80000, 50000]

print(minimum_adjustment_cost(n, values))  # Output: 52000
