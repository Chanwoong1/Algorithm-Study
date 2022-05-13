# https://www.acmicpc.net/problem/16139

# str = input()
# for _ in range(int(input())) :
#     s, start, end = list(input().split())
#     start = int(start)
#     end = int(end)
#     answer = 0
#     for i in str[start : end + 1] :
#         if i == s :
#             answer += 1
#     print(answer)

import sys

input = sys.stdin.readline

name = input().strip()
n = int(input())
arr = [[0 for i in range(26)] for i in range(len(name))]
arr[0][ord(name[0]) - 97] = 1
for i in range(1, len(name)):
    arr[i][ord(name[i]) - 97] = 1
    for j in range(26):
        arr[i][j] += arr[i - 1][j]
for i in range(n):
    a = input().split()
    if int(a[1]) > 0:
        res = arr[int(
            a[2])][ord(a[0]) - 97] - arr[int(a[1]) - 1][ord(a[0]) - 97]
    else:
        res = arr[int(a[2])][ord(a[0]) - 97]
    print(res)