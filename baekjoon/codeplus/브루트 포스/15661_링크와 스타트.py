# https://www.acmicpc.net/problem/15661

import sys
from itertools import combinations
N = int(input())
arr = []
for _ in range(N) :
    arr.append(list(map(int, sys.stdin.readline().split())))

answer = 100000000                              # 매우 큰 수를 기본값으로
N_lst = [i for i in range(N)]
for ii in range(1, N) :
    for i in combinations(N_lst, ii) :          # 조합으로 i에 1팀이 들어감 
        t1 = 0
        t2 = 0
        lst = [a for a in range(N)]             # 2팀을 뽑기위해
        i_lst = list(i)
        for q, w in combinations(i_lst, 2) :    # 1팀의 총 점수
            t1 += (arr[q][w] + arr[w][q])
        for p in i :
            lst.remove(p)                       # 2팀 목록에서 1팀에 들어가는 숫자들 제거
        for k, l in combinations(lst, 2) :
            t2 += (arr[k][l] + arr[l][k])       # 2팀의 총 점수
        if answer > abs(t1 - t2) :              # 두 팀의 점수 차이가 answer보다 낮다면 교쳬
            answer = abs(t1 - t2)
print(answer)