import sys

input = sys.stdin.readline
N, K = map(int, input().split())
univ_lst = []
for _ in range(N) :
    univ, team, solved, pan = input().split()
    univ_lst.append([univ, team, int(solved), int(pan)])
sort_univ = sorted(univ_lst, key = lambda x : (-x[2], x[3]))

idx = 0
cnt = 0
overlap = set()
while cnt < K :
    if sort_univ[idx][0] not in overlap :
        overlap.add(sort_univ[idx][0])
        print(sort_univ[idx][1])
        cnt += 1
    idx += 1