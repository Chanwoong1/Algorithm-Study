N, L, H = map(int, input().split())
scores = [*map(int, input().split())]
scores.sort()
print(sum(scores[L : N - H]) / (N - L - H))
