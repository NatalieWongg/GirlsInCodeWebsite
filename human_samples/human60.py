for _ in range(int(input())):
    S = input()
    pairs = 0
    i = 0
    while i < len(S)-1:
        if (S[i] == 'x' and S[i+1] == 'y') or (S[i] == 'y' and S[i+1] == 'x'):
            pairs += 1
            i += 2
        else:
            i += 1
    print(pairs)