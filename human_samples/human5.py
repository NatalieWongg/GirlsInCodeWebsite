n, u = (int(x) for x in input().split())
g = [[x == '#' for x in input()] for _ in range(n)]

best = n*n
for grid in range(2 ** ((n*n)//4)):
  wrongcount = 0
  for i in range(n):
    for j in range(n):
      truei = min(i, n-1-i)
      truej = min(j, n-1-j)
      if g[i][j] != ((grid & (2 ** (truei * (n // 2) + truej))) != 0): wrongcount += 1
  best = min(best, wrongcount)

print(best)
for _ in range(u):
  a, b = (int(x)-1 for x in input().split())
  g[a][b] = not g[a][b]
  print(best)
