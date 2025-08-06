A = input()
B = input()
length = len(A)
flips = 0
i=0
while i<length:
    if A[i]!=B[i]:
        flips +=1
        while i<length and A[i]!=B[i]:
            i+=1
    else: i+=1
print(flips)