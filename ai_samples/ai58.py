t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    
    cnt0 = s.count('0')
    cnt1 = s.count('1')
    cnt2 = s.count('2')
    
    min_top = cnt0
    max_top = cnt0 + cnt2
    min_bottom = cnt1
    max_bottom = cnt1 + cnt2
    
    res = []
    for i in range(1, n + 1):
        if i <= min_top or i > n - min_bottom:
            res.append('-')
        elif i <= max_top or i > n - max_bottom:
            res.append('?')
        else:
            res.append('+')
    print(''.join(res))
