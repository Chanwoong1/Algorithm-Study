# https://www.acmicpc.net/problem/19944

N, M = map(int, input().split())
if M in (1, 2) :
    print('NEWBIE!')
elif N < M :
    print('TLE!')
else :
    print('OLDBIE!')