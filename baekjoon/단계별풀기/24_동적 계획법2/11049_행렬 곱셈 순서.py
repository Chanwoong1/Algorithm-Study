# https://www.acmicpc.net/problem/11049

# N = int(input())
# mat_lst = []
# for _ in range(N) :
#     mat_lst.append(list(map(int, input().split())))
# dp = [0]
# dp2 = [0]
# for i in range(len(mat_lst) - 1) :
#     dp.append(mat_lst[i][0] * mat_lst[i][1] * mat_lst[i + 1][1])
# for i in range(len(mat_lst) - 1, 0, -1) :
#     dp2.append(mat_lst[i - 1][0] * mat_lst[i - 1][1] * mat_lst[i][1])
# print(dp)
# print(dp2)