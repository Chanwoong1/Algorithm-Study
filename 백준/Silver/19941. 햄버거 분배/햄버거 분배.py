N, K = map(int, input().split())
ham = list(input())
for i in range(N):
    if ham[i] == "P":
        for j in range(i - K if i - K >= 0 else 0, i + K + 1 if i + K + 1 < N else N):
            if ham[j] == "H":
                ham[j] = "O"
                break
print(sum([1 for i in ham if i == "O"]))
