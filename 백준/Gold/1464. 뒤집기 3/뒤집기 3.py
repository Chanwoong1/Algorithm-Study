S = input()
for i in range(len(S) - 1) :
    if S[i] > S[i + 1] and S[0] >= S[i + 1] :
        S = S[i::-1] + S[i + 1:]
        if S[i] >= S[i + 1] :
            S = S[i + 1::-1] + S[i + 2:]
print(S)