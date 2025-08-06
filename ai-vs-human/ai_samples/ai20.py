def traffic_flow_ranges(n, segments):
    # Step 1: Work backward to find possible initial range
    low, high = 0, 1000  # full range

    for i in reversed(range(n)):
        kind, x, y = segments[i]
        if kind == "none":
            low = max(low, x)
            high = min(high, y)
        elif kind == "on":
            low = max(0, low - y)
            high = high - x
        elif kind == "off":
            low = low + x
            high = high + y
        high = max(high, 0)

    initial_low, initial_high = low, high

    # Step 2: Work forward to find possible final range
    low, high = initial_low, initial_high

    for i in range(n):
        kind, x, y = segments[i]
        if kind == "none":
            low = max(low, x)
            high = min(high, y)
        elif kind == "on":
            low = low + x
            high = high + y
        elif kind == "off":
            low = max(0, low - y)
            high = high - x
        high = max(high, 0)

    final_low, final_high = low, high

    return (initial_low, initial_high), (final_low, final_high)

# Sample Input
n = 4
input_lines = [
    "on 1 1",
    "none 10 14",
    "none 11 15",
    "off 2 3"
]

segments = []
for line in input_lines:
    parts = line.split()
    kind = parts[0]
    x, y = map(int, parts[1:])
    segments.append((kind, x, y))

# Run
initial_range, final_range = traffic_flow_ranges(n, segments)
print(f"{initial_range[0]} {initial_range[1]}")
print(f"{final_range[0]} {final_range[1]}")
