# https://www.acmicpc.net/problem/21300

lst = list(map(int, input().split()))
# answer = 0
# for i in lst :
#     if i == 0 :
#         answer += 5
#     else :
#         answer += i * 2
print(sum(lst) * 5)