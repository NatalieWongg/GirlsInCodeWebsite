arr = input().strip()
flag = False
count = 0
for i in range (len(arr) - 1):
    if arr[i] == arr[i+1]:
        flag = True
        count += 1
    elif arr[i] != arr[i+1] and count < 6:
        flag = False

if flag == True:
    print("YES")
else: 
    print("NO")