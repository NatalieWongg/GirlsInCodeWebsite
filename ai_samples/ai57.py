t = int(input())
for _ in range(t):
    n = int(input())
    res = [0] * (2 * n)
    i = 0
    for x in range(1, n + 1):
        # find next empty spot
        while res[i] != 0:
            i += 1
        res[i] = x
        res[i + x] = x  # place second occurrence x distance away
    print(*res)
