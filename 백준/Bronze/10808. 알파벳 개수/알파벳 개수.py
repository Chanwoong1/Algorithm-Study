alpha = [0] * 26
S = input()
for i in range(len(S)) :
    alpha[ord(S[i]) - 97] += 1
print(*alpha)
