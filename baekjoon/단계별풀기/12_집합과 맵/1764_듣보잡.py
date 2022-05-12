# https://www.acmicpc.net/problem/1764

N, M = list(map(int, input().split()))
n_lst = set()
m_lst = set()
for _ in range(N) :
    n_lst.add(input())
for _ in range(M) :
    m_lst.add(input())

answer = sorted(list(n_lst & m_lst))
print(len(answer))
for i in answer :
    print(i)