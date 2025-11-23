t = int(input())
for i in range(t):
    n = int(input())
    arr = []
    arr = list(map(int, input().split()))
    total = 0
    max = -1
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += arr[j]
            average = int(total / (j - i + 1))
            if average > max: 
                max = average
    print(max)
