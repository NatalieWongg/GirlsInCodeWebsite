def total_painted_length(a, b, c, d):
    length1 = b - a
    length2 = d - c
    overlap = max(0, min(b, d) - max(a, c))
    return length1 + length2 - overlap

print(total_painted_length(a, b, c, d))  
