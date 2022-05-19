# https://www.acmicpc.net/problem/15656

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
answer = []

def solve(depth, N, M) :
    if depth == M :
        print(' '.join(map(str, answer)))
        return
    for i in range(N) :
        answer.append(lst[i])
        solve(depth+1, N, M)
        answer.pop()

solve(0, N, M)