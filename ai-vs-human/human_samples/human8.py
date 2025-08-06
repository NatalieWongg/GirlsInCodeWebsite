
punctuation = [' ', ',', '.', '!', '?', '-']
count = 0
for x in range(1, len(string)):
    if not string[x-1] in punctuation and string[x] in punctuation:
        count += 1
if not string[len(string)-1] in punctuation:
    count += 1
print (count)