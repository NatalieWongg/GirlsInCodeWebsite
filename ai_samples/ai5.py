import sys
input = sys.stdin.read

def main():
    data = input().split()
    idx = 0

    N = int(data[idx])
    idx += 1
    U = int(data[idx])
    idx += 1

    grid = []
    for _ in range(N):
        grid.append(list(data[idx]))
        idx += 1

    updates = []
    for _ in range(U):
        r = int(data[idx]) - 1
        idx += 1
        c = int(data[idx]) - 1
        idx += 1
        updates.append((r, c))

    half = N // 2
    group_map = {}  # maps each cell to its group leader (TR corner)
    group_cells = {}  # maps each TR corner to its 4 symmetric positions
    group_values = {}  # stores current values of each group
    group_cost = {}  # stores current cost for each group

    def get_group(i, j):
        # return group key for a cell (always the TR corner)
        r = i if i < half else N - i - 1
        c = j if j >= half else N - j - 1
        return (r, c)

    def get_group_positions(r, c):
        # returns the 4 symmetric positions for TR cell (r, c)
        return [
            (r, c),
            (r, N - c - 1),
            (N - r - 1, c),
            (N - r - 1, N - c - 1)
        ]

    def compute_cost(values):
        count = values.count('#')
        return min(count, 4 - count)

    # Step 1: Build group data
    for i in range(half):
        for j in range(half, N):
            key = (i, j)
            positions = get_group_positions(i, j)
            group_cells[key] = positions
            group_values[key] = [grid[r][c] for r, c in positions]
            group_cost[key] = compute_cost(group_values[key])
            for r, c in positions:
                group_map[(r, c)] = key

    # Step 2: Compute initial total cost
    total_cost = sum(group_cost.values())
    print(total_cost)

    # Step 3: Process updates
    for r, c in updates:
        key = group_map[(r, c)]
        values = group_values[key]
        positions = group_cells[key]

        # Remove old cost
        total_cost -= group_cost[key]

        # Update the correct value in the group
        for i in range(4):
            if positions[i] == (r, c):
                values[i] = '#' if values[i] == '.' else '.'
                break

        # Recalculate cost
        new_cost = compute_cost(values)
        group_cost[key] = new_cost
        total_cost += new_cost
        print(total_cost)

main()
