alomomofa = 1
alomomoja = 0
n=10000000

for i in range(n):
    alomomofa += alomomofa * 3

    if alomomofa >= 20:
        alomomoja += alomomofa // 20
        alomomofa %= 20

print(alomomofa)
print(alomomoja)