t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    total = sum(arr)
    odds = [x for x in arr if x % 2 == 1]
    
    if len(odds) == 0:
        print(0)
    elif len(odds) % 2 == 1:
        print(total)
    else:
        print(total - min(odds))
