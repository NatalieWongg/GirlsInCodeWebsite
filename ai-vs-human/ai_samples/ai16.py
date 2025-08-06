def min_flips(n, a, b):
    flips = 0
    i = 0
    while i < n:
        if a[i] != b[i]:
            # Start of a new flip block
            flips += 1
            while i < n and a[i] != b[i]:
                i += 1
        else:
            i += 1
    return flips

# Example input
n = 7
a = "GHHHGHH"
b = "GGHHHGG"

print(min_flips(n, a, b))  # Output: 2
