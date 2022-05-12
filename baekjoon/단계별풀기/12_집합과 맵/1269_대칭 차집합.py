# https://www.acmicpc.net/problem/1269

N, M = list(map(int, input().split()))
n_lst = set(map(int, input().split()))
m_lst = set(map(int, input().split()))
print(len(n_lst - m_lst) + len(m_lst - n_lst))