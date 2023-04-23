import sys

input = sys.stdin.readline
K, L = map(int, input().split())
success = dict()
for i in range(L):
    student = input().rstrip()
    success[student] = i

success = sorted(success.items(), key=lambda x: x[1])
for j in range(len(success) if len(success) < K else K):
    print(success[j][0])
