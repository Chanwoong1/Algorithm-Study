# https://www.acmicpc.net/problem/5554

sum = 0
for _ in range(4) :
    sum += int(input())
print(sum // 60)
print(sum % 60)