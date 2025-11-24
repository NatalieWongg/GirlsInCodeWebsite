n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
twin1 = 0
twin2 = 0
coins = 0
for i in range(n):
    twin1 += arr[i]

index = n - 1
while index >= 0:
    if twin1 >= twin2: 
        twin2 += arr[index]
        twin1 -= arr[index]
        coins+=1
        index-= 1
    else:
        break

print(coins)
