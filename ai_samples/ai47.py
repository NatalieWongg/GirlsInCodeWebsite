s = input().strip()
count = 1  # start with 1 because the first char counts
dangerous = False

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
        if count >= 7:
            dangerous = True
            break
    else:
        count = 1  # reset count when sequence breaks

if dangerous:
    print("YES")
else:
    print("NO")
