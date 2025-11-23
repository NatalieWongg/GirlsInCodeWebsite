nk = list(map(int, input().split()))
n = nk[0]
k = nk[1]
arr = []
odd = -1
even = 0

for i in range(int(n/2)):
    odd += 2
    arr.append(odd)

for i in range(int(n/2)):
    even += 2
    arr.append(even)

print(arr[k-1])

