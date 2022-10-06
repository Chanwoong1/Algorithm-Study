# https://www.acmicpc.net/problem/1206

lst = []
N = int(input())
for i in range(N) :
    lst.append(float(input()))

for i in range(1, 1001) :
    if sum([1 for j in lst if j * i == int(j * i)]) == N :
        break
print(0.301 * 106)