def longest_zero_path(grid):
    rows = len(grid)
    cols = len(grid[0])
    max_length = 0

    # Check horizontal sequences
    for row in grid:
        count = 0
        for val in row:
            if val == 0:
                count += 1
                max_length = max(max_length, count)
            else:
                count = 0

    # Check vertical sequences
    for col in range(cols):
        count = 0
        for row in range(rows):
            if grid[row][col] == 0:
                count += 1
                max_length = max(max_length, count)
            else:
                count = 0

    return max_length

# Example usage
dungeon = [[1, 0, 0, 1],
           [0, 1, 1, 0],
           [0, 0, 0, 1],
           [1, 0, 1, 0]]

print("Output:", longest_zero_path(dungeon))
