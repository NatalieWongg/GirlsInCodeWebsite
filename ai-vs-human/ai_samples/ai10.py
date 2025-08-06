from itertools import permutations

def print_unique_permutations(s):
    # Use set to remove duplicates, then sort the result
    unique_perms = sorted(set([''.join(p) for p in permutations(s)]))
    # Print each permutation
    for perm in unique_perms:
        print(perm)

# Example usage
print_unique_permutations("ada")
