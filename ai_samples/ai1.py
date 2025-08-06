def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        A = int(data[idx+1])
        B = int(data[idx+2])
        idx += 3
        
        photo = [data[idx + i] for i in range(N)]
        idx += N
        
        star = [[0]*N for _ in range(N)]
        used = [[0]*N for _ in range(N)]
        invalid = False
        
        for i in range(N):
            for j in range(N):
                c = photo[i][j]
                i2 = i - B
                j2 = j - A
                
                if c == 'W':
                    # Neither position can have a star
                    if 0 <= i < N and 0 <= j < N:
                        used[i][j] = 1
                    if 0 <= i2 < N and 0 <= j2 < N:
                        used[i2][j2] = 1
                elif c == 'B':
                    # Both must have a star
                    if not (0 <= i2 < N and 0 <= j2 < N):
                        invalid = True
                        break
                    star[i][j] = 1
                    star[i2][j2] = 1
                    used[i][j] = 1
                    used[i2][j2] = 1
                elif c == 'G':
                    # Exactly one of the positions must have a star
                    options = []
                    if 0 <= i < N and 0 <= j < N and not used[i][j]:
                        options.append((i,j))
                    if 0 <= i2 < N and 0 <= j2 < N and not used[i2][j2]:
                        options.append((i2,j2))
                    if not options:
                        invalid = True
                        break
                    # Assign star to one of the un-used positions
                    x, y = options[0]
                    star[x][y] = 1
                    used[x][y] = 1
            if invalid:
                break
        
        if invalid:
            results.append("-1")
        else:
            count = sum(sum(row) for row in star)
            results.append(str(count))
    
    print('\n'.join(results))
