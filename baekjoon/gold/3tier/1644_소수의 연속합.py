# https://www.acmicpc.net/problem/1644

import math

N = int(input())
prime_lst = []
arr = [True for i in range(N + 1)]
for i in range(2, int(math.sqrt(N)) + 1) :
    if arr[i] :
        j = 2
        while i * j <= N :
            arr[i * j] = False
            j += 1

for num in range(2, N + 1) :
    if arr[num] :
        prime_lst.append(num)
    
start = 0
end = 0
answer = 0
while end <= len(prime_lst) :
    tmp = sum(prime_lst[start : end])
    if tmp == N :
        answer += 1
        end += 1
    elif tmp < N :
        end += 1
    else :
        start += 1
print(answer)