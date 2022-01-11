# https://www.acmicpc.net/problem/15921

N = int(input())
if N == 0 :
    print('divide by zero')
else :
    lst = list(map(int, input().split()))
    ans = sum(lst)/N / (sum(lst)/N)
    print('%.2f' % ans)