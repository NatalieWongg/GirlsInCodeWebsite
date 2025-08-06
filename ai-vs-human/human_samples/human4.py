N = int(input())
A = list(map(int, input().split()))
 
cnt_left = [0] * (N + 1)
cnt_right = [0] * (N + 1)
for x in A:
	cnt_right[x] += 1
 
ans = 0
distinct_left = 0
 
for i in range(N):
	if cnt_right[A[i]] == 2:
		ans += distinct_left - (cnt_left[A[i]] > 0)
	cnt_right[A[i]] -= 1
	distinct_left += cnt_left[A[i]] == 0
	cnt_left[A[i]] += 1
 
print(ans)