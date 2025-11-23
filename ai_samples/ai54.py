import sys
input = sys.stdin.readline 
gi = lambda: list(map(int, input().split())) #for multiple integers
gs = lambda: list(input().split()) #for multiple strings

n = int(input())
for i in range (n):
    a , b = gi()
    print(a + b)