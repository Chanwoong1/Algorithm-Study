# https://www.acmicpc.net/problem/1904

'''
메모리 초과
N = int(input())
answer = [1, 2, 3, 5]
if N > 4 :
    for i in range(4, N + 1) :
        answer.append(answer[i-1] + answer[i-2])
    if answer[N-1] < 15746 :
        print(answer[N-1])
    else :
        print(answer[N-1]%15746)
else :
    print(answer[N-1])
'''

N = int(input())
n1 = 1
n2 = 2
res = 1 if N == 1 else 2

for i in range(3, N+1):
    res = (n1 + n2) % 15746
    n1, n2 = n2, res
print(res)