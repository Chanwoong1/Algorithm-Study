import sys
input = sys.stdin.readline
N, M = map(int, input().split())
friends = [0] * N
for _ in range(M) :
    a, b = map(int, input().split())
    friends[a - 1] += 1
    friends[b - 1] += 1
for i in friends : print(i)
