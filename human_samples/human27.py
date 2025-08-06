list1 = sorted(list1, key=lambda x : x[1], reverse=True)

print(list1)
print(len(list1))

if len(list1) % 2 == 0:
    print(list1[(len(list1)//2) - 1][0])
else:
    print(list1[len(list1)//2][0])