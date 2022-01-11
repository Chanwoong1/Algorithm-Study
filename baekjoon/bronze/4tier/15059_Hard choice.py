# https://www.acmicpc.net/problem/15059

A, B, C = map(int, input().split())
a, b, c = map(int, input().split())
answer = 0
if A - a < 0 :
    answer += a - A
if B - b < 0 :
    answer += b - B
if C - c < 0 :
    answer += c - C
print(answer)
            