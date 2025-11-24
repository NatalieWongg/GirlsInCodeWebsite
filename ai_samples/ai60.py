def solve():
    import sys
    input = sys.stdin.readline
    
    t = int(input())
    
    # Precompute possible deals
    w, c = [], []
    x = 0
    while True:
        val = 3 ** x
        if val > 1e9:
            break
        w.append(val)
        cost = 3 ** (x + 1) + x * (3 ** (x - 1)) if x > 0 else 3
        c.append(cost)
        x += 1
    
    for _ in range(t):
        n = int(input())
        ans = 0
        for i in range(len(w) - 1, -1, -1):
            if n >= w[i]:
                k = n // w[i]
                ans += k * c[i]
                n -= k * w[i]
        print(ans)
