a_b = input().split()
a = int(a_b[0])
b = int(a_b[1])
c_d = input().split()
c = int(c_d[0])
d = int(c_d[1])
length1 = b-a
length2 = d- c
overlap_start = max(a, c)
overlap_end = min(b, d)
if overlap_start<overlap_end:
    overlap_length=overlap_end-overlap_start
else:
    overlap_length= 0
total_length = length1 + length2 - overlap_length
print(total_length)
