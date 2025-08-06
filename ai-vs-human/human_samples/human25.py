a=[]
for i in range(len(l)):
    if l[i]==' ':
        a.append(' ')
    else:
        a.append(c[int(l[i][::-1])%26])
print(''.join(a))