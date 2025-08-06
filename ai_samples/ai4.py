import sys
from collections import defaultdict

def main():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    a = list(map(int, data[1:]))

    pos = defaultdict(list)
    for idx, val in enumerate(a):
        pos[val].append(idx)

    seen_prefix = set()
    prefix_count = defaultdict(int)
    result = set()

    for i in range(n):
        current = a[i]

        # If this value has appeared before, count how many values ≠ current have appeared before
        if prefix_count[current] >= 1:
            for x in seen_prefix:
                if x != current:
                    result.add((x, current, current))

        # Update prefix seen info
        prefix_count[current] += 1
        seen_prefix.add(current)

    print(len(result))

main()
