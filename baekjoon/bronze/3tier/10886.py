# https://www.acmicpc.net/problem/10886

answer = 0
n = int(input())
for _ in range(n) :
    answer += int(input())
if (n / 2 > answer) :
    print("Junhee is not cute!")
else :
    print("Junhee is cute!")