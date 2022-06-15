# https://www.acmicpc.net/problem/2217

N = int(input())
rope = sorted([int(input()) for _ in range(N)], reverse = True)
rope = [rope[i] * (i + 1) for i in range(N)]
print(max(rope))