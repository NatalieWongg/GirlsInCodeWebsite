from typing import List, Tuple

def find_ideal_crypts(grid: List[List[int]]) -> List[Tuple[int, int]]:
    rows = len(grid)
    cols = len(grid[0])
    ideal_crypts = []

    for y in range(rows):
        for x in range(cols):
            current = grid[y][x]

            # Get left and right neighbors (west and east)
            west = grid[y][x - 1] if x > 0 else float('-inf')
            east = grid[y][x + 1] if x < cols - 1 else float('-inf')

            # Get top and bottom neighbors (north and south)
            north = grid[y - 1][x] if y > 0 else float('inf')
            south = grid[y + 1][x] if y < rows - 1 else float('inf')

            if current > west and current > east and current < north and current < south:
                ideal_crypts.append((y, x))

    return sorted(ideal_crypts)