def sum(number):
    if number==1: return 1
    else: return sum(number-1)+number

n=int(input())
print(sum(n))
