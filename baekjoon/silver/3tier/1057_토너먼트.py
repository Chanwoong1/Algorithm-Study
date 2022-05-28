# https://www.acmicpc.net/problem/1057

N, kim, lim = list(map(int, input().split()))
count = 0
while kim != lim :
    kim -= kim // 2
    lim -= lim // 2
    count += 1
print(count)