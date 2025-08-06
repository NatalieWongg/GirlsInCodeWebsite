from itertools import permutations

# Read input
s = input().strip()

# Generate all permutations and remove duplicates using a set
unique_perms = set(permutations(s))

# Convert each tuple back to string and sort
sorted_perms = sorted(''.join(p) for p in unique_perms)

# Print the result
print(len(sorted_perms))
for p in sorted_perms:
    print(p)
