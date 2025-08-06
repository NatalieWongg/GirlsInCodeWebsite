import itertools

S = input("Enter initials: ")
perms = sorted(set(itertools.permutations(S))) 
for p in perms:  
    print("".join(p))