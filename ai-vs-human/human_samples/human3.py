perm = []
all = []
string = input()
length = len(string)
chosen = [0]*26
for c in string:
    chosen[ord(c) - ord('a')] += 1
 
 
def p(perm:str=""):
    if len(perm) == length:
        all.append(perm)
        return
    for i in range(26):
        if chosen[i] > 0:
            chosen[i] -= 1
            p(perm + chr(ord("a") + i))
            chosen[i] += 1
 
p()
print(len(all))
for n in all:
    print(n)