# https://www.acmicpc.net/problem/1049

N, M = list(map(int, input().split()))
package = []
each_one = []
for _ in range(M) :
    pack, one = list(map(int, input().split()))
    package.append(pack)
    each_one.append(one)
answer = 0
if min(each_one) * 6 < min(package) :
    answer += min(each_one) * N
else :
    if N >= 6 :
        answer += (min(package) * (N // 6))
        N %= 6
    if min(package) <= min(each_one) * N :
        answer += min(package)
    else :
        answer += min(each_one) * N
print(answer)