a=[[0]*len(l[0]) for _ in range(len(l))]
r=[]




for i in range(len(l)-1):
    for j in range(len(l[0])-1):
        if l[i][j]<l[i][j+1]:
            a[i][j+1]+=1
        elif l[i][j]>l[i][j+1]:
            a[i][j]+=1
        if l[i][j]>l[i+1][j]:
            a[i+1][j]+=1
        elif l[i][j]<l[i+1][j]:
            a[i][j]+=1

for i in range(len(a)):
    for j in range(len(a[0])):
        if (a[i][j]==4) or (((i==0 and j==0) or (i==0 and j==len(a[0])-1) or (i==len(a)-1 and j==0) or (i==len(a)-1 or j==len(a[0])-1)) and a[i][j]==2):
            r.append((i,j))


f.write(str(r))