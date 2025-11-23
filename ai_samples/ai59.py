t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    nonzero = [x for x in p if x != 0]
    
    if not nonzero:
        print(n)
        continue
    
    mn = min(nonzero)
    mx = max(nonzero)
    
    if len(nonzero) == n:
        # no zeros → check if already sorted
        sorted_p = sorted(p)
        l = 0
        while l < n and p[l] == sorted_p[l]:
            l += 1
        r = n - 1
        while r >= 0 and p[r] == sorted_p[r]:
            r -= 1
        print(0 if l > r else r - l + 1)
    else:
        print(min(n, mx - mn))
