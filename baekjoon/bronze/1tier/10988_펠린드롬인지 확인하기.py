# https://www.acmicpc.net/problem/10988

str = input()
len_str = len(str)
res = 1
for i in range(round(len_str / 2)) :
    if str[i] != str[len_str - 1 - i] :
        res = 0
print(res)