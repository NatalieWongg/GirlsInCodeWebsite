n = int(input())
coins = list(map(int, input().split()))

coins.sort(reverse=True)  # sort descending
total = sum(coins)
my_sum = 0
count = 0

for coin in coins:
    my_sum += coin
    count += 1
    if my_sum > total - my_sum:
        print(count)
        break
