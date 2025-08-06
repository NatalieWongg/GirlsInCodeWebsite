# Read input
a, b, x, y = map(int, input().split())

# Option 1: Travel directly from a to b
direct_distance = abs(a - b)

# Option 2: Travel from a to x, teleport to y, travel to b
via_teleport_1 = abs(a - x) + abs(b - y)

# Option 3: Travel from a to y, teleport to x, travel to b
via_teleport_2 = abs(a - y) + abs(b - x)

# Output the minimum distance
print(min(direct_distance, via_teleport_1, via_teleport_2))
