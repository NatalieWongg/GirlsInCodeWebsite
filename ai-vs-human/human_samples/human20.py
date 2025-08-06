read = open("traffic.in","r")
write = open("traffic.out","w")

n = int(read.readline())
curr = [0,0]
start = [0,0]
on = [0,0]
off = [0,0]
i = 0
prev =''
while start == [0,0]:
    line = read.readline().split()
    print(line)
    if line[0] == 'none':
        if prev == "":
            start[0],start[1] = line[1],line[2]
        elif prev == "on":
            start[0],start[1] = line[1],line[2]-on[1]
        elif prev == "off":
            start[0],start[1] = line[1]+off[1],line[2]-off[1]
    elif line[0] == 'on':
        prev = "on"
        on[0],on[1] = line[1],line[2]
    elif line [0] == "off":
        prev = 'off'
        off[0],off[1] = line[1],line[2]
    print(start)
    print(on)

print(start)
    

