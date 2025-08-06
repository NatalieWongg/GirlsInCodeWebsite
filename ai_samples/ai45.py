def solve_whack_a_mole():
    # Read input
    n = int(input())
    grid = []
    for i in range(n):
        row = input().strip()
        grid.append([int(c) for c in row])
    
    # Count moles in each row
    row_counts = []
    for i in range(n):
        count = sum(grid[i])
        row_counts.append(count)
    
    # Count moles in each column
    col_counts = []
    for j in range(n):
        count = sum(grid[i][j] for i in range(n))
        col_counts.append(count)
    
    # Find the target count (should be the maximum count since one row/col is missing a mole)
    target_row_count = max(row_counts)
    target_col_count = max(col_counts)
    
    # Find which row and column need an additional mole
    missing_row = -1
    missing_col = -1
    
    for i in range(n):
        if row_counts[i] == target_row_count - 1:
            missing_row = i + 1  # Convert to 1-indexed
            break
    
    for j in range(n):
        if col_counts[j] == target_col_count - 1:
            missing_col = j + 1  # Convert to 1-indexed
            break
    
    print(missing_row, missing_col)

# Test with the example
def test_example():
    # Simulate the example input
    test_input = """5
10110
11010
10011
01101
01001"""
    
    lines = test_input.strip().split('\n')
    n = int(lines[0])
    grid = []
    for i in range(1, n + 1):
        row = lines[i]
        grid.append([int(c) for c in row])
    
    # Count moles in each row
    row_counts = []
    for i in range(n):
        count = sum(grid[i])
        row_counts.append(count)
        print(f"Row {i+1}: {count} moles")
    
    # Count moles in each column
    col_counts = []
    for j in range(n):
        count = sum(grid[i][j] for i in range(n))
        col_counts.append(count)
        print(f"Col {j+1}: {count} moles")
    
    # Find missing row and column
    target_count = max(row_counts)
    missing_row = row_counts.index(target_count - 1) + 1
    missing_col = col_counts.index(target_count - 1) + 1
    
    print(f"\nAnswer: {missing_row} {missing_col}")

# Run the test
print("Testing with example:")
test_example()

print("\n" + "="*50)
print("To solve a new problem, run solve_whack_a_mole()")
print("="*50)