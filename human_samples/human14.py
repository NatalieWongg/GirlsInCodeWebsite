
s = "paabcdefghihisjfiejvjfpojojvjfpowfuohwgirlscodedocslrigajojgijriowoifnvkrirlhjshreifpsjdgjdlskfjb"
longest = ""
length=len(s)
for i in range(length):
    for j in range(i + 1, length + 1):
        substring = s[i:j]
        if substring == substring[::-1] and len(substring) > len(longest):
            longest = substring
            
print(longest)