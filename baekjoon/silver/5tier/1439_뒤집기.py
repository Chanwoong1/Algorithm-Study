# https://www.acmicpc.net/problem/1439

S = list(input())
idx = 0
num1 = 0
num0 = 0
while idx < len(S) :
    if S[idx] == '1' :
        i = 0
        while idx + i < len(S) :
            if S[idx + i] != '1' :
                break
            i += 1
        idx += i
        num1 += 1
    else :
        i = 0
        while idx + i < len(S) :
            if S[idx + i] != '0' :
                break
            i += 1
        idx += i
        num0 += 1
print(min(num1, num0))
    