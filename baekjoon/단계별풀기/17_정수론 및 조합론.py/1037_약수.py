# https://www.acmicpc.net/problem/1037

int(input())    # 첫째 줄은 버림
lst = sorted(list(map(int, input().split())))

if len(lst) == 1 :  # 특수한 경우
    print(lst[0] * lst[0])
else :              # 그 외의 경우
    print(lst[0] * lst[-1])