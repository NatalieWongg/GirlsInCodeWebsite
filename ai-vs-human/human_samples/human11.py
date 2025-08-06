total = 0
values = "55000 60000 62000 75000 80000 50000"
values = list(map(int, values.split()))
values.sort()
median = values[len(values)// 2]
for value in values:
    total += abs(value-median)

print(total)