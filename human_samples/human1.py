import sys

input = sys.stdin.readline

t = int(input())

for case in range(t):
    n, a, b = map(int, input().split())
    array = []
    count = 0
    for pixel in range(n):
        array.append([str(k) for k in input().strip()])

    if a == 0 and b == 0:
        for i in range(n):
            for j in range(n):
                if array[i][j] != 'W':
                    count = count + 1
    else:
        for i in range(n):
            for j in range(n):
                if count != -1:
                    if array[i][j] == 'B':
                        if i-b>=0 and i-b < n and (j-a)>=0 :
                            if array[i-b][j-a] == 'W':
                                count = -1
                            elif array[i-b][j-a] != 'W':
                                count += 1
                        if i+b<n and i+b>=0 and (j+a)<n and count!=-1:
                            if array[i+b][j+a] == 'W':
                                count += 1
                        elif i+b>=n or i+b<0 or (j+a)>=n:
                            count += 1
                        elif i-b<0 or i-b >= n or (j-a)<0:
                            count = -1
                        
                        
                    elif array[i][j] == 'G':
                        if i-b>=0 and i-b < n and (j-a)>=0:
                            if array[i-b][j-a] != 'W':
                                count += 1
                        
                        elif i+b<n and i+b>=0 and (j+a)<n:
                            if array[i+b][j+a] == 'W':
                                count += 1
                        elif i+b>=n or i+b<0 or (j+a)>=n:
                                count += 1
                        elif i-b<0 or i-b >= n or (j-a)<0:
                            count = -1


                    
    print (count)
    #hi